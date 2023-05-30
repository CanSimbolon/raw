import streamlit as st
import pandas as pd

def authenticate(username, password):
    # Add your authentication logic here
    # You can validate the credentials against a database or any other method

    # For simplicity, let's use a hardcoded username and password
    valid_username = "admin"
    valid_password = "password"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            show_csv_page()  # Redirect to CSV viewing page after successful login
        else:
            st.error("Invalid username or password")

def show_csv_page():
    st.title("CSV Viewer")

    # Add your logic to read the CSV file here
    # For demonstration purposes, let's assume the CSV file is named "data.csv"
    try:
        df = pd.read_csv("https://raw.githubusercontent.com/CanSimbolon/raw/main/csv1.csv")
        st.write(df)  # Display the DataFrame

        csv_content = df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv_content, file_name="data.csv", mime="text/csv")

    except FileNotFoundError:
            st.error("CSV file not found.")

if __name__ == "__main__":
    main()
