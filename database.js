//see ei saa hakkama posts tabeli tegemisega, users tabel töötab

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

// Create "users" table
const createUserTableQuery = `
  CREATE TABLE IF NOT EXISTS "users" (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL 
  );
`;

execute(createUserTableQuery).then((result) => {
  if (result) {
    console.log('Table "users" is created');
  }
});

const createPostsTableQuery = `
  CREATE TABLE IF NOT EXISTS "posts" (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES "users"(id),
    post_text VARCHAR(1000) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
`;

execute(createPostsTableQuery).then((result) => {
  if (result) {
    console.log('Table "posts" is created');
  }
});

module.exports = pool;
