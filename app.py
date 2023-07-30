# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:02:11 2023

@author: nanip
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('D:/trained_model.sav','rb'))
def predict(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

     #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    #standardize the input data
    prediction = loaded_model.predict(input_data_reshaped)
    if(prediction[0] == 0):
      return('person is not diabetic')
    else:
      return('person is diabetic')
def main():
    st.title('Diabetes Prediction')
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose     = st.text_input('Glucose level')
    Blood_Pressure = st.text_input('BP level')
    Skin_Thickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age')
    
    #code for prediction
    diagnosis = ''
    if st.button('Test result'):
        diagnosis = predict([Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    