document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get input values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    // Your verification logic (e.g., checking against a hardcoded username and password)
    if (username === "user" && password === "password") {
      // Redirect to landing page upon successful login
      window.location.href = "landingpage.html";
    } else {
      // Display error message for unsuccessful login
      document.getElementById("error-message").innerText = "Invalid username or password.";
    }
  });
  
  