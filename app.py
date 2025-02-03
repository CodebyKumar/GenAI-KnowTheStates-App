import streamlit as st
import langchain_helper

st.title("Know The States")

country = st.sidebar.selectbox("Select the country", ("India", "United States", "Russia", "Japan"))

if country:
    response = langchain_helper.get_states(country)
    st.header(country)
    st.write("Sates of ",country)
    st.write(response)
    