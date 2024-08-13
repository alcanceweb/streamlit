import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Simple Data Dashbard')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Data Preview')
    st.write(df.head())  # imprime os dados do csv

    st.subheader('Data Summary')
    st.write(df.describe()) # cria um sumário genérico

    st.subheader('Filter Data')
    columns = df.columns.tolist() # lista os cabeçalhos das colunas do csv e joga em columns
    selected_column = st.selectbox('Select column to filter by', columns) # o item que o usuário escolher será jogado em selected_column
    unique_values = df[selected_column].unique() 
    selected_value = st.selectbox('Select value', unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader('Plot Data')
    x_column = st.selectbox('select x-axis column', columns)
    y_column = st.selectbox('select y-axis column', columns)

    if st.button('Generate Plot'):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write('Waiting on file upload...')