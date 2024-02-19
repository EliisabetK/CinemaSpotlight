import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
import datetime
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Function to convert movie length like '2h15' to minutes
def convert_runtime_to_minutes(runtime):
    if 'h' in runtime and 'min' in runtime:
        hours, minutes = map(int, runtime.replace('h', '').replace('min', '').split(' '))
        return hours * 60 + minutes
    elif 'h' in runtime:
        return int(runtime.replace('h', '')) * 60
    elif 'min' in runtime:
        return int(runtime.replace('min', ''))
    else:
        return None

# Function to trim the summary to 1000 characters if necessary
def trim_summary(summary):
    if summary and len(summary) > 1000:
        # Find the last occurrence of a period within the first 1000 characters
        last_period_index = summary[:1000].rfind('.')
        
        # If a period is found within the first 1000 characters, trim the summary up to that point
        if last_period_index != -1:
            return summary[:last_period_index + 1]  # Include the period in the trimmed summary
        else:
            # If no period is found within the first 1000 characters, simply trim the summary to 1000 characters
            return summary[:1000]
    else:
        return summary


# Function to process image links
def process_image_link(cover):
    # Add "http://" to the beginning of the image link
    cover = "http://" + cover
    # Remove unnecessary parts from the image link
    cover = cover.replace('//images.markus.live/', '').split('?')[0]
    # Remove everything that comes after .jpg
    cover = cover.split('.jpg')[0] + '.jpg'

    return cover

# Function to get movie details from TMDB API
def get_movie_details_from_tmdb(title, api_key):
    base_url = f'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': api_key, 'query': title}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        movie_details = json.loads(response.text)
        if movie_details['results']:
            return movie_details['results'][0]  # Return the first result
    return None


# Function to get movie score from IMDb using Selenium
def get_movie_score_from_rt(title):
    # Setup Selenium
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')  # Suppress console logs
    driver = webdriver.Chrome(service=service, options=options)

    base_url = f'https://www.rottentomatoes.com/search?search={title}'

    driver.get(base_url)
    
    try:
        try:
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        except NoSuchElementException:
            print("Could not find element with ID 'onetrust-accept-btn-handler'")
        button.click()

        # Wait for the movie page to load and find the score element
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.TAG_NAME, 'search-page-media-row'))
        )
        score = element.get_attribute('tomatometerscore')
        
    except TimeoutException:
        score = None
        print("Accept button not found or not clickable within 1 second.")

    driver.quit()
    return score

# Function to get movie score from Letterboxd using Selenium
def get_movie_score_from_letterboxd(title):
    # Setup Selenium
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')  # Suppress console logs
    driver = webdriver.Chrome(service=service, options=options)

    base_url = f'https://letterboxd.com/search/films/{title}'
    driver.get(base_url)

    try:
        # Wait for the consent button to load and click it
        #consent_button = WebDriverWait(driver, 5).until(
        #    EC.presence_of_element_located((By.XPATH, '//p[text()="Consent"]'))
        #)
        #consent_button.click()

        # Wait for the page to load and find the first movie element
        first_movie_element = WebDriverWait(driver, 1.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.film-poster'))
        )

        # Wait until the overlay is no longer present
        WebDriverWait(driver, 1.5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.fc-dialog-overlay'))
        )

        first_movie_element.click()

        # Wait for the movie page to load and find the score element
        score_element = WebDriverWait(driver,1.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.average-rating'))
        )
        score = float(score_element.text.strip())
    except TimeoutException:
        score = None

    driver.quit()
    return score

