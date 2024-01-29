<template>
  <div>
    <div class="container2">
      <main>
        <div class="contacts">
          <div class="contacts-content">
            <div class="additional-info">
              <h2>This page is for learning and entertainment only, not for commercial use.</h2>
              <p>
                It finds the best movies playing in cinemas, so you won't miss the movie of the year.
              </p>
            </div>
        
            <div class="feedback-box">
              <h3>Feedback: </h3>
              <form>      
              <input name="name" type="text" class="feedback-input" placeholder="Name" />   
              <input name="email" type="text" class="feedback-input" placeholder="Email" />
              <textarea name="text" class="feedback-input" placeholder="Comment"></textarea>
              <input type="submit" value="SUBMIT"/>
            </form>
            </div>
            <div class="references">
              <h2>References:</h2>
              <ul>
                <li>
                  <a href="https://developer.themoviedb.org/docs/getting-started" target="_blank">The website uses TMDb API</a>
                </li>
                <li>
                  <a href="https://www.apollokino.ee" target="_blank">Apollo Kino</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contacts",
  data() {
    return {
      feedback: "",
    };
  },
  methods: {
    submitFeedback() {
      // Implement your logic to handle the submitted feedback
      console.log("Feedback submitted:", this.feedback);
      // You can send the feedback to your server, save it to a database, etc.
      // Clear the feedback textarea after submission
      this.feedback = "";
    },
  },
};
</script>

<style scoped>
form { 
  max-width:420px; 
  margin:50px auto; 
  color: var(--text-light)
}

.feedback-input {
  color:var(--text-light);
  font-weight:500;
  font-size: 18px;
  border-radius: 5px;
  line-height: 22px;
  background-color: transparent;
  border:2px solid var(--text-light);
  transition: all 0.3s;
  padding: 13px;
  margin-bottom: 15px;
  width:100%;
  box-sizing: border-box;
  outline:0;
}

input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active {
  -webkit-box-shadow: 0 0 0 30px var(--secondary-dark) inset !important;
  -webkit-text-fill-color: var(--text-light) !important; 
}
.feedback-input:focus { 
  border:2px solid var(--accent-dark); 
}

textarea {
  height: 150px;
  line-height: 150%;
  resize:vertical;
}

[type="submit"] {
  width: 100%;
  background:var(--accent-yellow);
  border-radius:5px;
  border:0;
  cursor:pointer;
  color:var(--text-dark);
  font-size:24px;
  padding-top:10px;
  padding-bottom:10px;
  transition: all 0.3s;
  margin-top:-4px;
  font-weight:700;
}
[type="submit"]:hover { 
  background:var(--accent-yellow-hover); 
  color: var(--text-dark) 
}
.contacts {
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin: auto;
  width: 60em;
  align-items: center;
  border-radius: 20px;
  padding: 2em;
  margin-top: 5%;
}

.feedback-box {
  width: 30em;
  display: flex;
  justify-content: center;
  flex-direction: row;
  gap:1em;
  height: 20em;
  margin-left: 13em;
  margin-bottom: -10em;
}

h3 {
  font-size: 1.5em;
  margin-top: 1em;
  margin-bottom: -2em;
}
li {
  margin-top: 1em;
}

.references {
  margin-top: 17em;
}
@media(max-width: 600px) {
  form { 
    max-width: 100%; /* Set the form width to 100% of the viewport */
    margin-left: 0; /* Remove margin-left for better alignment */
    color: var(--text-light);
  }

  .feedback-box {
    width: 100%; 
    display: flex;
    justify-content: center;
    flex-direction: column;
    gap: 1em;
    height: auto; 
    margin-left: 0; 
    margin-bottom: 1em;
  }

  .contacts {
    width: 20em;
    border-radius: 0;
    padding: 1em;
    margin-top: 2em;
  }

  .additional-info {
    width: 100%;
  }

  .container2 {
    width: 100%;
  }

  .references {
    margin-top: 1em;
  }
}
</style>
