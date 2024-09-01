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
    # Simple content-based recommendation (replace with actual logic)
    return resources[resources['name'] != resource_name]

def get_collaborative_recommendations(user_id):
    # Placeholder for collaborative filtering
    return resources.sample(3)

def get_hybrid_recommendations(user_id, resource_name):
    # Placeholder for hybrid filtering
    return resources.sample(3)

def get_ml_recommendations(user_id):
    # Placeholder for machine learning-based recommendations
    return resources.sample(3)

# Streamlit application code

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Educational Resource Recommender System</h1>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f4f4f4;
        color: #333;
        font-size: 16px;
        border-radius: 10px;
        padding: 20px;
    }
    .sidebar .sidebar-content input, .sidebar .sidebar-content select, .sidebar .sidebar-content button {
        margin-bottom: 10px;
    }
    </style>
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
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <h3><a href="{row['url']}" style="text-decoration: none; color: #007bff;">{row['name']}</a></h3>
                    <p><strong>Category:</strong> {row['category']}</p>
                    <p><strong>Description:</strong> {row['description']}</p>
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.subheader("All Available Resources:")
        for index, row in resources.iterrows():
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                    <h3><a href="{row['url']}" style="text-decoration: none; color: #007bff;">{row['name']}</a></h3>
                    <p><strong>Category:</strong> {row['category']}</p>
                    <p><strong>Description:</strong> {row['description']}</p>
                </div>
                """, unsafe_allow_html=True
            )

# Footer
st.markdown(
    """
    <div style="text-align: center; padding: 20px; background-color: #f8f9fa; border-top: 1px solid #ddd;">
        <p style="font-size: 16px; color: #333; margin-bottom: 5px;">Developed By: Irfan Ullah Khan</p>
        <p style="font-size: 16px; color: #007bff; margin-bottom: 5px;"><a href="https://flowcv.me/ikm" target="_blank" style="text-decoration: none; color: #007bff;">https://flowcv.me/ikm</a></p>
        <p style="font-size: 16px; color: #333; margin-bottom: 5px;">Developed For: Essential Generative AI Training</p>
        <p style="font-size: 16px; color: #333;">Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </div>
    """, unsafe_allow_html=True
)
