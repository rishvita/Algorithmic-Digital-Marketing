import streamlit as st
import os
import pandas as pd
import numpy as np

#add_selectbox=st.sidebar.radio("Select the type of Search Method ",("FAISS"))

#os.chdir('C:/Users/rishv/OneDrive/Northeastern/SEM3/Algorithmic Digital Marketing/Assignments/Assignment3/Streamlit')

#if add_selectbox=='FAISS':
st.title("FACEBOOK ADD SIMILARITY SEARCH")
st.write("----------------------------------------------------")
def get_data():
	return pd.read_csv('faiss.csv')

n=1
df=get_data()
images=df['0'].unique()
st.subheader("Select an image from drop down menu :")
pic=st.selectbox('Choices:',images)
st.write("**You selected**")
st.image(pic,width=None)

#Displaying output
z=st.slider('How many images do you want to see?',1,10,5)
st.write("---------------------------------------------------------")
st.subheader("Output:")
st.write('**Images similar to the image selected by you: **')
for index,row in df.iterrows():
	if row['0']==pic:
		while n<z+1:
			st.image(row[n],use_column_width=None,caption=row[n])
			n+=1

