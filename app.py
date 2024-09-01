import streamlit as st
import pandas as pd

# Define the extended resources DataFrame with more sites, categories, tags, and URLs
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

# Sample function to simulate content-based recommendations
def get_content_based_recommendations(resource_name):
    # Placeholder function: you'd compute similarity scores in a real implementation
    similar_resources = resources[resources['name'] != resource_name]
    return similar_resources

# Sample function to simulate collaborative filtering recommendations
def get_collaborative_recommendations(user_id):
    # Placeholder function: you'd use user-based collaborative filtering in a real implementation
    return resources.sample(3)

# Sample function to simulate hybrid recommendations
def get_hybrid_recommendations(user_id, resource_name):
    # Placeholder function: you'd combine content-based and collaborative filtering in a real implementation
    return resources.sample(3)

# Sample function to simulate machine learning recommendations
def get_ml_recommendations(user_id):
    # Placeholder function: you'd use a trained ML model in a real implementation
    return resources.sample(3)

# Streamlit application code

# Title
st.title("Educational Resource Recommender System")

# Sidebar for user input
st.sidebar.header("User Preferences")

# User ID input
user_id = st.sidebar.number_input("Enter User ID", min_value=1, value=1, step=1)

# Educational Level selection
education_level = st.sidebar.selectbox("Select Education Level", ['K-12', 'Higher Education', 'Skill Development'])

# Subject Tags selection
subject_tags = st.sidebar.multiselect(
    "Select Preferred Subjects",
    ['physics', 'computer science', 'math', 'chemistry', 'biology', 'finance', 'economics', 'language', 'technology', 'coding', 'problem-solving', 'machine learning', 'AI', 'web development']
)

# Preferred Category
category = st.sidebar.multiselect("Select Preferred Categories", resources['category'].unique())

# Recommendation Method
rec_method = st.sidebar.selectbox("Select Recommendation Method", ['Content-Based', 'Collaborative', 'Hybrid', 'Machine Learning'])

# Search bar
search_term = st.sidebar.text_input("Search Resources", "")

# Button to generate recommendations
if st.sidebar.button("Get Recommendations"):
    # Filter resources by the selected education level, category, subject tags, and search term
    filtered_resources = resources[
        (resources['education_level'] == education_level) & 
        (resources['category'].isin(category)) & 
        (resources['tags'].apply(lambda x: any(tag in x for tag in subject_tags))) &
        (resources['name'].str.contains(search_term, case=False) | resources['description'].str.contains(search_term, case=False))
    ]
    
    if filtered_resources.empty:
        st.warning("No exact resources found for the selected filters.")
        st.info("Showing resources for the selected education level regardless of subjects.")
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
        
        # Display recommendations as clickable links
        st.subheader("Recommended Resources:")
        for index, row in recs.iterrows():
            st.markdown(f"### [{row['name']}]({row['url']})")
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Description:** {row['description']}")
            st.markdown("---")
    else:
        st.error("No resources found even after relaxing the filters.")

# Display all resources if no filter is applied
if not st.sidebar.button("Get Recommendations"):
    st.subheader("All Available Resources:")
    for index, row in resources.iterrows():
        st.markdown(f"### [{row['name']}]({row['url']})")
        st.write(f"**Category:** {row['category']}")
        st.write(f"**Description:** {row['description']}")
        st.markdown("---")
