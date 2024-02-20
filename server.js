const express = require('express');
const pool = require('./database');
const cors = require('cors');
const cookieParser = require('cookie-parser');
const port = process.env.PORT || 3000;
const app = express();

app.use(cors({ origin: 'http://localhost:8080', credentials: true }));
app.use(express.json()); 
app.use(cookieParser());

app.listen(port, () => {
    console.log("Server is listening to port " + port)
});

app.get('/api/movies', async (req, res) => {
    try {
      console.log('Get movies request has arrived');
      const movies = await pool.query('SELECT * FROM movies');
      res.json(movies.rows);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });
  
  app.get('/api/movies/:id', async (req, res) => {
    const movieId = req.params.id;
    try {
      console.log('Get movie by ID request has arrived');
      const result = await pool.query('SELECT * FROM movies WHERE id = $1', [movieId]);
      if (result.rows.length === 0) {
        res.status(404).json({ error: 'Movie not found' });
      } else {
        res.json(result.rows[0]);
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal Server Error' });
    }
  });