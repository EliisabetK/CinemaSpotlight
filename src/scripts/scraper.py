import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from datetime import datetime
import requests
import json

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

# Function to scrape movie data from the Apollo page
def scrape_movie_data(url, api_key):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    # Replace these selectors with the actual HTML elements from the target website
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
            movies.append({
                'title': title,
                'link': link,
                'cover': cover,
                'director': director,  # Add director to movie data
                'runtime': runtime_in_minutes,
                'releasedate': releasedate,  # Add releasedate to movie data
                'summary': summary,  # Add summary to movie data
                'score': score,  # Add the score to your movie data
            })
        print(f"Title: {title}, Director: {director}, Length: {runtime_in_minutes}, Summary: {summary}, Score: {score}")
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
save_to_database(movies_data)
