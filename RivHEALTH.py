"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import json



# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from streamlit_lottie import st_lottie

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

st.sidebar.image('resources/imgs/rivhealth-1.jpeg', width=300)

# Function to load Lottie animation file
def load_lottiefile(path:str):
    with open(path, "r") as f:
        return json.load(f)
    


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    #page_options = ["Home", "About Us", "RivHEALTH Dash Board","Solution Overview", "Feedback"]
     
     # DO NOT REMOVE - Sidebar animation
    with st.sidebar:
        st.write("Select an option")
        page_options =st.radio("", ["Home", "About Us", "RivHEALTH Dash Board","River Thames History", "Feedback"])

        lottie = load_lottiefile("resources/imgs/location.json")
        st_lottie(lottie, key='animation')

       
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    #page_selection = st.sidebar.selectbox("Select an option", page_options)
    if page_options == "Home":

        st.image('resources/imgs/river.jpg', width= 700)   

        st.header("Welcome to RivHealth!")
        st.write("")
        st.write("RivHEALTH is platform aimed at providing comprehensive view of river thames health and identify pollution sources.Our goal is to empower stakeholders such as water companies, river conservation trusts, environmental agencies, farmers, and local authorities with data-backed insights for informed decision-making and policy development. ")

        st.divider()
        # Real-time map
        st.write("Real-time Map:")
        m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)
        folium_static(m)

        st.divider()
        st.write("### Our Services")
        col1, col2 = st.columns(2)

        with col1:
            st.write("##### River health Awareness")
            st.write("Provide the public and industry player with education regarding activities that negatively affect\
                     river thames health.Help water companies, farmers and the general public allocate resources effectively\
                     by highlighting critical areas for infrastructure upgrades.")

        with col2:
            edu_lottie = load_lottiefile("resources/imgs/ecology.json")
            st_lottie(edu_lottie)

        col3, col4 = st.columns(2)

        with col3:
            st.write("##### Interactive Platform")
            st.write("An platform that will collect and Analyze data from various sources to understand the overall health of rivers and pinpoint the sources of pollution.\
                    This dashbord will show the chemical and biological composition of water in your area.")

        with col4:
            dash_lottie = load_lottiefile("resources/imgs/dashboard.json")
            st_lottie(dash_lottie)
            st.write()

        col5, col6 = st.columns(2)

        with col5:
            st.write("##### Pollution source ")
            st.write("To effectively pinpoint sources of pollution at various locations and  \
                    to visually represent the river and its surroundings on a map.")

        with col6:
            sour_lottie = load_lottiefile("resources/imgs/point.json")
            st_lottie(sour_lottie)

        col7, col8 = st.columns(2)

        st.divider()

        col9, col10 = st.columns(2)

        with col9:
            st.write("###### RivHealth 🏡")
        with col10:
            st.write("###### Copyright © 2024")

    if page_options == "About Us":
        st.title("About Us ")

        st.divider()
        st.write("### Our Mission")
        st.write("##### Empowering the public through Data Excellence")
        st.write(" our mission is to be the trusted source of truthful insights in the water industry.\
                  We have observed a lack of understanding among stakeholders about river health and its impact,\
                  including issues like sewage discharges, agricultural runoff, misconnected sewers, illegal dumping,\
                  and industrial waste. To address this, we are developing a platform to provide a comprehensive view of\
                  river health and identify pollution sources. Our goal is to empower stakeholders such as water companies,\
                  river conservation trusts, environmental agencies, farmers, and local authorities around River Thames with data-backed insights for informed decision-making and policy development.")

        st.image('resources/imgs/rivermapcropped.jpg', width= 400)

        st.divider()
        st.write("## Meet Our Team:")
        st.write("##### 🌐 Innovation at the Core")

       # Function to display oval-like square image with caption
        def image_with_caption(image_path, caption, width=250):
            st.markdown(
            f"""
            <div style="text-align:center">
                <figure>
                    <img src="{image_path}" style="border-radius: 20%; border: 2px solid #fff; width: {width}px;">
                     <figcaption>{caption}</figcaption>
                </figure>
            </div>
            """,
            unsafe_allow_html=True,
            )

        with st.container():
            col20, col21, col22 = st.columns(3)

            with col20:
                image_with_caption('resources/imgs/fhulu.jpg', 'Fhulufhelo')

            with col21:
                image_with_caption('resources/imgs/lauryn.png', 'Lauryn')
                
            with col22:
                image_with_caption('resources/imgs/lebo.png', 'Lebohang')

        st.write("")
        st.write("")

        with st.container():
            col23, col24, col25 = st.columns(3)

            with col23:
                image_with_caption('resources/imgs/justice.jpeg', 'Justice')

            with col24: 
                image_with_caption('resources/imgs/omotola.jpeg', 'Omotola')

            with col25:
                image_with_caption('resources/imgs/nk.jpeg', 'Ngokoana')
                

        st.write(" ")
        st.write(" ")
     
       
        st.divider()

        col17, col18, col19 = st.columns(3)

        with col17:
            st.write("###### RivHEALTH 🏡")
        with col19:
            st.write("###### Copyright © 2024")


    if page_options == "RivHEALTH Dash Board":
        #st.markdown("# GreenRising 🎈")
        st.image('resources/imgs/QuantumInsights.png', width= 170)
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col17, col18, col19 = st.columns(3)

        with col17:
            st.image('resources/imgs/QuantumInsights.png', width= 80)
        with col18:
            st.write("###### RivHEALTH 🏡")
        with col19:
            st.write("###### Copyright © 2024")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_options == "River Thames History":
        st.write("## Solution Overview 🚧")   

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
        st.write("In the Content-Based Filtering approach, we analyze the content and features of movies, such as genres, actors, directors, and tags. By understanding the unique characteristics of each movie, we can recommend similar movies that match the user's preferences.")
        st.write("On the other hand, the Collaborative-Based Filtering approach leverages the wisdom of the crowd. We analyze the ratings and preferences of similar users to identify movies that align with the user's tastes. This technique allows us to uncover hidden gems that might not be obvious based on content alone.")
        st.write("By combining these two approaches, we create a hybrid recommendation system that offers the best of both worlds. ")
       
        st.write("### Exploratory Data Analysis EDA")
        eda_select = st.selectbox('Select a Visual to inspect', ('Rating Distribution', 'Most Common Genres', 'Movie Budget', 'Top Directors'))
        if eda_select == "Rating Distribution":
            st.image('resources/imgs/Ratings_distribution.jpg', use_column_width= True)
            st.write("Here we explore and perform feature engineering on the movies ratings data. We create a dataframe to check ratings and the number of ratings a movie has and use visuals to view the distribution.\
                    The majority of ratings in the viwer's dataset is comprised of rations around 3.0")
            st.write(" ")
            st.image('resources/imgs/Ratings_boxlot.jpg', use_column_width= True)
            st.write("Here we also explore the boxplot of the rating to get the Outliers within the rating of movies by users, The boxplot shows a distribution \
                    of rating in the train dataset. with the minum being 0.5 and the maximum being 5 and the avarage being 3.53")
        
        #Top 10 Genres
        if eda_select == "Most Common Genres":
            st.image('resources/imgs/Top_genres.jpg', use_column_width= True)
            st.write("Here we explore and built a Visual Representation of the Top Genres with the highest view by the Users, and it was noted that Drama has the highest view and ratings by the Users ")
        
        #Movie Budget
        if eda_select == "Movie Budget":
            st.image('resources/imgs/movie_budget.jpg', use_column_width= True)
            st.write("Here we explore the Movies based on the budgetted fee or cost of production of the movies, in no order of year of production or Casts.")
        
        #Movie Directors
        if eda_select == "Top Directors":
            st.image('resources/imgs/Director_chart.jpg', use_column_width= True)
            st.write("Here we have created a Pie Chart which is showing the Distribution of the Top Rated Directors, based on User Ratings and Number of Movies Directed.")

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col25, col26, col27 = st.columns(3)

        with col25:
            st.image('resources/imgs/QuantumInsights.png', width= 80)
        with col26:
            st.write("###### RivHEALTHs 🏡")
        with col27:
            st.write("###### Copyright © 2024")



    if page_options == "Feedback":
        st.image('resources/imgs/QuantumInsights.png', width= 170)
        st.title("Feedback 💌")

        st.subheader("We would like to here your review about the prediction of our model")
        st.write("Kindly comment in the textbox below:")

        with st.form("my_form"):
            title = st.text_input('Your feedback', 'Write here')
        # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("Thanks for your time")

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col17, col18, col19 = st.columns(3)

        with col17:
            st.image('resources/imgs/QuantumInsights.png', width= 80)
        with col18:
            st.write("###### RivHEALTH 🏡")
        with col19:
            st.write("###### Copyright © 2024")

if __name__ == '__main__':
    main()