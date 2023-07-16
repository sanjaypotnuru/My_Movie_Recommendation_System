import streamlit as st
import pickle
import pandas as pd
import requests
import webbrowser


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://images.tmdb.org/t/p/w500/" + data['poster_path'], data['release_date'][:4], data['id'], data['vote_average']


def fetch_trailer(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/videos?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    if data['results']:
        return "https://www.youtube.com/watch?v=" + data['results'][0]['key']
    else:
        return None


def recommend(selected_movie):
    movie_index = movies[movies['title'] == selected_movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_tags = []
    recommended_scores=[]
    recommended_trailers = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        a, b, c, d = fetch_poster(movie_id)
        recommended_movies_posters.append(a)
        recommended_tags.append(b)
        recommended_trailers.append(c)
        recommended_scores.append(d)
    return recommended_movies, recommended_movies_posters, recommended_tags, recommended_trailers,recommended_scores


movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movies = movies[:-5]
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, tags, trailers, scores = recommend(selected_movie_name)
    frame_width = 300
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"[{names[0]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[0]].index[0]].movie_id})")
        st.image(posters[0])
        st.text(tags[0])
        user_score = int(scores[0] * 10)
        star_bullet = "&#9733;"
        star_html = f"<span style='color:gold;'>{star_bullet}</span>"
        st.markdown(f"<p style='text-align:center;'><strong> User Score: {star_html}{scores[0]}/10</strong></p>", unsafe_allow_html=True)
        st.progress(user_score)
        trailer_url_1 = fetch_trailer(trailers[0])
        if trailer_url_1:
            st.button(f"Watch Trailer", on_click=lambda: webbrowser.open_new_tab(trailer_url_1))
        else:
            st.write("Trailer not available.")
    with col2:
        st.markdown(f"[{names[1]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[1]].index[0]].movie_id})")
        st.image(posters[1])
        st.text(tags[1])
        user_score = int(scores[1] * 10)
        star_bullet = "&#9733;"
        star_html = f"<span style='color:gold;'>{star_bullet}</span>"
        st.markdown(f"<p style='text-align:center;'><strong> User Score: {star_html}{scores[1]}/10</strong></p>", unsafe_allow_html=True)
        st.progress(user_score)
        trailer_url_2 = fetch_trailer(trailers[1])
        if trailer_url_2:
            st.button(f"Watch Trailer ", on_click=lambda: webbrowser.open_new_tab(trailer_url_2))
        else:
            st.write("Trailer not available.")
    with col3:
        st.markdown(f"[{names[2]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[2]].index[0]].movie_id})")
        st.image(posters[2])
        st.text(tags[2])
        trailer_url_3 = fetch_trailer(trailers[2])
        star_bullet = "&#9733;"
        star_html = f"<span style='color:gold;'>{star_bullet}</span>"
        st.markdown(f"<p style='text-align:center;'><strong> User Score: {star_html}{scores[2]}/10</strong></p>", unsafe_allow_html=True)
        st.progress(user_score)
        #st.markdown(f"<p style='text-align:center;'><strong>User Score: {scores[2]}</strong></p>", unsafe_allow_html=True)
        if trailer_url_3:
            st.button(f" Watch Trailer    ", on_click=lambda: webbrowser.open_new_tab(trailer_url_3))
        else:
            st.write("Trailer not available.")
    with col4:
        st.markdown(f"[{names[3]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[3]].index[0]].movie_id})")
        st.image(posters[3])
        st.text(tags[3])
        user_score = int(scores[3] * 10)
        star_bullet = "&#9733;"
        star_html = f"<span style='color:gold;'>{star_bullet}</span>"
        st.markdown(f"<p style='text-align:center;'><strong> User Score: {star_html}{scores[3]}/10</strong></p>", unsafe_allow_html=True)
        st.progress(user_score)
        trailer_url_4 = fetch_trailer(trailers[3])
        if trailer_url_4:
            st.button(f"Watch Trailer  ", on_click=lambda: webbrowser.open_new_tab(trailer_url_4))
        else:
            st.write("Trailer not available.")
    with col5:
        st.markdown(f"[{names[4]}](https://www.themoviedb.org/movie/{movies.iloc[movies[movies['title'] == names[4]].index[0]].movie_id})")
        st.image(posters[4])
        st.text(tags[4])
        user_score = int(scores[4] * 10)
        star_bullet = "&#9733;"
        star_html = f"<span style='color:gold;'>{star_bullet}</span>"
        st.markdown(f"<p style='text-align:center;'><strong> User Score: {star_html}{scores[4]}/10</strong></p>", unsafe_allow_html=True)
        st.progress(user_score)
        trailer_url_5 = fetch_trailer(trailers[4])
        if trailer_url_5:
            st.button(f"   Watch Trailer", on_click=lambda: webbrowser.open_new_tab(trailer_url_5))
        else:
            st.write("Trailer not available.")