def scrape_movie_data(url, api_key):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Replace these selectors with the actual HTML elements from the target website
    movie_elements = soup.select('.movie-card')

    for movie_element in movie_elements:
        # Extracting data
        title_element = movie_element.select_one('.movie-card__title a')
        cover_element = movie_element.select_one('.image__img')

        # Exclude movies with "OPERA" or "BALLET" in the title
        if 'OPERA' in title_element.text.upper() or 'BALLET' in title_element.text.upper():
            continue

        # Extract details from the movie details page
        details_url = title_element['href']
        details_response = requests.get(details_url)
        details_soup = BeautifulSoup(details_response.text, 'html.parser')

        # Use find_next_sibling to locate the next sibling element after the specified key element
        director_element = details_soup.find('p', string='Director')
        director = director_element.find_next_sibling('p').text.strip() if director_element else None

        runtime_element = details_soup.find('p', string='Run time')
        runtime = runtime_element.find_next_sibling('p').text.strip() if runtime_element else None

        in_cinemas_element = details_soup.find('p', string='In Cinemas')
        in_cinemas = in_cinemas_element.find_next_sibling('p').text.strip() if in_cinemas_element else None

        # Check if in_cinemas is not None before converting it to datetime
        if in_cinemas is not None:
            releasedate = datetime.datetime.strptime(in_cinemas, '%m/%d/%Y')
        else:
            releasedate = None

        summary_element = details_soup.select_one('.movie-details__description .text')
        summary = trim_summary(summary_element.text.strip()) if summary_element else None

        title = title_element.text.strip()
        cover = cover_element['data-srcset'].split(' ')[-2]  # Extracting the last URL in the srcset

        # Process the image link
        cover = process_image_link(cover)

        # Convert the runtime to minutes
        runtime_in_minutes = convert_runtime_to_minutes(runtime)

        tmdb=get_movie_details_from_tmdb(title, api_key)
        if tmdb is not None:
            tmdb_score = tmdb['vote_average']
        else:
            tmdb_score = None
        letterboxd_score = get_movie_score_from_letterboxd(title)
        rt_score = get_movie_score_from_rt(title)

        # Insert the movie into the database
        insert_movie_into_database(title, director, runtime_in_minutes, releasedate, summary, cover, tmdb_score, rt_score, letterboxd_score)

        print(f"Title: {title}, Director: {director}, Length: {runtime}, Summary: {summary}, TMDB Score: {tmdb_score}, Letterboxd Score: {letterboxd_score}, Rotten Tomatoes Score: {rt_score}")

def insert_movie_into_database(title, director, runtime, releasedate, summary, cover, tmdb_score, rt_score, letterboxd_score):
    conn = psycopg2.connect(
        host="localhost",
        database="homework4",
        user="postgres",
        password="eliisabet"
    )
    cursor = conn.cursor()

    # Insert data into the table with ON CONFLICT clause, only if director is not None
    tmdb_score = float(tmdb_score) if tmdb_score not in ('', None) else None
    rt_score = float(rt_score) if rt_score not in ('', None) else None
    letterboxd_score = float(letterboxd_score) if letterboxd_score not in ('', None) else None

    cursor.execute(sql.SQL('''
        INSERT INTO movies (name, director, length, releasedate, summary, photo, tmdb_score, rt_score, letterboxd_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (name) DO UPDATE
        SET director = EXCLUDED.director,
            length = EXCLUDED.length,
            releasedate = EXCLUDED.releasedate,
            summary = EXCLUDED.summary,
            photo = EXCLUDED.photo,
            tmdb_score = EXCLUDED.tmdb_score,
            rt_score = EXCLUDED.rt_score,
            letterboxd_score = EXCLUDED.letterboxd_score
    '''), (title, director, runtime, releasedate, summary, cover, tmdb_score, rt_score, letterboxd_score))

    conn.commit()
    conn.close()


# Example usage
api_key = 'de150413238cb1ec0252f5c6374f3691'
url = 'https://www.apollokino.ee/eng/movies?fromLang=1001'
movies_data = scrape_movie_data(url, api_key)
movies = [{'title': 'Beautiful Wedding', 'link': 'https://www.apollokino.ee/eng/event/5429/beautiful_wedding?theatreAreaID=1004', 'cover': 'http://mcswebsites.blob.core.windows.net/1013/Event_8890/landscape_fullhd/BeautifulWedding_3840x2160PX.jpg', 'director': 'Roger Kumble', 'runtime': 100, 'releasedate': datetime.datetime(2024, 2, 9, 0, 0), 'summary': 'It follows Abby and Travis, who after a crazy night in Las Vegas, discover they are married. They head to Mexico for a honeymoon with friends and family.', 'tmdb_score': 5.7, 'letterboxd_score': None, 'rt_score': ''}]
