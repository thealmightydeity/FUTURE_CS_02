// Function to analyze password strength
function analyzePassword() {
    const password = document.getElementById("password").value; // Get password input
    let strength = 0;
    const feedback = [];

    // Check password rules
    if (password.length >= 8) {
        strength++;
    } else {
        feedback.push("Password should be at least 8 characters long.");
    }

    if (/[A-Z]/.test(password)) {
        strength++;
    } else {
        feedback.push("Include at least one uppercase letter.");
    }

    if (/[a-z]/.test(password)) {
        strength++;
    } else {
        feedback.push("Include at least one lowercase letter.");
    }

    if (/\d/.test(password)) {
        strength++;
    } else {
        feedback.push("Include at least one number.");
    }

    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
        strength++;
    } else {
        feedback.push("Include at least one special character.");
    }

    const commonPasswords = ["123456", "password", "qwerty", "abc123"];
    if (commonPasswords.includes(password.toLowerCase())) {
        feedback.push("Avoid using common passwords.");
    }

    // Display results
    const result = document.getElementById("result");
    const advice = document.getElementById("advice");

    if (strength === 5) {
        result.textContent = "Strong password!";
        result.style.color = "green";
    } else if (strength >= 3) {
        result.textContent = "Moderate password. You can improve it.";
        result.style.color = "orange";
    } else {
        result.textContent = "Weak password. Consider strengthening it.";
        result.style.color = "red";
    }

    advice.innerHTML = feedback.map(item => `<li>${item}</li>`).join(""); // Display feedback
}

// Attach the function to the button
document.getElementById("analyze-btn").addEventListener("click", analyzePassword);
