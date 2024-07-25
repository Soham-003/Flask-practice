import pandas as pd
import streamlit as st
st.title("Hello, Let's get started!")

data = {
    'a' : [1,2,3,4,5],
    "b" : [2,3,4,5,6],
    "c" : [3,4,5,6,7]
}

df = pd.DataFrame(data)
st.write(df)
st.line_chart(df)
name = st.text_input("Enter your name : ")
if name :
    st.write(f"Hi, {name}")
age = st.slider("Select : ",2,100,22)   
st.write("Your age is",age) 
uploaded_file = st.file_uploader("Choose a csv file ",type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)