import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")
st.subheader("Hello")

st.sidebar.image("Image/logo.png",caption="NTT Data")
option = st.sidebar.selectbox(
    'Select Model',
    ('Model1', 'Model2', 'Model3'))




