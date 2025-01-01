import tkinter as tk
from tkinter import messagebox, filedialog
import re
import math
import pyperclip
import random
import string


# Password strength checker
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length checker
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
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
    if re.search(r'[!@#$%^&*()_+=\-{};:"<>,.?/\[\]]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Common passwords
    common_passwords = ["123456", "password", "12345678", "qwerty", "admin"]
    if password.lower() in common_passwords:
        suggestions.append("Avoid using common passwords.")
        score -= 2

    # Check for sequences or repeated characters
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        suggestions.append("Avoid repeated characters.")
        score -= 1
    if re.search(r'(1234|abcd|4321|dcba)', password.lower()):  # Common sequences
        suggestions.append("Avoid common sequences.")
        score -= 1

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# Password entropy calculator
def calculate_entropy(password):
    # Character pool size
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[!@#$%^&*()_+=\-{};:"<>,.?/\[\]]', password):
        pool_size += 32

    # Entropy calculation
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy


# Evaluate password and display results
def evaluate_password():
    password = password_entry.get()
    if not password.strip():
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, suggestions = check_password_strength(password)
    entropy = calculate_entropy(password)
    result_label.config(text=f"Password Strength: {strength} (Entropy: {entropy:.2f} bits)")

    # Add to history
    password_history.append((password, strength, entropy))
    update_history()

    # Color coding
    if strength == "Weak":
        result_label.config(fg="#FF4444")  # Red
    elif strength == "Medium":
        result_label.config(fg="#FFAA00")  # Orange
    else:
        result_label.config(fg="#00C851")  # Green

    suggestions_text.delete("1.0", tk.END)
    if suggestions:
        suggestions_text.insert(tk.END, "\n".join(suggestions))
    else:
        suggestions_text.insert(tk.END, "Your password looks strong!")


# Toggle password visibility
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# Copy suggestions to clipboard
def copy_suggestions():
    suggestions = suggestions_text.get("1.0", tk.END).strip()
    if suggestions:
        pyperclip.copy(suggestions)
        messagebox.showinfo("Copied", "Suggestions copied to clipboard!")


# Generate a random password
def generate_password():
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+=-{};:\"<>,.?/"

    # Combine all pools
    all_chars = lowercase + uppercase + digits + special_chars

    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Toggle dark mode
def toggle_dark_mode():
    if dark_mode_var.get():
        root.config(bg="#2E2E2E")
        for widget in root.winfo_children():
            if widget.winfo_class() in ("Label", "Button", "Checkbutton", "Text"):
                widget.config(bg="#2E2E2E", fg="white")
            elif widget.winfo_class() == "Entry":
                widget.config(bg="#555555", fg="white", insertbackground="white")
            elif widget.winfo_class() == "Frame":
                widget.config(bg="#2E2E2E")
    else:
        root.config(bg="#F5F5F5")
        for widget in root.winfo_children():
            if widget.winfo_class() in ("Label", "Button", "Checkbutton", "Text"):
                widget.config(bg="#F5F5F5", fg="black")
            elif widget.winfo_class() == "Entry":
                widget.config(bg="white", fg="black", insertbackground="black")
            elif widget.winfo_class() == "Frame":
                widget.config(bg="#F5F5F5")


# Update password history
def update_history():
    history_text.delete("1.0", tk.END)
    for idx, (password, strength, entropy) in enumerate(password_history, 1):
        history_text.insert(tk.END, f"{idx}. Password: {password}, Strength: {strength}, Entropy: {entropy:.2f} bits\n")


# Export results to a text file
def export_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(result_label.cget("text") + "\n")
            file.write("Suggestions:\n")
            file.write(suggestions_text.get("1.0", tk.END))
            file.write("\nPassword History:\n")
            file.write(history_text.get("1.0", tk.END))
        messagebox.showinfo("Export Successful", f"Results exported to {file_path}")


# Create GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x600")
root.config(bg="#F5F5F5")

# Modern font
font_style = ("Helvetica", 12)

# Input field
input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter your password:", font=font_style, bg="#F5F5F5").pack(pady=5)
password_entry = tk.Entry(input_frame, show="*", width=30, font=font_style)
password_entry.pack(pady=5)

# Show password checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(input_frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility, font=font_style, bg="#F5F5F5")
show_password_checkbox.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=10)

check_button = tk.Button(button_frame, text="Check Password", command=evaluate_password, font=font_style, bg="#4CAF50", fg="white", padx=10, pady=5)
check_button.grid(row=0, column=0, padx=5)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password, font=font_style, bg="#FF9800", fg="white", padx=10, pady=5)
generate_button.grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#F5F5F5")
result_label.pack(pady=10)

# Suggestions box
suggestions_frame = tk.Frame(root, bg="#F5F5F5")
suggestions_frame.pack(pady=10)

tk.Label(suggestions_frame, text="Suggestions:", font=font_style, bg="#F5F5F5").pack(pady=5)
suggestions_text = tk.Text(suggestions_frame, height=5, width=45, wrap=tk.WORD, font=font_style)
suggestions_text.pack(pady=5)

# Password history box
history_frame = tk.Frame(root, bg="#F5F5F5")
history_frame.pack(pady=10)

tk.Label(history_frame, text="Password History:", font=font_style, bg="#F5F5F5").pack(pady=5)
history_text = tk.Text(history_frame, height=5, width=45, wrap=tk.WORD, font=font_style)
history_text.pack(pady=5)

# Copy suggestions button
copy_button = tk.Button(root, text="Copy Suggestions", command=copy_suggestions, font=font_style, bg="#2196F3", fg="white", padx=10, pady=5)
copy_button.pack(pady=10)

# Export results button
export_button = tk.Button(root, text="Export Results", command=export_results, font=font_style, bg="#9C27B0", fg="white", padx=10, pady=5)
export_button.pack(pady=10)

# Dark mode checkbox
dark_mode_var = tk.BooleanVar()
dark_mode_checkbox = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode, font=font_style, bg="#F5F5F5")
dark_mode_checkbox.pack(pady=10)

# Password history list
password_history = []

# Run the application
root.mainloop()