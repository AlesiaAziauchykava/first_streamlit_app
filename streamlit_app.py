import streamlit

streamlit.title('My Parents new healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣Omega 3 and Brabery Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket Smothie')
streamlit.text('🐔Hight-Bolled Free-Ranhe Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
