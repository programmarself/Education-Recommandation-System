import streamlit as st
import pandas as pd

# Define the resources DataFrame
resources = pd.DataFrame({
    'resource_id': [1, 2, 3, 4, 5],
    'name': ['Khan Academy', 'Coursera', 'edX', 'Duolingo', 'TED-Ed'],
    'category': ['Educational Platform', 'Educational Platform', 'Educational Platform', 'Educational App', 'Educational Video'],
    'description': ['Free online courses for K-12', 'Online courses from universities', 'University-level courses', 'Language learning app', 'Educational videos on various topics'],
    'tags': ['math, science', 'computer science, data science', 'engineering, humanities', 'language, vocabulary', 'technology, innovation'],
    'education_level': ['K-12', 'Higher Education', 'Higher Education', 'Skill Development', 'K-12']
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

# Preferred Category
category = st.sidebar.multiselect("Select Preferred Categories", resources['category'].unique())

# Recommendation Method
rec_method = st.sidebar.selectbox("Select Recommendation Method", ['Content-Based', 'Collaborative', 'Hybrid', 'Machine Learning'])

# Button to generate recommendations
if st.sidebar.button("Get Recommendations"):
    # Filter resources by the selected education level and category
    filtered_resources = resources[(resources['education_level'] == education_level) & (resources['category'].isin(category))]
    
    if filtered_resources.empty:
        st.warning("No exact resources found for the selected education level and category.")
        st.info("Showing resources for the selected education level regardless of category.")
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
        
        # Display recommendations
        st.subheader("Recommended Resources:")
        for index, row in recs.iterrows():
            st.markdown(f"### {row['name']}")
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Description:** {row['description']}")
            st.markdown("---")
    else:
        st.error("No resources found even after relaxing the filters.")
