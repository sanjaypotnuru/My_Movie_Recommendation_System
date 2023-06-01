import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://images.tmdb.org/t/p/w500/" + data['poster_path'], data['release_date'][:4]


def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:5]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_tags = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        a, b = fetch_poster(movie_id)
        recommended_movies_posters.append(a)
        recommended_tags.append(b)
    return recommended_movies, recommended_movies_posters, recommended_tags


movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, tags = recommend(selected_movie_name)
    frame_width = 300
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"[{names[0]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[0]].index[0]].movie_id})")
        st.image(posters[0])
        st.text(tags[0])
    with col2:
        st.markdown(f"[{names[1]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[1]].index[0]].movie_id})")
        st.image(posters[1])
        st.text(tags[1])
    with col3:
        st.markdown(f"[{names[2]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[2]].index[0]].movie_id})")
        st.image(posters[2])
        st.text(tags[2])
    with col4:
        st.markdown(f"[{names[3]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[3]].index[0]].movie_id})")
        st.image(posters[3])
        st.text(tags[3])
    with col5:
        st.markdown(f"[{names[4]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[4]].index[0]].movie_id})")
        st.image(posters[4])
        st.text(tags[4])
