import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
apptitle = 'Student Attitude and Behavior'
st.set_page_config(layout="wide", page_title=apptitle, page_icon="👩‍🎓")

# Optionally set a background image for the main app and sidebar
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1519327232521-1ea2c736d34d?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-attachment: fixed;
}
[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0);
    visibility:hidden;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
.centered {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: "black";
}
.title {
    font-size: 3em;
    font-weight: bold;
    color: "black";
}
.subtitle {
    font-size: 1.5em;
    margin-top: 0.5em;
    color: "black";
}
.start-button {
    margin-top: 2em;
    font-size: 1.2em;
    background-color: #ff4b4b;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Define a function to display the cover page
def show_cover_page():
    st.markdown(
        '''
        <div body="centered">
            <div class="title">Welcome to our website </div>
            <div class="subtitle">Explore insights and trends in student attitudes and behaviors.</div>
        </div>
        ''', unsafe_allow_html=True
    )
    if st.page_link("pages/1_🏠_Home.py", label="Get Start"):
        st.session_state.show_cover = False

# Check if the cover page should be displayed or the main content
if 'show_cover' not in st.session_state:
    st.session_state.show_cover = True

if st.session_state.show_cover:
    show_cover_page()
else:
    # Load the dataset with appropriate encoding handling
    try:
        sp = pd.read_csv('C:/Student Attitude and Behavior.csv')
    except UnicodeDecodeError:
        sp = pd.read_csv('C:/Student Attitude and Behavior.csv', encoding='ISO-8859-1')

