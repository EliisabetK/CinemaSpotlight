export default {
  user: { authenticated: false },

  // Function to authenticate the user
  authenticate: async function () {
    try {
      const response = await fetch("http://localhost:3000/auth/authenticate", {
        credentials: 'include', // Include credentials for cookies
      });

      const data = await response.json();
      this.user.authenticated = data.authenticated;

      return this.user.authenticated;
    } catch (error) {
      console.log(error);
      console.log("Error during authentication");
      return false;
    }
  },

  login: async function (credentials) {
    try {
      const response = await fetch("http://localhost:3000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: 'include',
        body: JSON.stringify(credentials),
      });

      const data = await response.json();
      this.user.authenticated = data.authenticated;

      return this.user.authenticated;
    } catch (error) {
      console.log(error);
      console.log("Error during login");
      return false;
    }
  },

  // Function to handle user signup
  signup: async function (credentials) {
    try {
      const response = await fetch("http://localhost:3000/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: 'include',
        body: JSON.stringify(credentials),
      });

      const data = await response.json();
      this.user.authenticated = data.authenticated;

      return this.user.authenticated;
    } catch (error) {
      console.log(error);
      console.log("Error during signup");
      return false;
    }
  },
};
