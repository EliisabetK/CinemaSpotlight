import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from datetime import datetime
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
    return summary[:1000] if summary else None

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
        button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
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
        consent_button = WebDriverWait(driver, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '//p[text()="Consent"]'))
        )
        consent_button.click()

        # Wait for the page to load and find the first movie element
        first_movie_element = WebDriverWait(driver, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.film-poster'))
        )

        # Wait until the overlay is no longer present
        WebDriverWait(driver, 0.5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.fc-dialog-overlay'))
        )

        first_movie_element.click()

        # Wait for the movie page to load and find the score element
        score_element = WebDriverWait(driver, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.average-rating'))
        )
        score = float(score_element.text.strip())
    except TimeoutException:
        score = None

    driver.quit()
    return score


# Function to scrape movie data from the Apollo page
def scrape_movie_data(url, api_key):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    movie_elements = soup.select('.movie-card')
    for movie_element in movie_elements:
        score = None

        # Extracting data
        title_element = movie_element.select_one('.movie-card__title a')
        cover_element = movie_element.select_one('.image__img')
        summary_element = movie_element.select_one('.movie-card__details .description')

        # Exclude movies with "OPERA" or "BALLET" in the title
        if 'OPERA' in title_element.text.upper() or 'BALLET' in title_element.text.upper():
            continue

        title = title_element.text.strip()
        title = title.replace('Cinema Classics: ', '')  # Remove prefix if it exists

        link = title_element['href']
        cover = cover_element['data-srcset'].split(' ')[-2]  # Extracting the last URL in the srcset

        # Process the image link
        cover = process_image_link(cover)

        # Convert the runtime to minutes
        runtime_element = movie_element.select_one('.movie-card__duration span')
        runtime_in_minutes = convert_runtime_to_minutes(runtime_element.text.strip()) if runtime_element else None

        # Extract summary
        summary = trim_summary(summary_element.text.strip()) if summary_element else None

        tmdb_movie_details = get_movie_details_from_tmdb(title, api_key)
        if tmdb_movie_details:
            # Extract director information
            director = ', '.join([crew['name'] for crew in tmdb_movie_details.get('crew', []) if crew['job'] == 'Director'])

            # Extract releasedate information
            releasedate_str = tmdb_movie_details.get('release_date')
            releasedate = datetime.strptime(releasedate_str, '%Y-%m-%d') if releasedate_str else None

            score = tmdb_movie_details['vote_average']

        # Get the Letterboxd score
        letterboxd_score = get_movie_score_from_letterboxd(title)
        rt_score = get_movie_score_from_rt(title)

        movies.append({
            'title': title,
            'link': link,
            'cover': cover,
            'director': director,
            'runtime': runtime_in_minutes,
            'releasedate': releasedate,
            'summary': summary,
            'score': score,
            'letterboxd_score': letterboxd_score, 
            'rt_score': rt_score,
                })
        print(f"Title: {title}, Director: {director}, Length: {runtime_in_minutes}, Summary: {summary}, TMDB Score: {score}, Letterboxd Score: {letterboxd_score}, Rotten Tomatoes Score: {rt_score}")
    return movies

# Function to save data to PostgreSQL database
def save_to_database(movies):
    conn = psycopg2.connect(
        host="localhost",
        database="homework4",
        user="postgres",
        password="eliisabet"
    )
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS movies')

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(200) NOT NULL UNIQUE,
            director VARCHAR(200),
            length INTEGER,
            releasedate timestamp,
            summary TEXT,
            photo VARCHAR(1000),
            score DECIMAL(3, 1)
        )
    ''')

    # Insert data into the table with ON CONFLICT clause, only if director is not None
    for movie in movies:
        cursor.execute(sql.SQL('''
            INSERT INTO movies (name, director, length, releasedate, photo, score)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (name) DO UPDATE
            SET director = EXCLUDED.director,
                length = EXCLUDED.length,
                releasedate = EXCLUDED.releasedate,
                photo = EXCLUDED.photo,
                score = EXCLUDED.score  -- Update the score
        '''), (movie['title'], movie['director'], movie['runtime'], movie['releasedate'], movie['cover'], movie['score']))

    conn.commit()
    conn.close()

# Example usage
api_key = 'de150413238cb1ec0252f5c6374f3691'
url = 'https://www.apollokino.ee/eng/movies?fromLang=1001'
movies_data = scrape_movie_data(url, api_key)
