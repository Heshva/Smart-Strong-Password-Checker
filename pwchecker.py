import streamlit as st

st.title("🔐 Smart Password Strength Checker")


st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Times New Roman", Times, serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

name = st.text_input("Enter your name")
dob = st.text_input("Enter your Date of Birth (YYYY-MM-DD)")
password = st.text_input("Enter your password", type="password")

if st.button("Check Password"):

    if name == "" or dob == "" or password == "":
        st.error("Please fill all details")
    else:
        year = dob[:4]
        score = 0
        reasons = []


        if len(password) >= 8:
            score += 1
        else:
            reasons.append("Password length less than 8")

        if any(a.isupper() for a in password):
            score += 1
        else:
            reasons.append("No uppercase letter")

        if any(a.islower() for a in password):
            score += 1
        else:
            reasons.append("No lowercase letter")

        if any(a.isdigit() for a in password):
            score += 1
        else:
            reasons.append("No digit")

        if any(c in "@$#&!%?*;\"',[]{}" for c in password):
            score += 1
        else:
            reasons.append("No special character")

        if year in password:
            score -= 2
            reasons.append("Password contains DOB year")

        if name.lower() in password.lower():
            score -= 2
            reasons.append("Password contains name")


        if score < 2:
            st.error(" Weak Password")
        elif score < 5:
            st.warning("Medium Password")
        else:
            st.success("Strong Password")

        if reasons:
            for r in reasons:
                st.write("- ", r)

