# 🎬 Movie Recommendation System

A **content-based movie recommendation web application** built using **Python and Streamlit**.  
The system recommends movies similar to a selected title based on content similarity and also fetches real-time IMDb details using the **OMDb API**.

🔗 **Live Demo (Streamlit App):**  
https://movie-recommendation-system-jeutphzywpxrqtkgph8hzb.streamlit.app/  

---

## 📌 Project Overview

This project suggests movies by analyzing similarity between movies based on their metadata.  
Instead of recommending based on user behavior, it focuses on **content similarity**, making it fast, simple, and effective.



---

## 🧠 How It Works

1. Movie metadata is loaded from a CSV file
2. A precomputed similarity matrix is used to find similar movies
3. On selecting a movie:
   - Top 5 similar movies are recommended
   - IMDb details of the selected movie are fetched using the OMDb API

Large model files are stored externally using **Hugging Face Hub**.

---

## 🚀 Features

- ✅ Content-based movie recommendations  
- ✅ Real-time IMDb rating, year, genre, and plot  
- ✅ Clean and interactive Streamlit UI  
- ✅ Fast performance using caching  
- ✅ Cloud-deployable (Streamlit Cloud)  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web framework  
- **Pandas & NumPy** – Data processing  
- **OMDb API** – Movie details  
- **Hugging Face Hub** – Model storage  

---







## Dataset and Supporting Files

- **tmdb_5000_credits.csv:** [Download here](https://drive.google.com/file/d/1bpvEM9Rfq2nGtBK0diy0q1syf9nkDTKU/view?usp=sharing)
- **.ipynb_checkpoints:** [View folder](https://drive.google.com/drive/folders/1u46zPIdt4oI2ojBVfDzoT8OklfTJv2LU?usp=drive_link)
- **similarity.pkl:** [Download here](https://drive.google.com/file/d/1lqDXaAaiCNgiSwfTRm_WzRINxPeFmK4j/view?usp=drive_link)
   - **tmdb_5000_movies.csv:** [Download here](https://drive.google.com/file/d/1Z84rt7ud6STxppYz_fNo-ZtSMjArg501/view?usp=sharing)

