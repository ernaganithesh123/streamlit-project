import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.markdown("<h1 style = 'text-align: center;'>Data Visualizer</h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
st.text("This is a simple data visualizer built using streamlit library in python. It allows a csv files to uploade.")
files = st.file_uploader("Uploade multiple files",type=["csv"],accept_multiple_files=True)
files_name = []
if files == []:
    st.warning("Please uploade at least one file to visualize")
else:
    for file in files:
        files_name.append(file.name)
    selected_file = st.selectbox("Select files to visualize",options=files_name)
   
    for file in files:
       if file.name == selected_file:
           data = pd.read_csv(file)
           sample_data = data[0:15]
    st.write(data.head())
    select_box = st.sidebar.radio("Select the type of graph.",options=["None","Plot chart","Bar chart","Horizontal bar","Histogram"])
    numeric_col = data.select_dtypes(exclude="object").columns
    categorical_col = data.select_dtypes(include = "object").columns
    if select_box == "Plot chart":
        st.markdown("<h1 style = 'text-align: center;'>Plot chart</h1>",unsafe_allow_html = True)
        x_axis = st.selectbox("Select the X axis",options=numeric_col)
        y_axis = st.selectbox("Select the Y axis",options=numeric_col)
        fig = plt.figure(figsize=(10,6))
        plt.plot(sample_data[x_axis],sample_data[y_axis],color="red",marker="d",markersize=10)
        st.write(fig)
    elif select_box == "Bar chart":
        st.markdown("<h1 style = 'text-align: center;'>Bar chart</h1>",unsafe_allow_html = True)
        x_axis = st.selectbox("Select the x axis",options=numeric_col)
        y_axis = st.selectbox("select the y axis",options=categorical_col)
        fig = plt.figure(figsize=(10,6))
        plt.bar(sample_data[x_axis],sample_data[y_axis])
        st.write(fig)
    elif select_box == "Horizontal bar":
        st.markdown("<h1 style = 'text-align: center;>Horizontal chart</h1>",unsafe_allow_html = True)
        x_axis = st.selectbox("Select the x axis",options=categorical_col)
        y_axis = st.selectbox("select the y axis",options=numeric_col)
        fig = plt.figure(figsize=(10,6))
        plt.barh(sample_data[x_axis],sample_data[y_axis])
        st.write(fig)
    elif select_box == "Histogram":
        st.markdown("<h1 style = 'text-align: center;'>Histogram</h1>",unsafe_allow_html = True)
        columns = st.selectbox("select the columns to plot histogram",options=data.columns)
        fig = plt.figure(figsize=(10,6))
        plt.hist(data[columns],bins=10)
        st.write(fig)
        