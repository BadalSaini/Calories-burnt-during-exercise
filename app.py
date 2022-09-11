import streamlit as st
import joblib

#load the joblib model
model_nb = joblib.load('Calories-burnt')

st.title('PRIDICTION OF CALORIES BURNT DURING EXERCISE')
ip = st.text_input('Enter your text :')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
