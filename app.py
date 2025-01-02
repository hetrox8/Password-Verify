import streamlit as st
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
    return password


# Streamlit App
def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
    st.title("Password Strength Checker")
    st.write("Check the strength of your password and get suggestions to improve it.")

    # Input field
    password = st.text_input("Enter your password:", type="password")

    # Generate password button
    if st.button("Generate Strong Password"):
        password = generate_password()
        st.text_input("Generated Password:", value=password, type="password")

    # Check password strength
    if password:
        strength, suggestions = check_password_strength(password)
        entropy = calculate_entropy(password)

        # Display results
        st.subheader("Results")
        st.write(f"**Password Strength:** {strength}")
        st.write(f"**Entropy:** {entropy:.2f} bits")

        if suggestions:
            st.subheader("Suggestions")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.success("Your password looks strong!")

    # Footer
    st.markdown("---")
    st.write("Made by Suleiman Yusuf Gacheru")


if __name__ == "__main__":
    main()