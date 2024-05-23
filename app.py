import streamlit as st
import langchain_helper 
st.title("Restaurant name generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Arabian","Indian","Italian","Mexican","Japanese","Korean","Chinese"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write("**Menu items**")
    for item in menu_items:
        st.write("-",item)