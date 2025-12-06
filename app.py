



import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# ---------------- OMDb API KEY ---------------- #
API_KEY = "eb6579ab"

# ---------------- LOAD FILES ---------------- #
movies = pickle.load(open("movies.pkl", "rb"))
movie_dict = pickle.load(open("movie_dict.pkl", "rb"))

movies_df = pd.DataFrame(movie_dict)

# ---------------- FUNCTIONS ---------------- #
def fetch_movie_details(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    response = requests.get(url).json()
    return response

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(movies[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies

# ---------------- UI ---------------- #
st.title("🎬 Movie Recommendation System")
st.caption("Search movies and get ML-based recommendations")

selected_movie = st.selectbox(
    "🔍 Select a movie",
    movies_df['title'].values
)

if st.button("Recommend"):
    movie_data = fetch_movie_details(selected_movie)

    col1, col2 = st.columns([1, 2])

    with col1:
        if movie_data.get("Poster") != "N/A":
            st.image(movie_data["Poster"], width=300)
        else:
            st.image("https://via.placeholder.com/300x450")

    with col2:
        st.subheader(movie_data.get("Title", selected_movie))
        st.write("⭐ IMDb Rating:", movie_data.get("imdbRating", "N/A"))
        st.write("🎭 Genre:", movie_data.get("Genre", "N/A"))
        st.write("📅 Year:", movie_data.get("Year", "N/A"))
        st.write("🕒 Runtime:", movie_data.get("Runtime", "N/A"))
        st.write("📖 Plot:", movie_data.get("Plot", "N/A"))

    st.markdown("---")
    st.subheader("✅ Recommended Movies")

    recommendations = recommend(selected_movie)
    cols = st.columns(5)

    for i, movie in enumerate(recommendations):
        with cols[i]:
            details = fetch_movie_details(movie)
            if details.get("Poster") != "N/A":
                st.image(details["Poster"], width=150)
            st.caption(movie)

