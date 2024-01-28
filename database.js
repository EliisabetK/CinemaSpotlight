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
    director VARCHAR(200),
    length INTEGER,
    releasedate timestamp,
    tmdb DECIMAL(3, 1),
    summary TEXT,
    photo VARCHAR(1000)
  );
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
