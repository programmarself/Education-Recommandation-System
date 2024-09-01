import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API key and Search Engine ID from environment variables
API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

def google_search(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get('items', [])
        return results
    else:
        st.error("Error in fetching search results.")
        return []

# Streamlit application code
st.title("Educational Resource Recommender System")

# Sidebar for user input
st.sidebar.header("User Preferences")

# Search bar
search_term = st.sidebar.text_input("Search Topics", "")

# Button to initiate search
search_button = st.sidebar.button("Search")

if search_button and search_term:
    st.subheader("Search Results:")
    results = google_search(search_term)
    
    if results:
        for result in results:
            st.markdown(f"### [{result['title']}]({result['link']})")
            st.write(f"**Snippet:** {result['snippet']}")
            st.write(f"**Link:** {result['link']}")
            st.markdown("---")
    else:
        st.warning("No search results found.")
