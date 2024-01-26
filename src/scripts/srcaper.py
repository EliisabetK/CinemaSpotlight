import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# Function to scrape movie data from the website
def scrape_movie_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    
    # Replace these selectors with the actual HTML elements from the target website
    movie_elements = soup.select('.movie-container')

    for movie_element in movie_elements:
        # Extracting data
        name = movie_element.select_one('.movie-title').text.strip()
        release_date_str = movie_element.select_one('.release-date').text.strip()
        release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
        length = int(movie_element.select_one('.movie-length').text.strip().split(' ')[0])
        director = movie_element.select_one('.director').text.strip()

        movies.append({
            'name': name,
            'release_date': release_date,
            'length': length,
            'director': director
        })

    return movies

# Function to save data to SQLite database
def save_to_database(movies):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            release_date DATE,
            length INTEGER,
            director TEXT
        )
    ''')

    # Insert data into the table
    for movie in movies:
        cursor.execute('''
            INSERT INTO movies (name, release_date, length, director)
            VALUES (?, ?, ?, ?)
        ''', (movie['name'], movie['release_date'], movie['length'], movie['director']))

    conn.commit()
    conn.close()

# Example usage
url = 'https://example.com/movies'
movies_data = scrape_movie_data(url)
save_to_database(movies_data)
