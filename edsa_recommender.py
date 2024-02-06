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
        st.sidebar.markdown("Home Page 🏡")
        st.image('resources/imgs/QuantumInsights.png', width= 170)   

        st.header("Welcome to QuantumInsights, Your Gateway to Innovative Data Solutions!")
        st.write("🚀 Empowering Businesses with Data Excellence")
        st.write("")
        st.write("At QuantumInsights, we harness the power of data to drive transformative insights and solutions. \
        As a leading data science firm, we specialize in delivering cutting-edge services that propel businesses \
        to new heights. Explore our homepage to discover how we can unlock the full potential of your data.")

        st.divider()
        st.write("### Our Services")
        col1, col2 = st.columns(2)

        with col1:
            st.write("##### Data Analytics and Visualization")
            st.write("➡ Transform raw data into actionable insights. Our expert analysts leverage advanced tools \
            and techniques to uncover trends, patterns, and key metrics that drive informed decision-making.")

        with col2:
            st.image('resources/imgs/Data_Analytics_and_Visuals.jpg', width= 300)

        col3, col4 = st.columns(2)

        with col3:
            st.write("##### Machine Learning Solutions")
            st.write("➡ Embrace the future with our machine learning expertise. From predictive modeling to natural \
            language processing, our team crafts intelligent solutions that adapt to your evolving business needs.")

        with col4:
            st.image('resources/imgs/Machine_learning_solution.jpg', width= 300)
       
        col5, col6 = st.columns(2)

        with col5:
            st.write("##### Big Data Management")
            st.write("➡ Efficiently manage and analyze vast datasets. Our big data solutions ensure seamless processing, \
            storage, and retrieval of information, enabling you to make data-driven decisions at scale.")

        with col6:
            st.image('resources/imgs/big_data.jpg', width= 300)

        col7, col8 = st.columns(2)

        with col7:
            st.write("##### AI-powered Applications")
            st.write("➡ Experience the power of artificial intelligence. We design and develop intelligent applications \
            that enhance user experiences, automate processes, and deliver tangible business outcomes.")

        with col8:
            st.image('resources/imgs/AI_App.jpg', width= 300)
 
        st.divider()
        st.write("### Why Choose QuantumInsights?")
        col9, col10 = st.columns(2)

        with col9:
            st.image('resources/imgs/Team_expert.jpg', width= 200)

        with col10:
            st.write("➡ Expert Team: Our team of seasoned data scientists, engineers, and analysts bring a wealth of \
            expertise to every project.")
        
        col11, col12 = st.columns(2)

        with col11:
            st.image('resources/imgs/innovation.jpg', width= 200)

        with col12:
            st.write("➡ Innovation: Stay ahead in the dynamic world of data science with our commitment to continuous \
            innovation and exploration of emerging technologies.")

        col13, col14 = st.columns(2)

        with col13:
            st.image('resources/imgs/tailored_solution.jpg', width= 200)

        with col14:
            st.write("➡ Tailored Solutions: We understand that every business is unique. Our solutions are customized \
            to meet your specific challenges and goals.")

        col15, col16 = st.columns(2)

        with col15:
            st.image('resources/imgs/proven_solution.jpg', width= 200)

        with col16:
            st.write("➡ Proven Results: Discover success stories from businesses that have unlocked value through our \
            data science solutions..")

        st.divider()
        st.write("### Let's Transform Your Data Journey")
        st.write("Whether you're looking to enhance analytics capabilities, implement machine learning solutions, \
        or navigate the world of big data, QuantumInsights is your trusted partner. Let's embark on a journey to turn \
        your data into a strategic asset.")

        st.write("##### 📈 Unlock the Power of Your Data with QuantumInsights - Where Innovation Meets Insight! 🌐")

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col17, col18, col19 = st.columns(3)

        with col17:
            st.image('resources/imgs/QuantumInsights.png', width= 80)
        with col18:
            st.write("###### Quantum Insights 🏡")
        with col19:
            st.write("###### Copyright © 2024")

    if page_selection == "About Us":
        st.image('resources/imgs/QuantumInsights.png', width= 170)
        st.title("About Us 🎈")
        st.sidebar.markdown("About Us🎈")

        st.divider()
        st.write("### Company Overview")
        st.write("Welcome to QuantumInsights – Where Data Unveils Infinite Possibilities!")
        st.write("Founded in 2002 with a Global socio-economic perspective, tailored for the unique needs of clients \
        and for dynamic hub of innovation, education, and entrepreneurship.  At QuantumInsights, we believe in the \
        transformative power of data. Our journey began with a vision \
        to redefine the landscape of data science, turning complex datasets into strategic assets for businesses across \
        diverse industries.")

        st.divider()
        st.write("### Our Mission")
        st.write("##### 🚀 Empowering Businesses through Data Excellence")
        st.write("Our mission is to empower organizations with innovative data solutions, enabling them to navigate \
        the digital era with confidence. We are dedicated to delivering cutting-edge data science services that drive \
        informed decision-making, fuel innovation, and foster sustainable growth.")

        st.divider()
        st.write("### What Sets Us Apart")
        st.write("##### 🌐 Innovation at the Core")
        st.write("At Quantum Insights Labs, innovation is not just a buzzword – it's our guiding principle. Our team \
        of seasoned data scientists, engineers, and analysts thrives on pushing the boundaries of what's possible. \
        We continuously explore emerging technologies, ensuring our clients stay ahead in the dynamic world of data science.")
        st.write("##### 🤝 Tailored Solutions for Your Success")
        st.write("We understand that each business is unique, facing its own challenges and opportunities. That's why we \
        don't believe in one-size-fits-all solutions. Our approach is collaborative, and our solutions are meticulously \
        tailored to meet the specific needs and goals of our clients.")
        st.write("##### 💡 Proven Expertise")
        st.write("Our journey is marked by a track record of success. From data analytics and machine learning to big data \
        management, we bring a wealth of expertise to every project. Explore our success stories and discover how businesses \
        have unlocked value through our data science solutions.")

        st.divider()
        st.write("### Our Commitment")
        st.write("##### ✨ Excellence, Integrity, Innovation")
        st.write("➡ EExcellence: We are committed to delivering solutions of the highest quality, exceeding our clients' expectations.")
        st.write("➡ Integrity: We operate with transparency, honesty, and the utmost respect for our clients, partners, and team members.")
        st.write("➡ Innovation: We thrive on continuous innovation, staying at the forefront of technological advancements to bring fresh \
        perspectives to every project.")

        st.divider()
        st.write("### Let's Shape the Future of Data Together")
        st.write("Whether you are looking to elevate your data analytics, implement machine learning solutions, or navigate the vast world \
        of big data, QuantumInsights is your dedicated partner. Join us on a journey where data becomes a catalyst for growth and transformation.")

        st.write("##### 🚀 Explore Infinite Possibilities with QuantumInsights! 🌐")

        st.divider()
        st.write("## Meet Our Team:")

        with st.container():
            col20, col21, col22 = st.columns(3)

            with col20:
                st.image('resources/imgs/Ngokoana.png', width= 200)

            with col21:
                st.image('resources/imgs/Nina.png', width= 150)
                    
            with col22:
                st.image('resources/imgs/Josh.png', width= 150)

        st.write("")
        st.write("")
        with st.container():
            col23, col24 = st.columns(2)

            with col23:
                st.image('resources/imgs/Joseph.png', width= 150)
                
           #with col5:
                #st.image('Fabian.png', width= 200)

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col17, col18, col19 = st.columns(3)

        with col17:
            st.image('resources/imgs/QuantumInsights.png', width= 80)
        with col18:
            st.write("###### Quantum Insights 🏡")
        with col19:
            st.write("###### Copyright © 2024")


    if page_selection == "Recommender System":
        #st.markdown("# GreenRising 🎈")
        st.sidebar.markdown("Recommender System")
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
        movie_1 = st.selectbox('Fisrt Option',title_list[14765:15222])
        movie_2 = st.selectbox('Second Option',title_list[25655:25435])
        movie_3 = st.selectbox('Third Option',title_list[21312:21243])
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
            st.write("###### Quantum Insights 🏡")
        with col19:
            st.write("###### Copyright © 2024")

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.image('resources/imgs/QuantumInsights.png', width= 170)
        st.title("Solution Overview 🚧")
        st.sidebar.markdown("Solution Overview 🚧")
        #st.image('GreenRising.jpg', width= 250)
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
        st.write("In the Content-Based Filtering approach, we analyze the content and features of movies, such as genres, actors, directors, and tags. By understanding the unique characteristics of each movie, we can recommend similar movies that match the user's preferences.")
        st.write("On the other hand, the Collaborative-Based Filtering approach leverages the wisdom of the crowd. We analyze the ratings and preferences of similar users to identify movies that align with the user's tastes. This technique allows us to uncover hidden gems that might not be obvious based on content alone.")
        st.write("By combining these two approaches, we create a hybrid recommendation system that offers the best of both worlds. This approach allows us to provide accurate recommendations that align with the user's preferences while also introducing them to new and exciting movies they might not have discovered otherwise.")
        st.write("Furthermore, our recommendation engine continuously learns and adapts based on user feedback. As users rate and interact with movies, our system updates its recommendations to reflect their evolving preferences, ensuring that the recommendations stay relevant and personalized over time.")
        st.write("We believe that our winning approach will transform the movie-watching experience for users, providing them with a curated list of movies that they will truly enjoy. Try our Movie Recommender Engine today and let us help you discover your next favorite movie!")

        

    if page_selection == "Feedback":
        st.image('resources/imgs/QuantumInsights.png', width= 170)
        st.title("Feedback 💌")
        st.sidebar.markdown("Feedback 💌")

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
            st.write("###### Quantum Insights 🏡")
        with col19:
            st.write("###### Copyright © 2024")

if __name__ == '__main__':
    main()
