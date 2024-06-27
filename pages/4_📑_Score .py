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

st.markdown('<h1 class="title">🎈Score Statistics </h1>', unsafe_allow_html=True)

# Selectbox for choosing mark type
col1, col2 = st.columns([0.7, 0.3], gap="medium") 
with col1:
    mark_options = ["10th Mark", "12th Mark", "college mark"]
    selected_mark = st.selectbox("Types of mark:", options=mark_options)
    st.image(image="C:\\Users\\XPS\\Downloads\\2e935d8c1322f3567bf6452b53b54634-removebg-preview (1).png", width=400)

# Image insertted in column 1
with col2:
    st.image(image="C:\\Users\\XPS\\Downloads\\Screenshot_2024-06-25_122902-removebg-preview.png", width=250)

    selected_daily = st.radio("Daily studying time", ('All', *sp['Daily studying time'].unique()), key='Daily studying time')
    if selected_daily == 'All':
        filtered_daily = sp
    else:
        filtered_daily = sp[sp['Daily studying time'] == selected_daily]
    if selected_gender == 'All' and selected_daily == 'All':
        filtered_data = sp
    elif selected_gender == 'All':
        filtered_data = sp[sp['Daily studying time'] == selected_daily]
    elif selected_daily == 'All':
        filtered_data = sp[sp['Gender'] == selected_gender]
    else:
        filtered_data = sp[(sp['Gender'] == selected_gender) & (sp['Daily studying time'] == selected_daily)]

# Add 2 columns for plotting
col1, col2 = st.columns([0.55, 0.45])  # Adjust the ratio here

with col1:
    # Create histogram chart with marks
    fig2 = px.histogram(filtered_data, x=selected_mark, nbins=10, title=f'Distribution of {selected_mark}', labels={selected_mark: selected_mark, 'count': 'Frequency'})
    fig2.update_layout(xaxis_title=selected_mark, yaxis_title='Frequency', bargap=0.1)
    fig2.update_traces(marker_color='#00CC99', marker_line_color='black', marker_line_width=1.5, opacity=0.7)  # Adjust histogram colors and appearance
    fig2.update_layout(
        font=dict(family="Arial", size=12),
        
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        
        xaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F')),
        yaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F'), gridcolor='white', gridwidth=2), # Set grid color and width for y-axis    
    )
    st.plotly_chart(fig2)
        
    st.write("---")

    st.markdown(
        '''
        <p>📘The histogram chart titled <strong>"Distribution of Marks"</strong> provides a visual representation of the frequency distribution of students' scores. This chart allows us to understand how marks are spread across the student population for categories (10th Mark, 12th Mark, or college mark).</p>
        <ul>
            <li>The x-axis represents the range of marks and the y-axis shows the frequency or the number of students.</li>
            <li>The histogram helps in identifying patterns, such as whether marks are concentrated in a particular range or spread out across the spectrum.</li>
            <li>Supervisors can use this information to evaluate students' overall performance and highlight areas that might require further attention.</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )
    st.image(image="C:\\Users\\XPS\\Downloads\\440217f82012557521491a7c81683697-removebg-preview.png", width=450)

with col2:
    # Calculate average mark based on 10th and 12th marks
    filtered_data['Average Mark'] = (filtered_data['10th Mark'] + filtered_data['12th Mark'] + filtered_data['college mark']) / 3

    # Create violin chart with average mark
    fig3 = px.box(filtered_data, y="Average Mark", points="all", title="Violin Plot of Average Marks", hover_data=["10th Mark", "12th Mark"])
    fig3.update_traces(boxpoints='all', jitter=0.3, marker=dict(color='#6699FF', size=4.5), line=dict(color='#FFCC33', width=2))
    fig3.update_layout(
        font=dict(family="Arial", size=12),
        
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        
        xaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F')), # Set grid color, tick color, and width for x-axis
        yaxis=dict(tickfont=dict(color='#31333F'), title_font=dict(color='#31333F'), gridcolor='white', gridwidth=2), # Set grid color, tick color, and width for y-axis    
)
    st.plotly_chart(fig3)
        
    st.write("---")

    st.markdown(
        '''
        <p>📙The <strong>"Violin Plot of Average Marks"</strong> provides a visual representation of the distribution of students' average marks, calculated based on their 10th, 12th, and college marks. This chart combines aspects of a box plot with a density plot to offer a detailed view of the data distribution.</p>
        <ul>
            <li>The average marks are represented by the y-axis, and the density of the points across different y-values is indicated by the dimension of the plot at those values.</li>
            <li>The plot shows the central tendency and variability of the average marks, helping to identify the range within which most students' average marks lie.</li>
            <li>Professors can use this data to more accurately evaluate pupils' overall academic performance and notice any notable deviations or outliers.</li>
        </ul>
        ''',
        unsafe_allow_html=True
    )
