import tkinter as tk
from tkinter import messagebox
import re


def check_password_strength(password):
    score = 0
    suggestions = []

    # Length checker
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length (12+ characters recommended)")

    # Uppercase and lowercase checker
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase and lowercase characters")

    # Number checker
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add at least one number")

    # Special character checker
    if re.search(r'[!@#$%^&*()_+=-{};:"<>,.?/]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Common passwords
    common_passwords = ["123456", "password", "12345678", "qwerty"]
    if password in common_passwords:
        suggestions.append("Avoid using common passwords.")
        score -= 1

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# GUI Implementation
def evaluate_password():
    password = password_entry.get()
    if not password.strip():
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, suggestions = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")
    suggestions_text.delete("1.0", tk.END)
    if suggestions:
        suggestions_text.insert(tk.END, "\n".join(suggestions))
    else:
        suggestions_text.insert(tk.END, "Your password looks strong!")


# Create GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

# Input field
tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check Password", command=evaluate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Suggestions box
tk.Label(root, text="Suggestions:", font=("Arial", 12)).pack(pady=5)
suggestions_text = tk.Text(root, height=5, width=45, wrap=tk.WORD, font=("Arial", 10))
suggestions_text.pack(pady=5)

# Run the application
root.mainloop()
