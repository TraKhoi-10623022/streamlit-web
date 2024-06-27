import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset with appropriate encoding handling
try:
    sp = pd.read_csv(r"./database/Student Attitude and Behavior.csv")
except UnicodeDecodeError:
    sp = pd.read_csv(r"./database/Student Attitude and Behavior.csv", encoding='ISO-8859-1')

# Set page config
apptitle = 'Student Attitude and Behavior'
st.set_page_config(layout="wide", page_title=apptitle, page_icon="👩‍🎓")

# Optionally set a background image for the main app and sidebar
page_bg_img = '''
<style>
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
    color: white;
}
.title {
    font-size: 3em;
    font-weight: bold;
}
.subtitle {
    font-size: 1.5em;
    margin-top: 0.5em;
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
.pulsate {
    animation: pulsate 1s ease-out;
    animation-iteration-count: infinite;
    color: red;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

@keyframes pulsate {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

.description-box {
    border: 2px solid #FF6347;
    padding: 15px;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.8);
    color: #333333;
    font-family: Arial, sans-serif;
    font-size: 1.1em;
    margin-top: 20px;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Gender selection
selected_gender = st.sidebar.radio("Gender 👨/👩", ('All', *sp['Gender'].unique()), key='Gender')

# Filtering data based on selected gender
if selected_gender == 'All':
    filtered_sp = sp
else:
    filtered_sp = sp[sp['Gender'] == selected_gender]

# Bar chart tab content
col1, col2 = st.columns([0.6, 0.4], gap="medium")

# Define options for multiselect and checkbox to select all options in the same column
with col2:
    options = st.multiselect(
        "Choose your department:",
        ["BCA", "B.com Accounting and Finance ", "Commerce", "B.com ISM"],
    )
    selected_all = st.checkbox("Select All Departments")
    if selected_all:
        options = ["BCA", "B.com Accounting and Finance ", "Commerce", "B.com ISM"]

# Check if at least one department is selected
with col1:
    if options:
        # Filter the data based on the selected department
        filtered_sp = filtered_sp[filtered_sp['Department'].isin(options)]
        hobbies_counts = filtered_sp['hobbies'].value_counts()
        hobbies_df = hobbies_counts.reset_index()
        hobbies_df.columns = ['Hobbies', 'Count']
        st.image(image="C:\\Users\\XPS\\Downloads\\Screenshot_2024-06-24_151842-removebg-preview.png", width=400)
    else:
        st.write("")  # Add a space to position the warning message in the middle
        st.write('<p class="pulsate" style="text-align:center;"><span>⚠️</span> Please select at least one department</p>', unsafe_allow_html=True)

st.markdown('<h1 class="title">🎈Different Hobbies Distribution</h1>', unsafe_allow_html=True)


if options:
    # Define custom colors for the pie chart
    custom_colors = {
        "Sports": "#FF6347",      # Tomato
        "Cinema": "#FFD700",      # Gold
        "Video Games": "#8A2BE2", # Blue Violet
        "Reading Books": "#3CB371" # Medium Sea Green
    }
    
    fig1 = px.pie(
        hobbies_df,
        names='Hobbies',
        values='Count',
        color='Hobbies',
        color_discrete_map=custom_colors  # Use custom colors
    )
    fig1.update_traces(marker=dict(line=dict(color='#000000', width=1)))  # Add black border with width 1
    fig1.update_layout(
        font=dict(
            family="Arial, monospace",
            size=14,
            color="RebeccaPurple"
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(
            title='Hobbies',  # Title for the legend
            title_font=dict(size=16, color='#31333F'),  # Font size and color for the legend title
            font=dict(size=14, color='#31333F'),  # Font size and color for legend labels
            bgcolor='rgba(255, 255, 255, 0.5)',  # Background color of the legend
            bordercolor="RebeccaPurple",  # Border color of the legend
            borderwidth=2,  # Border width of the legend
            itemclick="toggleothers",  # Allow toggling of other legend items on click
            itemdoubleclick="toggle",  # Allow toggling of current legend item on double click
            itemsizing="constant"
        )
    )
    st.plotly_chart(fig1)
    
    st.write("---")


    st.markdown(
    '''
    <p>📕The pie chart titled <strong>"Distribution of Different Hobbies"</strong> offers a captivating visual illustration of the popularity of different hobbies among students. This informative graphic illustrates the wide range of interests among students, showing how some are more drawn to sports than others to movies, video games, or reading book. In particular, the disparities in their majors and gender have a big impact on their interests.</p>
    <ul>
        <li>By analyzing this distribution, educators and activity coordinators can better understand students' preferences, allowing them to tailor extracurricular programs that align with these interests.</li>
        <li>Such data-driven insights are invaluable for fostering a supportive and enriching educational environment.</li>
    </ul>
    ''',
    unsafe_allow_html=True
)
