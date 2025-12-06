import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(open(os.path.join(BASE_DIR, "movies.pkl"), "rb"))
similarity = pickle.load(open(os.path.join(BASE_DIR, "similarity.pkl"), "rb"))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    return [movies.iloc[i[0]]['title'] for i in movie_list]


st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    cols = st.columns(5)
    for i, movie in enumerate(recommendations):
        with cols[i]:
            st.write(movie)

st.sidebar.header("About Project")
st.sidebar.write("""
Movie recommendation using cosine similarity  
Final Year Project – Streamlit App
""")


