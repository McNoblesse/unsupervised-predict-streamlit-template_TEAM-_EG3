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

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home", "About Us", "Recommender System","Solution Overview", "Feedback"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Home":
        #st.markdown("# GreenRising 🎈")
        st.sidebar.markdown("Home Page 🏡")
        #st.image('GreenRising.jpg', width= 250)

        tab1, tab2, tab3, tab4 = st.tabs(["Home Page 🏡", "About Us 🎈", "EDA Process🚧", "Feedback 💌"])

        #tab1.link_button("Test Model", "http://localhost")

        #tab2.link_button("Test Model", "http://localhost:8501/About_Us")

        #tab3.link_button("Test Model", "http://localhost:8501/EDA_Process")

        #tab4.link_button("Test Model", "http://localhost:8501/Feedback")

        st.header("Welcome to DataEra, where data meets insight.!")
        st.write("Discover the power of data analytics and machine learning")
        st.divider()
        st.subheader("Our Mission:")
        st.write("Our mission is to catalyze positive environmental change by fostering awareness, implementing eco-friendly solutions, and advocating for policies that mitigate climate change's impact. Through collaborative efforts, we strive to build resilient  communities that actively contribute to the well-being of the Earth, ensuring a legacy of sustainability \for generations to come.")
        st.write("➡Empowering businesses through data-driven decision-making.")
        st.write("➡Transforming raw data into actionable insights.")

        st.subheader("Our Vision:")
        st.write("Empowering communities for a sustainable future, where the delicate balance of our planet \is respected, and all individuals thrive in harmony with nature.")

        st.header("Key Features:")
        st.write("➡Advanced Data Analytics: Uncover hidden patterns and trends.")
        st.write("➡Machine Learning Models: Predictive modeling for informed decisions.")
        st.write("➡Insightful Visualizations: Communicate complex data in a clear manner.")

        st.divider()
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Explore our EDA Report for in-depth insights.")
            #st.link_button("EXPLORE EDA", "http://localhost:8501/EDA_Process")
            st.markdown("<a href='http://localhost:8501/EDA_Process'><button>EXPLORE EDA</button></a>", unsafe_allow_html=True)

        with col2:
            st.subheader("See the performance of our models on the Model Test page.")
            #st.link_button("Test Model", "http://localhost:8501/Test_model")
            st.markdown("<a href='http://localhost:8501/Test_model'><button>Test Model</button></a>", unsafe_allow_html=True)


    if page_selection == "About Us":
        #st.image('GreenRising.jpg', width= 150)
        st.header("About Us 🎈")
        st.sidebar.markdown("About Us🎈")
        st.divider()
        st.subheader("Company Overview:")
        st.write("Founded in 2017, GreenRising is an NGO that seeks to educate corporate entities and individuals on the importance of climate change, sustainable development and responsible custodianship of our planet and it's resources")
        st.header("")

        st.caption("What Sets Us Apart:")
        st.write("➡Expertise in advanced data analytics and machine learning")
        st.write("➡Committed to delivering high-quality, impactful results")

        st.divider()
        st.subheader("Meet Our Team:")

        #with st.container():
            #col1, col2, col3 = st.columns(3)

            #with col1:
                #st.image('Vicky.jpg', width= 200)
                #st.subheader("Victoria Chukwuno")
                #st.caption("Team Lead")

            #with col2:
                #st.image('Lesiba.jpg', width= 200)
                #st.subheader("Lesiba Victoria")
                #st.caption("Data Analyst")
                    
            #with col3:
                #st.image('Bakwe.jpg', width= 200)
                #st.subheader("Bakwe Chokoe")
                #st.caption("Project Manager")
        st.write("")
        st.write("")
        st.write("")
       # with st.container():
            #col4, col5, col6 = st.columns(3)

           # with col4:
                #st.image('Josh.jpg', width= 200)
                #st.subheader("Joshua Oluwole")
                #st.caption("Software Engineer")
                
           # with col5:
                #st.image('Fabian.png', width= 200)
                #st.subheader("Fabian Dafat")
                #st.caption("Data Engineer")

        
           # with col6:
                #st.image('kemi.png', width= 200)
                #st.subheader("Data Specialist")
                #st.caption("Data Specialist")



    if page_selection == "Recommender System":
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


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


    if page_selection == "Feedback":

        #st.image('GreenRising.jpg', width= 150)
        st.header("Feedback 💌")
        st.sidebar.markdown("Feedback 💌")

        st.subheader("We would like to here your review about the prediction of our model")
        st.write("Kindly comment in the textbox below:")

        with st.form("my_form"):
            title = st.text_input('Your feedback', 'Write here')
        # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("Thanks for your time")


if __name__ == '__main__':
    main()
