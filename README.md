# Smart-Strong-Password-Checker
A simple and interactive Streamlit-based Python application that evaluates password strength based on multiple security rules and provides clear feedback and suggestions to user.

Features

Takes Username, Date of Birth, and Password as input

Checks password strength using:

Minimum length
Uppercase letters
Lowercase letters
Digits
Special characters

Penalizes passwords that contain:

User’s name
Date of birth (year)

Displays:

Password strength (Weak / Medium / Strong)
Numerical score
Suggestions for improvement

Tech Stack

Python
Streamlit

How to Run the Project
1️⃣ Install dependencies
pip install streamlit

2️⃣ Run the application
streamlit run app.py

Score Range	Strength
< 2	Weak
2–4	Medium
≥ 5	Strong




