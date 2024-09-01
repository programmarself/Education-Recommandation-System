import streamlit as st
import pandas as pd

# Define the extended resources DataFrame with detailed mappings
resources = pd.DataFrame({
    'resource_id': list(range(1, 13)),
    'name': [
        'Khan Academy', 'Coursera', 'edX', 'Duolingo', 'TED-Ed', 'Finance Academy',
        'Codeacademy', 'LinkedIn Learning', 'Udacity', 'MIT OpenCourseWare', 'FutureLearn', 'Brilliant'
    ],
    'category': [
        'Educational Platform', 'Educational Platform', 'Educational Platform', 'Educational App', 'Educational Video', 'Educational Platform',
        'Coding Platform', 'Educational Platform', 'Coding Platform', 'University Courses', 'Educational Platform', 'Problem-Solving Platform'
    ],
    'description': [
        'Free online courses for K-12', 'Online courses from universities', 'University-level courses', 'Language learning app', 'Educational videos on various topics', 'Finance and investment courses',
        'Learn to code interactively', 'Courses from experts in various fields', 'Nanodegree programs in tech', 'Free lecture notes, exams, and videos', 'Courses from top universities and organizations', 'Interactive learning for STEM subjects'
    ],
    'tags': [
        'math, science, physics', 'computer science, data science', 'engineering, humanities', 'language, vocabulary', 'technology, innovation', 'finance, economics',
        'coding, programming, web development', 'business, design, technology', 'machine learning, AI, data science', 'engineering, computer science, physics', 'online learning, universities', 'math, logic, problem-solving'
    ],
    'education_level': [
        'K-12', 'Higher Education', 'Higher Education', 'Skill Development', 'K-12', 'Higher Education',
        'Skill Development', 'Higher Education', 'Higher Education', 'Higher Education', 'Higher Education', 'Skill Development'
    ],
    'url': [
        'https://www.khanacademy.org', 'https://www.coursera.org', 'https://www.edx.org', 'https://www.duolingo.com', 'https://ed.ted.com', 'https://www.financeacademy.com',
        'https://www.codecademy.com', 'https://www.linkedin.com/learning', 'https://www.udacity.com', 'https://ocw.mit.edu', 'https://www.futurelearn.com', 'https://www.brilliant.org'
    ]
})

# Define a mapping from topics to resources
topic_to_resources = {
    'types of speed': ['Khan Academy', 'MIT OpenCourseWare'],
    'types of energy': ['Khan Academy', 'Coursera'],
    'quantum mechanics': ['MIT OpenCourseWare', 'Coursera'],
    'computer science': ['Coursera', 'LinkedIn Learning', 'Codecademy'],
    'machine learning': ['Coursera', 'Udacity'],
    'coding': ['Codecademy', 'LinkedIn Learning'],
    'finance': ['Finance Academy', 'Coursera']
}

# Define recommendation functions
def get_content_based_recommendations(resource_name):
    if resource_name not in resources['name'].values:
        return pd.DataFrame()  # Return an empty DataFrame if the resource is not found
    return resources[resources['name'] != resource_name]

def get_collaborative_recommendations(user_id):
    return resources.sample(3)

def get_hybrid_recommendations(user_id, resource_name):
    return resources.sample(3)

def get_ml_recommendations(user_id):
    return resources.sample(3)

# Streamlit application code

# Page configuration
st.set_page_config(page_title="Educational Resource Recommender System", layout="wide")

