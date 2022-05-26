# -*- coding: utf-8 -*-
"""happiness_streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dBAUMJufWB2DxrqhXQOXuKf_yiJbaTOz
"""



import streamlit as st 
import joblib 
import numpy as np

from PIL import Image



reload_model = joblib.load('happiness_model')

GDP_per_capita= st.numeric_input('GDP_per_capita')
Social_support = st.numeric_input('Social_support') 
Healthy_life_expectancy= st.numeric_input("Healthy_life_expectancy") 
Freedom_to_make_life_choices= st.numeric_input('Freedom_to_make_life_choices')
Generosity = st.numeric_input('Generosity') 
Perceptions_of_corruption= st.numeric_input("Perceptions_of_corruption") 
result =""

if st.button("Predict"): 
    prediction=reload_model.predict([[GDP_per_capita,Social_support, Healthy_life_expectancy,Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption]])
    st.text('score')
    st.text(prediction)
        
        

















