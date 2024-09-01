import streamlit as st

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
    if rec_method == 'Content-Based':
        # For simplicity, using the first resource in selected category and level
        sample_resource = resources[(resources['education_level'] == education_level) & (resources['category'].isin(category))].iloc[0]['name']
        recs = get_content_based_recommendations(sample_resource)
    elif rec_method == 'Collaborative':
        recs = get_collaborative_recommendations(user_id)
    elif rec_method == 'Hybrid':
        sample_resource = resources[(resources['education_level'] == education_level) & (resources['category'].isin(category))].iloc[0]['name']
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
