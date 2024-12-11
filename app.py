import streamlit as st
import pandas as pd
import pickle
import requests

st.title("Top Movie Recommendations for you...")

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(title):
    response = requests.get('https://www.omdbapi.com/?t={}&apikey=747577ea'.format(title))
    data = response.json()
    return data['Poster']

def recommend_movie(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].title))

    return recommended_movies,recommended_movies_posters

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend_movie(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

