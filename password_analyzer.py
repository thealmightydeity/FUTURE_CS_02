import tkinter as tk
from tkinter import messagebox
import re
import hashlib

def check_password_strength(password):
    """Analyzes the strength of the password and provides feedback."""
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    # Check for common patterns
    common_passwords = ["123456", "password", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords.")

    # Determine password strength
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password. You can improve it.", feedback
    else:
        return "Weak password. Consider strengthening it.", feedback

def hash_password(password):
    """Hashes the password using SHA-256 and returns the hash."""
    return hashlib.sha256(password.encode()).hexdigest()

def analyze_password():
    """Handles the password analysis and display."""
    password = entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return

    # Analyze password strength
    strength, advice = check_password_strength(password)

    # Display results
    result_label.config(text=strength)
    advice_label.config(text="\n".join(advice))

    # Optionally display hashed password
    hashed_password = hash_password(password)
    hash_label.config(text=f"SHA-256 Hash:\n{hashed_password}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("500x400")

# Create and place widgets
tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_password, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

advice_label = tk.Label(root, text="", font=("Arial", 10), fg="red", wraplength=450, justify="left")
advice_label.pack(pady=10)

hash_label = tk.Label(root, text="", font=("Arial", 10), fg="green", wraplength=450, justify="left")
hash_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
