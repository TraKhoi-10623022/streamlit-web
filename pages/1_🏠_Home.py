import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# Load the dataset with appropriate encoding handling
try:
    sp = pd.read_csv('C:/Student Attitude and Behavior.csv')
except UnicodeDecodeError:
    sp = pd.read_csv('C:/Student Attitude and Behavior.csv', encoding='ISO-8859-1')

# Set page config
apptitle = 'Student Attitude and Behavior'
st.set_page_config(layout="wide", page_title=apptitle, page_icon=":👩‍🎓:")

page_bg_img = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
.stApp {
    background-image: url("https://images.unsplash.com/photo-1547623641-d2c56c03e2a7?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-attachment: fixed;
}
[data-testid="stSidebar"] {
    background-image: url("https://images.unsplash.com/photo-1508796079212-a4b83cbf734d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
.centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: black;
}
.title {
    font-size: 3em;
    font-weight: bold;
    font-family: 'Roboto', sans-serif;
    color: #2c3e50;
}
.subtitle {
    font-size: 1.5em;
    margin-top: 0.5em;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

with st.sidebar:
    st.write("Date: ", datetime.date(2024, 6, 30))
    
st.subheader('**🔎 Group 6 Business IT 2**') 
st.markdown('<h1 class="title">Student Attitude and Behavior</h1>', unsafe_allow_html=True)
st.markdown("")
st.markdown("")


st.markdown("""
    <style>
    .sidebar .sidebar-content h2 {
        color: "white";
    }
    .sidebar .sidebar-content .stText {
        color: "white";
    }
    .stTitle:hover {
        font-size: 3.5em;
        transition: font-size 0.4s ease;
    }
    .stTitle {
        color: #000;
    }
    .stMarkdown p {
        font-size: 1.2em; /* Adjust the size as needed */
        font-weight: 400;
        color: #000;
    }
    .stMarkdown a {
        color: #000;
    }
    .footer {
        text-align: center;
        padding: 10px;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #34495e;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)



col1, col2 = st.columns([0.5, 0.5], gap="medium")
with col1:
    st.write('**👥 Group information:**')

    st.write('Nguyen Thien Van Khanh - 10623017👩🏻')
    st.write('Nguyenn Thi Tra Khoi - 10623022)👩🏻')
    st.image(image="C:\\Users\\XPS\\Downloads\\47618cf8f33a2bfbac2fa643111d5ef8-removebg-preview.png", width=350)

with col2:
    st.image(image="C:\\Users\\XPS\\Downloads\\e923c7d1320f904bd720821ed25e774d-removebg-preview.png", width=400)
    
st.subheader("🗒Introduction")

with st.container():
    st.write("👋Welcome to the \"Student Attitude and Behavior\" dataset, an insightful collection that delves into various aspects of student life. We will captures a comprehensive range of attributes including academic performance, personal behaviors, and career aspirations. By exploring this dataset, hopefully you can gain valuable perspectives on the holistic development, attitudes, and behaviors of students, paving the way for more informed decisions and strategies in the educational landscape.")

with st.container():
    st.write("---")

    left_column, right_column = st.columns([3, 1])  # Adjust the ratio here
    st.markdown('<a href="https://www.kaggle.com/datasets/susanta21/student-attitude-and-behavior" target="_blank">Where did we find dataset? 💯</a>', unsafe_allow_html=True)
    
    
# Toggle switch to show/hide DataFrame
    if st.toggle("Show Data Frame"):
        st.dataframe(data=sp[['Certification Course', 'Gender', 'Department', 'Height(CM)', 'Weight(KG)', '10th Mark', '12th Mark', 'college mark', 'hobbies', 'Daily studying time', 'prefer to study in', 'salary expectation', 'Do you like your degree?', 'willingness to pursue a career based on their degree  ', 'social medai & video', 'Travelling Time ']], width=1500, use_container_width=True) 

col1, col2 = st.columns([0.5, 0.5], gap="medium")
with col1: 
# List of variables and their functions
    st.subheader("💡Variables")
    st.markdown("""
    <ul>
        <li><strong style="color: #1e8449;">Certification Course:</strong> Indicates if the student is enrolled in a certification course.</li>
        <li><strong style="color: #1e8449;">Gender:</strong> Gender of the student.</li>
        <li><strong style="color: #1e8449;">Department:</strong> Academic department of the student.</li>
        <li><strong style="color: #1e8449;">Height(CM):</strong> Height of the student in centimeters.</li>
        <li><strong style="color: #1e8449;">Weight(KG):</strong> Weight of the student in kilograms.</li>
        <li><strong style="color: #1e8449;">10th Mark:</strong> Marks obtained in the 10th grade.</li>
        <li><strong style="color: #1e8449;">12th Mark:</strong> Marks obtained in the 12th grade.</li>
        <li><strong style="color: #1e8449;">College Mark:</strong> Marks obtained in college.</li>
        <li><strong style="color: #1e8449;">Hobbies:</strong> Student's hobbies.</li>
        <li><strong style="color: #1e8449;">Daily studying time:</strong> Time spent daily on studying.</li>
        <li><strong style="color: #1e8449;">Prefer to study in:</strong> Preferred study environment.</li>
        <li><strong style="color: #1e8449;">Salary expectation:</strong> Expectation regarding future salary.</li>
        <li><strong style="color: #1e8449;">Do you like your degree?:</strong> Student's satisfaction with their degree program.</li>
        <li><strong style="color: #1e8449;">Willingness to pursue a career based on their degree:</strong> Intentions regarding career alignment with degree.</li>
        <li><strong style="color: #1e8449;">Social media & video:</strong> Engagement with social media and video platforms.</li>
        <li><strong style="color: #1e8449;">Travelling Time:</strong> Time spent commuting to college.</li>
    </ul>
""", unsafe_allow_html=True)
    
with col2:
    st.image(image="C:\\Users\\XPS\\Downloads\\b13afc0e9a58d4d6a442a06cec85c07e-removebg-preview.png", width=400)


    st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