# Title with background color
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #fff;
        font-size: 48px;
        font-family: 'Arial', sans-serif;
        background: linear-gradient(45deg, #6a1b9a, #ff6f00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px;
        border-radius: 10px;
    }
    .background {
        background-color: #e3f2fd; /* Light blue background */
        padding: 20px;
        border-radius: 15px;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #e3f2fd, #bbdefb);
        color: #333;
        font-size: 16px;
        border-radius: 15px;
        padding: 20px;
    }
    .sidebar .sidebar-content input, .sidebar .sidebar-content select, .sidebar .sidebar-content button {
        margin-bottom: 10px;
        border-radius: 10px;
        border: 1px solid #ddd;
        padding: 10px;
        font-size: 16px;
    }
    .sidebar .sidebar-content button {
        background-color: #007bff;
        color: #fff;
        border: none;
        padding: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .sidebar .sidebar-content button:hover {
        background-color: #0056b3;
    }
    .resource-card {
        border: 1px solid #ddd;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .resource-card:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
    }
    .resource-title {
        color: #007bff;
        text-decoration: none;
    }
    .resource-title:hover {
        text-decoration: underline;
    }
    .footer {
        text-align: center;
        padding: 30px;
        background: #f1f1f1;
        border-top: 1px solid #ddd;
        color: #333;
    }
    .footer a {
        color: #007bff;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="title">Educational Resource Recommender System</div>
    <div class="background">
    """, unsafe_allow_html=True)

# Sidebar widgets
user_id = st.sidebar.number_input("Enter User ID", min_value=1, value=1, step=1)
education_level = st.sidebar.selectbox("Select Education Level", ['K-12', 'Higher Education', 'Skill Development'])
subject_tags = st.sidebar.multiselect(
    "Select Preferred Subjects",
    ['physics', 'computer science', 'math', 'chemistry', 'biology', 'finance', 'economics', 'language', 'technology', 'coding', 'problem-solving', 'machine learning', 'AI', 'web development']
)
category = st.sidebar.multiselect("Select Preferred Categories", resources['category'].unique())
rec_method = st.sidebar.selectbox("Select Recommendation Method", ['Content-Based', 'Collaborative', 'Hybrid', 'Machine Learning'])
get_recommendations = st.sidebar.button("Get Recommendations")

# Logic to display recommendations or all resources
if get_recommendations:
    filtered_resources = resources[
        (resources['education_level'] == education_level) & 
        (resources['category'].isin(category)) & 
        (resources['tags'].apply(lambda x: any(tag in x for tag in subject_tags)))
    ]
    
    if filtered_resources.empty:
        filtered_resources = resources[resources['education_level'] == education_level]
    
    if not filtered_resources.empty:
        if rec_method == 'Content-Based':
            sample_resource = filtered_resources.iloc[0]['name']
            recs = get_content_based_recommendations(sample_resource)
        elif rec_method == 'Collaborative':
            recs = get_collaborative_recommendations(user_id)
        elif rec_method == 'Hybrid':
            sample_resource = filtered_resources.iloc[0]['name']
            recs = get_hybrid_recommendations(user_id, sample_resource)
        else:
            recs = get_ml_recommendations(user_id)
        
        # Display recommendations in a card-like format
        st.subheader("Recommended Resources:")
        for index, row in recs.iterrows():
            st.markdown(
                f"""
                <div class="resource-card">
                    <a href="{row['url']}" class="resource-title" target="_blank">
                        <h3 style="margin: 0;">{row['name']}</h3>
                        <p><strong>Category:</strong> {row['category']}</p>
                        <p><strong>Description:</strong> {row['description']}</p>
                    </a>
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.subheader("All Available Resources:")
        for index, row in resources.iterrows():
            st.markdown(
                f"""
                <div class="resource-card">
                    <a href="{row['url']}" class="resource-title" target="_blank">
                        <h3 style="margin: 0;">{row['name']}</h3>
                        <p><strong>Category:</strong> {row['category']}</p>
                        <p><strong>Description:</strong> {row['description']}</p>
                    </a>
                </div>
                """, unsafe_allow_html=True
            )

# Footer
st.markdown("""
    </div>
    <div class="footer">
        <p><strong>Developed By:</strong> Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm" target="_blank">https://flowcv.me/ikm</a></p>
        <p><strong>Developed For:</strong> Essential Generative AI Training</p>
        <p><strong>Conducted By:</strong> PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </div>
    """, unsafe_allow_html=True)
