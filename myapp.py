import streamlit as st 

st.write("hello iman hensem")
st.write("sial zharfan")
st.write("hehe")

st.selectbox("Kuala Lumpur is located at",
['Malaysia', 'Thailand', 'UK'])

st.multiselect("Select 2 states",
['Selangor','Johor','Kedah'])

st.button("Click Here to Proceed")

st.slider("Select the length of stay", 1,10, value=3)

number = st.number_input("Insert a number",
value=None, placeholder="Type a number...")

st.write("The current number is ", number)

from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampleData.xlsx')
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")

st.line_chart(df, x="Location", y="Income")

st.scatter_chart(df, x="Location", y="Income")



tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   


col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write("")