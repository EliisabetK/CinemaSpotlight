<template>
<body>
    <div class="box">
        <div>
            <h2>Welcome to PostIt</h2>
            <p>Sign up</p>
            <form class="form" for="login" v-on:submit="Login">
                <div class="text_inputs">
                    <div class="text">
                        <b>Email:</b>
                        <b>Password:</b>
                    </div>
                    <div class="inputs">
                        <label>
                            <input type="email" placeholder="Email" required>
                        </label>
                        <label>
                            <input type="password" v-model="password" placeholder="Password" required>
                        </label>
                    </div>
                </div>
                <br>
                <button type="submit" value="Log in">Sign up</button>
            </form>
            <p class="errors" v-if="errors.length">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-for="error in errors">{{ error }}</li>
                </ul>
            </p>
        </div>
    </div>
</body>
</template>

<script>
export default {
  name: 'SignupView',
  data: () => {
    return {
        errors: [],
        password: '',
    };
  },
  methods:{
    Login: function() {
        this.errors = [];
        var correct = true;
        if(this.password.length < 8 || this.password.length >= 15){
            this.errors.push('Password should contain at least 8 characters and less than 15 characters.')
            correct = false;
        }
        if(!/[A-Z]/.test(this.password)){
            this.errors.push('Password should contain at least one uppercase character.')
            correct = false;
        }
        if(!/[a-z].*[a-z]/.test(this.password)){
            this.errors.push('Password should contain at least two lowercase characters.')
            correct = false;
        }
        if(!/[0-9]/.test(this.password)){
            this.errors.push('Password should contain at least one numeric character.')
            correct = false;
        }
        if(!/[A-Z]/.test(this.password.charAt(0))){
            this.errors.push('Password should start with uppercase character.')
            correct = false;
        }
        if(!/_/.test(this.password)){
            this.errors.push('Password should include "_".')
            correct = false;
        }
        if(correct){
            this.$router.push({ path: '/' });
        }
    },
  }
};
</script>

<style scoped>
.box{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

a{
    color: rgb(89, 80, 255);
    text-decoration: none;
}
.inputs > label > input{
    outline: none;
    border: none;
    padding: 0.5em 0em;
    margin: 0.6em;
}

input::placeholder{
    color: rgb(173, 173, 173);
}

button{
    display: inline-block;
    background-color: rgb(0, 0, 195);
    color: rgb(255, 255, 255);
    border: none;
    text-align: center;
    padding: 0.5em;
    margin: 0.3em;
    margin-bottom: 3em;
}

button:hover{
    background-color: rgb(0, 0, 118);
    color: rgb(159, 159, 159);
}

a:hover{
    color: rgb(42, 38, 125);
}


.box > div{
      width: 22em;
      height: 20em;
      background-color: rgb(224, 224, 224);
      border-radius: 10px;
      text-align: center;
      margin: 8em auto;
      margin-bottom: 0em;
  }

  input::placeholder{
      color: rgb(173, 173, 173);
      padding: 0.2em;
  }

  button{
      display: inline-block;
      font-family: monospace, sans-serif;
      font-size: 14px;
      color: rgb(255, 255, 255);
      border: none;
      text-align: center;
      padding: 0.5em;
      margin: 0.3em;
      margin-bottom: 3em;
      width: 12em;
  }

  .createpost > button {
      background-color: rgb(0, 0, 195);
  }

  .choosefile > button {
      background-color: rgb(103, 103, 103);
  }

  .createpost button:hover{
      background-color: rgb(0, 0, 118);
      color: rgb(159, 159, 159);
  }

  .choosefile button:hover{
      background-color: rgb(92, 92, 92);
      color: rgb(159, 159, 159);
  }

  textarea{
      border: none;
      width: 16em;
      height: 10em;
      resize: none;
  }

  button{
      display: inline-block;
      background-color: rgb(0, 0, 195);
      color: rgb(255, 255, 255);
      text-align: center;
      padding: 0.5em;
      margin: 0.3em;
      margin-bottom: 3em;
  }

  .errors{
    display: flex;
    flex-direction: column;
    font-size: small;
    padding-top: 1.5em;
  }
  .form{
    padding-top: 2em;
  }

  .text_inputs{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .text{
    display: flex;
    flex-direction: column;
  }
  .text > b{
    text-align: right;
    margin: 0.8em;
  }

  .inputs{
    display: flex;
    flex-direction: column;
  }
</style>