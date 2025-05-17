# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Streamlit, and machine learning techniques to suggest top movies similar to your favorite one. It also fetches movie posters using the OMDB API for a more engaging UI.

---

## 🚀 Project Highlights

- 🔍 **Content-Based Filtering**: Recommends movies based on similarity of content.
- 📊 **Precomputed Similarity Matrix**: For fast and efficient retrieval.
- 🎞️ **Interactive UI with Streamlit**: Easy-to-use dropdown menu for movie selection.
- 🖼️ **OMDB API Integration**: Fetches and displays movie posters.
- ⚡ **Instant Recommendations**: Top 5 movies shown with thumbnails and titles.

---

## 🛠️ Tech Stack

- **Python** 🐍
- **Pandas** 📊
- **Scikit-learn** 🤖
- **Streamlit** 🌐
- **Pickle** for model and data serialization
- **OMDB API** for fetching movie poster images

---

## 🧠 How it Works

1. The user selects a movie from a dropdown menu.
2. A similarity score is computed using cosine similarity (preprocessed).
3. Top 5 most similar movies are fetched.
4. Posters are retrieved from the OMDB API.
5. Recommendations are displayed with images and titles in a grid layout.

---

## 🖥️ App Preview

![Movie Recommender Screenshot](Movie Matchmaker/app interface 1.png)
---

## 🧾 Files in the Project

| File/Folder         | Description                           |
|---------------------|---------------------------------------|
| `app.py`            | Streamlit web app script              |
| `movies_dict.pkl`   | Dictionary of movies with features    |
| `similarity.pkl`    | Precomputed similarity matrix         |
| `Movie_Recommender.ipynb` | Jupyter notebook for data prep & EDA |

---



