import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from datetime import datetime
import re 

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

# Function to scrape IMDb score from a movie details page
def scrape_imdb_score(details_soup):
    # Extract IMDb score
    imdb_score_element = details_soup.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
    imdb_score_str = imdb_score_element.text if imdb_score_element else None
    imdb_score = float(imdb_score_str) if imdb_score_str else None
    return imdb_score

def scrape_letterboxd_scores(letterboxd_url):
    response = requests.get(letterboxd_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    # Replace this selector with the actual HTML element from the Letterboxd page
    movie_elements = soup.select('.frame.has-menu')

    for movie_element in movie_elements:
        title_element = movie_element.select_one('.frame-title')
        score_str = movie_element['data-original-title'].split(' ')[-1]
        score = float(score_str) if score_str else None

        movies.append({
            'title': title_element.text.strip(),
            'letterboxd_score': score
        })

    return movies


# Function to scrape movie data from the Apollo page
def scrape_movie_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

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

        summary_element = details_soup.select_one('.movie-details__description .text')
        summary = trim_summary(summary_element.text.strip()) if summary_element else None

        title = title_element.text.strip()
        link = title_element['href']
        cover = cover_element['data-srcset'].split(' ')[-2]  # Extracting the last URL in the srcset

        # Process the image link
        cover = process_image_link(cover)

        # Convert the runtime to minutes
        runtime_in_minutes = convert_runtime_to_minutes(runtime)

        # Convert the release date to timestamp
        releasedate_element = details_soup.find('p', string='In Cinemas')
        releasedate_str = releasedate_element.find_next_sibling('p').text.strip() if releasedate_element else None

        # Adjust the date format
        releasedate = datetime.strptime(releasedate_str, '%m/%d/%Y') if releasedate_str else None

        movies.append({
            'title': title,
            'link': link,
            'cover': cover,
            'director': director,
            'runtime': runtime_in_minutes,
            'in_cinemas': in_cinemas,
            'summary': summary,
            'releasedate': releasedate,
        })
        print(f"Title: {title}, Director: {director}, Runtime: {runtime_in_minutes} minutes")

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

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(200) NOT NULL UNIQUE,
            director VARCHAR(200),
            length INTEGER,
            releasedate timestamp,
            imdb DECIMAL(3, 1),
            letterboxd DECIMAL(3, 1),
            rottentomatoes DECIMAL(3),
            summary TEXT,
            photo VARCHAR(1000)
        )
    ''')

    # Insert data into the table with ON CONFLICT clause, only if director is not None
    for movie in movies:
        if movie['director'] is not None:
            cursor.execute(sql.SQL('''
                INSERT INTO movies (name, director, length, releasedate, summary, photo)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET director = EXCLUDED.director,
                    length = EXCLUDED.length,
                    releasedate = EXCLUDED.releasedate,
                    summary = EXCLUDED.summary,
                    photo = EXCLUDED.photo
            '''), (movie['title'], movie['director'], movie['runtime'], movie['releasedate'], movie['summary'], movie['cover']))

    conn.commit()
    conn.close()

# Example usage
url = 'https://www.apollokino.ee/eng/movies?fromLang=1001'
movies_data = scrape_movie_data(url)
save_to_database(movies_data)

