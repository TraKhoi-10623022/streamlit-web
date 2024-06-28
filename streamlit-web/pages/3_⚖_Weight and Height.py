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
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Gender selection
selected_gender = st.sidebar.radio("Gender 👨/👩", ('All', *sp['Gender'].unique()), key='Gender')

# Filtering data based on selected gender
if selected_gender == 'All':
    filtered_sp = sp
else:
    filtered_sp = sp[sp['Gender'] == selected_gender]
    
st.markdown('<h1 class="title">🎈Weight and Height Distribution</h1>', unsafe_allow_html=True)

    # Stress Level selection
stress_levels = ["All", "fabulous", "Good", "Bad", "Awful"]
selected_stress_level = st.sidebar.radio("Stress Level:", stress_levels)

col1, col2 = st.columns([0.6, 0.4], gap="medium")
with col1:
    st.image(image=r"./pics/Screenshot_2024-06-25_120959-removebg-preview.png", width=450)

with col2: 
    st.markdown(
    '''
    <div style="border: 2px solid #ff4b4b; padding: 10px; border-radius: 20px;">
    <p>🌐Stress increases cortisol levels, leading to higher appetite and fat storage, which can cause weight gain. Emotional eating under stress often results in consuming calorie-dense foods, contributing further to weight gain. In children and adolescents, chronic stress can inhibit growth hormone production, potentially stunting height development.</p>
    </div>
    ''',
    unsafe_allow_html=True
)
# Filtering data based on the selected stress level
if selected_stress_level != "All":
    filtered_sp = filtered_sp[filtered_sp['Stress Level '] == selected_stress_level]

# Filter data based on the selected height, weight ranges, and gender
filtered_sp_height_weight = filtered_sp.copy()

# Height and Weight range sliders
height_range = st.slider(
    'Select Height Range (CM):',
    min_value=int(sp['Height(CM)'].min()),
    max_value=int(sp['Height(CM)'].max()),
    value=(int(sp['Height(CM)'].min()), int(sp['Height(CM)'].max()))
)
weight_range = st.slider(
    'Select Weight Range (KG):',
    min_value=int(sp['Weight(KG)'].min()),
    max_value=int(sp['Weight(KG)'].max()),
    value=(int(sp['Weight(KG)'].min()), int(sp['Weight(KG)'].max()))
)

# Filter data based on the selected height, weight ranges, and gender
filtered_sp_height_weight = filtered_sp[(filtered_sp['Height(CM)'] >= height_range[0]) & 
                                        (filtered_sp['Height(CM)'] <= height_range[1]) &
                                        (filtered_sp['Weight(KG)'] >= weight_range[0]) & 
                                        (filtered_sp['Weight(KG)'] <= weight_range[1])]


# Create scatter plot
fig4 = px.scatter(filtered_sp_height_weight, x='Height(CM)', y='Weight(KG)', 
                title='Scatter Plot of Weight vs Height', 
                labels={'Height(CM)': 'Height (CM)', 'Weight(KG)': 'Weight (KG)'}, 
                color='Gender',
                color_discrete_map={'Male': 'green', 'Female': 'lightcoral'})  # Change colors as per your preference

fig4.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    
    xaxis_title='Height (CM)', 
    yaxis_title='Weight (KG)',
    
    legend=dict(
        title_font=dict(size=16, color='#31333F'),  # Font size and color for the legend title
        font=dict(size=12, color='#31333F'),
        bgcolor='rgba(255, 255, 255, 0.5)',  # Background color of the legend
        bordercolor="RebeccaPurple",  # Border color of the legend
        borderwidth=2,  # Border width of the legend
        itemclick="toggleothers",  # Allow toggling of other legend items on click
        itemdoubleclick="toggle",  # Allow toggling of current legend item on double click
        itemsizing="constant",
        ), # Legend color
    
    xaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F')), # Set grid color, tick color, and width for x-axis
    yaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F'), gridcolor='white', gridwidth=2), # Set grid color, tick color, and width for y-axis    
)

st.plotly_chart(fig4)

st.write("---")

st.markdown(
    '''
    <p>📗The <strong>"Scatter Plot of Weight vs Height"</strong> provides a clear visualization of the relationship between students' heights and weights. This chart offers insights into how these two physical attributes vary across the student population, and how they may be influenced by gender and the level of stress experienced.</p>
    <ul>
        <li>Each point on the scatter plot represents an individual student's height and weight, color-coded by gender, making it easy to distinguish between male and female students. In addition, the points on the chart also depend on the student's choice of stress level.</li>
        <li>We can identify trends and patterns, such as whether a particular height and weight combination is more common in students of a certain gender or at a particular stress level.</li>
        <li>Wellness and health care programs can benefit greatly from this data, which can assist educators and physicians to comprehend the physical features of the student population and adjust their programs accordingly.</li>
    </ul>
    <p>Overall, the scatter plot is an effective instrument for looking at and understanding the height and weight distribution of adolescents, offering a foundation for further investigations and comprehension of their physical well-being.</p>
    ''',
    unsafe_allow_html=True
)

st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
