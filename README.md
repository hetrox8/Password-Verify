# **Password Strength Checker Documentation**

## **Overview**

The **Password Strength Checker** is a Python-based tool designed to evaluate the strength of a given password and provide suggestions for improvement. It checks the following aspects of a password:

- **Length**
- **Uppercase and lowercase characters**
- **Numbers**
- **Special characters**
- **Commonly used passwords**

The password strength is categorized as **"Weak"**, **"Medium"**, or **"Strong"**, and the user is provided with actionable suggestions to improve the password.

---

## **Features**

- **Password Evaluation**: Checks the strength of a password based on multiple criteria.
- **Suggestions for Improvement**: Provides specific feedback to enhance password security.
- **Common Password Check**: Verifies if the password is commonly used and vulnerable to attacks.

---

## **How It Works**

The tool evaluates a password based on the following criteria:

1. **Length**: Passwords shorter than 8 characters are considered weak.
2. **Character Diversity**: Passwords must include a mix of:
   - Uppercase letters (`A-Z`)
   - Lowercase letters (`a-z`)
   - Numbers (`0-9`)
   - Special characters (`!@#$%^&*()`)
3. **Common Passwords**: The tool checks if the password is in a list of commonly used passwords.

Based on these checks, the tool assigns a strength rating and provides suggestions for improvement.

---

## **Installation**

### **Prerequisites**
- Python 3.x installed on your system.

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/hetrox8/password-strength-checker.git
   cd password-strength-checker
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python -m streamlit run app.py
   ```

---

## **Usage**

1. **Run the Script**:
   ```bash
   python password_checker.py
   ```
![Password Strength Checker Example](image.png)
![image](https://github.com/user-attachments/assets/0aeb41cd-1960-4534-a252-09bdb827a205)
![image](https://github.com/user-attachments/assets/366f7617-f45a-4b71-a5a9-7a8fe13cae7a)
2. **Enter Your Password**:
   When prompted, enter the password you want to check.

3. **View Results**:
   The tool will display the password strength and suggestions for improvement.

### **Example**
```plaintext
Enter your password: Suleiman
Password Strength: Weak
Suggestions:
- Add at least one number.
- Add at least one special character.
```

---

## **Code Structure**

The project consists of the following files:

- `password_checker.py`: The main script for evaluating password strength.
- `common_passwords.txt`: A list of commonly used passwords for comparison.
- `README.md`: Project documentation (this file).

---

## **How to Contribute**

Contributions are welcome! Here’s how you can contribute:

1. **Fork the Repository**:
   Click the "Fork" button on the GitHub repository page.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```

3. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**:
   Implement your changes or improvements.

5. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**:
   Go to the original repository and click "New Pull Request".

---

## **Future Improvements**

Here are some ideas for future enhancements:

- **Real-Time Feedback**: Add a GUI or web interface for a more interactive user experience.
- **Password Leak Check**: Integrate with a password leak database (e.g., Have I Been Pwned) to check if the password has been exposed in data breaches.
- **Password Generator**: Add a feature to generate strong, random passwords.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions, feedback, or collaboration, feel free to reach out:

- **Email**: dretrevor8@gmail.com
- **LinkedIn**: [Suleiman Yusuf Gacheru](https://www.linkedin.com/in/yourlinkedin)
- **GitHub**: [hetrox8](https://github.com/hetrox8)

---

## **Acknowledgments**

- Inspired by the need for better password security practices.
- Built with ❤️ using Python.

---

Thanks for using the **Password Strength Checker**! Let’s make the internet a safer place, one strong password at a time. 🚀
