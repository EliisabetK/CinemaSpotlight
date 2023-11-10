<template>
<body>
    <div class="box">
        <div>
            <h2>Welcome to PostIt</h2>
            <a href="#">Create an account</a>
            <p>or</p>
            <p>Please log in</p>
            <form for="login" action="index.html">
                <div class="input">
                    <label for="email">
                        <input type="email" placeholder="Email" required>
                    </label>
                </div>
                <br>
                <div class="input">
                    <label for="password">
                        <input type="password" placeholder="Password" required>
                    </label>
                </div>
                <br>
                <button type="submit" value="Log in">Log in</button>
            </form>
            <a href="#">Forget password</a>
        </div>
    </div>
</body>
</template>

<script>
export default {
  name: 'SignupView'
};
</script>

<style scoped>
.box{
    display: flex;
    align-items: center;
    justify-content: center;
}
.box > div{
    width: 20em;
    height: 24em;
    background-color: rgb(224, 224, 224);
    border-radius: 10px;
    text-align: center;
    margin: 10em auto;
}
.box a{
    color: rgb(89, 80, 255);
    text-decoration: none;
}
label input{
    outline: none;
    border: none;
    padding: 0.5em 0em;
    width: 32%;
    margin: -0.2em;
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

.box a:hover{
    color: rgb(42, 38, 125);
}
</style>