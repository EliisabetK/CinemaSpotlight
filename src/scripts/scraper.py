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

# function to convert movie length like '2h15' to minutes
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

# function to trim the summary to 1000 characters if necessary
def trim_summary(summary):
    if summary and len(summary) > 1000:
        last_period_index = summary[:1000].rfind('.')
        
        if last_period_index != -1:
            return summary[:last_period_index + 1] 
        else:
            return summary[:1000]
    else:
        return summary


def process_image_link(cover):
    cover = "http://" + cover
    cover = cover.replace('//images.markus.live/', '').split('?')[0]
    cover = cover.split('.jpg')[0] + '.jpg'

    return cover

def get_movie_details_from_tmdb(title, api_key):
    base_url = f'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': api_key, 'query': title}
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        movie_details = json.loads(response.text)
        if movie_details['results']:
            return movie_details['results'][0]
    return None


def get_movie_score_from_rt(title):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=service, options=options)

    base_url = f'https://www.rottentomatoes.com/search?search={title}'

    driver.get(base_url)
    
    try:
        try:
            button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        except NoSuchElementException:
            print("Could not find element with ID 'onetrust-accept-btn-handler'")
        button.click()

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.TAG_NAME, 'search-page-media-row'))
        )
        score = element.get_attribute('tomatometerscore')
        
    except TimeoutException:
        score = None
        print("Accept button not found or not clickable within 1 second.")

    driver.quit()
    return score

def get_movie_score_from_letterboxd(title):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=service, options=options)

    base_url = f'https://letterboxd.com/search/films/{title}'
    driver.get(base_url)

    try:
        #consent_button = WebDriverWait(driver, 5).until(
        #    EC.presence_of_element_located((By.XPATH, '//p[text()="Consent"]'))
        #)
        #consent_button.click()

        first_movie_element = WebDriverWait(driver, 1.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.film-poster'))
        )

        WebDriverWait(driver, 1.5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.fc-dialog-overlay'))
        )

        first_movie_element.click()

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
    movie_elements = soup.select('.movie-card')

    for movie_element in movie_elements:
        title_element = movie_element.select_one('.movie-card__title a')
        cover_element = movie_element.select_one('.image__img')

        if 'OPERA' in title_element.text.upper() or 'BALLET' in title_element.text.upper():
            continue

        details_url = title_element['href']
        details_response = requests.get(details_url)
        details_soup = BeautifulSoup(details_response.text, 'html.parser')

        director_element = details_soup.find('p', string='Director')
        director = director_element.find_next_sibling('p').text.strip() if director_element else None

        runtime_element = details_soup.find('p', string='Run time')
        runtime = runtime_element.find_next_sibling('p').text.strip() if runtime_element else None

        in_cinemas_element = details_soup.find('p', string='In Cinemas')
        in_cinemas = in_cinemas_element.find_next_sibling('p').text.strip() if in_cinemas_element else None

        if in_cinemas is not None:
            releasedate = datetime.datetime.strptime(in_cinemas, '%m/%d/%Y')
        else:
            releasedate = None

        summary_element = details_soup.select_one('.movie-details__description .text')
        summary = trim_summary(summary_element.text.strip()) if summary_element else None

        title = title_element.text.strip()
        cover = cover_element['data-srcset'].split(' ')[-2]

        cover = process_image_link(cover)

        runtime_in_minutes = convert_runtime_to_minutes(runtime)

        tmdb=get_movie_details_from_tmdb(title, api_key)
        if tmdb is not None:
            tmdb_score = tmdb['vote_average']
        else:
            tmdb_score = None
        letterboxd_score = get_movie_score_from_letterboxd(title)
        rt_score = get_movie_score_from_rt(title)

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

api_key = 'de150413238cb1ec0252f5c6374f3691'
url = 'https://www.apollokino.ee/eng/movies?fromLang=1001'
movies_data = scrape_movie_data(url, api_key)

#movies = [{'title': 'Beautiful Wedding', 'link': 'https://www.apollokino.ee/eng/event/5429/beautiful_wedding?theatreAreaID=1004', 'cover': 'http://mcswebsites.blob.core.windows.net/1013/Event_8890/landscape_fullhd/BeautifulWedding_3840x2160PX.jpg', 'director': 'Roger Kumble', 'runtime': 100, 'releasedate': datetime.datetime(2024, 2, 9, 0, 0), 'summary': 'It follows Abby and Travis, who after a crazy night in Las Vegas, discover they are married. They head to Mexico for a honeymoon with friends and family.', 'tmdb_score': 5.7, 'letterboxd_score': None, 'rt_score': ''}]
