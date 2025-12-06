


import streamlit as st
import pickle
import pandas as pd
import requests
from huggingface_hub import hf_hub_download

# ==========================
# OMDb API KEY
# ==========================
OMDB_API_KEY = "eb6579ab"

# ==========================
# HUGGING FACE CONFIG
# ==========================
REPO_ID = "aditi1411963/movie-recommendation"
FILENAME = "similarity.pkl"
REPO_TYPE = "model"

# ==========================
# LOAD DATA (CSV ONLY CHANGE ✅)
# ==========================
@st.cache_data
def load_movies():
    return pd.read_csv("movies.csv")

@st.cache_data
def load_similarity():
    path = hf_hub_download(
        repo_id=REPO_ID,
        repo_type=REPO_TYPE,
        filename=FILENAME
    )
    with open(path, "rb") as f:
        similarity = pickle.load(f)
    return similarity

# ==========================
# OMDb DETAILS
# ==========================
@st.cache_data(show_spinner=False)
def fetch_movie_details(title):
    url = "http://www.omdbapi.com/"
    params = {"apikey": OMDB_API_KEY, "t": title}
    try:
        data = requests.get(url, params=params, timeout=10).json()
        if data.get("Response") == "True":
            return {
                "rating": data.get("imdbRating", "N/A"),
                "votes": data.get("imdbVotes", "N/A"),
                "year": data.get("Year", "N/A"),
                "runtime": data.get("Runtime", "N/A"),
                "genre": data.get("Genre", "N/A"),
                "director": data.get("Director", "N/A"),
                "actors": data.get("Actors", "N/A"),
                "language": data.get("Language", "N/A"),
                "awards": data.get("Awards", "N/A"),
                "plot": data.get("Plot", "N/A")
            }
    except:
        pass
    return None

# ==========================
# RECOMMEND FUNCTION
# ==========================
def recommend(movie, movies, similarity):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]
    return movies.iloc[[i[0] for i in distances]]

# ==========================
# STREAMLIT UI
# ==========================
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.sidebar.title("🎬 Movie Recommender")
st.sidebar.markdown(
    """
    ### 📌 About Project
    This project is a **content-based movie recommendation system** that suggests
    movies based on similarity in content rather than user behavior.

    ### 🧠 Recommendation Logic
    - Recommends movies similar to the selected title

    ### 🛠️ Technologies Used
    - Python
    - Streamlit
    - Pandas
    - Hugging Face Hub
    - OMDb API

    ### ✅ Key Features
    - Real-time IMDb rating & details
    - Fast similarity matching
    - Clean and simple UI

    ### 🎓 Academic Use
    - Demonstrates ML + API integration
    """
)


movies = load_movies()
similarity = load_similarity()

st.markdown("<h1 style='text-align:center;'>🎥 Movie Recommendation System</h1>", unsafe_allow_html=True)

selected_movie = st.selectbox("Search Movie", movies["title"].values)

if st.button("Recommend"):
    left, right = st.columns([2, 1])

    with left:
        st.subheader("🎬 Selected Movie Details")
        st.markdown(f"### {selected_movie}")

        details = fetch_movie_details(selected_movie)
        if details:
            st.write(f"⭐ IMDb Rating: {details['rating']}")
            st.write(f"📅 Year: {details['year']}")
            st.write(f"🎭 Genre: {details['genre']}")
            st.write(f"📝 Plot: {details['plot']}")
        else:
            st.warning("Movie details not available")

    with right:
        st.subheader("✅ Recommended Movies")
        recs = recommend(selected_movie, movies, similarity)
        for i, row in enumerate(recs.itertuples(), 1):
            st.write(f"{i}. {row.title}")

