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
        suggestions.append("Increase password length (12+ characters recommended).")

    # Uppercase and Lowercase checker
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase and lowercase characters.")

    # Number checker
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character checker
    if re.search(r'[!@#$%^&*()_+=\-{};:"<>,.?/]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Common password check
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

# Example usage
password = input("Enter your password: ")
strength, tips = check_password_strength(password)
print(f"Password Strength: {strength}")
if tips:
    print("Suggestions:")
    for tip in tips:
        print(f"- {tip}")
