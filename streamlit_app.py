import streamlit as st
import pandas as pd
st.title('Penguin Species Predictor')

st.write('This app helps you build and interact with a machine learning model using the penguin dataset.')


with st.expander('Data'):
    st.write('**Raw Data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
    df

    st.write('**X**')
    X = df.drop('species',axis=1)
    X

    st.write('**y**')
    y=df.species
    y


with st.expander('Data Visulization'):
    st.scatter_chart(data=df,x="bill_length_mm",y="body_mass_g",color="species")

# Data Preparations
with st.sidebar:
    st.header("Input features")
    island = st.selectbox("Island",('Biscoe','Dream','Torgersen'))
    gender = st.selectbox("Gender",('male','female'))
    bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)


    
