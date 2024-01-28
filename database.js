const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  password: 'eliisabet', // add your password
  database: 'homework4',
  host: 'localhost',
  port: '5432'
});

const execute = async (query) => {
  try {
    await pool.connect();
    await pool.query(query);
    return true;
  } catch (error) {
    console.error(error.stack);
    return false;
  }
};

const createMovieTableQuery = `
  CREATE TABLE IF NOT EXISTS "movies" (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL UNIQUE,
    director VARCHAR(200) NOT NULL,
    length INTEGER NOT NULL,
    releasedate timestamp NOT NULL,
    imdb DECIMAL(3, 1),
    letterboxd DECIMAL(3, 1),
    rottentomatoes DECIMAL(3),
    summary TEXT,
    photo VARCHAR(1000)
  );
`;

// Insert sample movie data
const insertMovieDataQuery = `
  INSERT INTO "movies" (name, director, length, releasedate, imdb, letterboxd, rottentomatoes, summary, photo)
  VALUES
    ('Poor Things', 'Yorgos Lanthymos', 141, '2022-01-01', 7.5, 3.5, 80, 'A great movie with an interesting plot.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/PoorThings_1350x2000.jpg'),
    ('Movie2', 'Director2', 110, '2022-02-15', 8.2, 4.0, 92, 'An exciting film with superb performances.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/PoorThings_1350x2000.jpg'),
    ('Movie3', 'Director3', 95, '2022-03-30', 6.5, 3.0, 70, 'A classic that stands the test of time.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/PoorThings_1350x2000.jpg'),
    ('Movie4', 'Director4', 130, '2022-04-20', 9.0, 4.5, 95, 'An epic masterpiece that everyone should watch.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/PoorThings_1350x2000.jpg'),
    ('The Beekeeper', 'David Ayer', 120, '2024-01-01', 7.1, 3.5, 71, 'A thrilling action movie with Jason Statham.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/TheBeekeeper_1350x2000.jpg'),
    ('Saltburn', 'Emerald Fennell', 115, '2023-12-15', 7.1, 3.5, 71, 'A beautifully wicked tale of privilege and desire.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/Saltburn_1350x2000.jpg'),
    ('Mean Girls', 'Samantha Jayne, Arturo Perez Jr.', 100, '2024-02-01', 7.0, 3.5, 70, 'A new twist on the modern classic.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/MeanGirls_1350x2000.jpg'),
    ('I.S.S.', 'Gabriela Cowperthwaite', 110, '2023-12-20', 6.4, 3.2, 64, 'A thrilling drama set in the near future.', 'https://mcswebsites.blob.core.windows.net/1011/Event_7104/portrait_micro/ISS_1350x2000.jpg');
  `;

execute(createMovieTableQuery)
  .then((result) => {
    if (result) {
      console.log('Table "movies" is created');
      // After creating the table, insert sample data
      return execute(insertMovieDataQuery);
    }
  })
  .then((insertResult) => {
    if (insertResult) {
      console.log('Sample data inserted into the "movies" table');
    }
  });

module.exports = pool;
