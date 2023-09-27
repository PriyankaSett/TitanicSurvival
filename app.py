"""
Steps : 

1. Load the data from web interface.
2. Transform the data as done in notebook. 
3. Load the best model pickle file.
4. Get prediction and display. 

"""

import os 
import pickle
import requests

import numpy as np
import pandas as pd 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import streamlit as st 

# Page header
st.header("Titanic Survival and Analysis Prediction")

# getting inputs
pclass = st.selectbox('Pclass', [1,2,3])
sex = st.selectbox('Sex', ['female', 'male'])
age = int(st.number_input('Age:', 0, 120, 20))
sibsp = st.selectbox('Number of siblings/Spoused Aboard', [0,1,2,3,4,5,8])
#sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
#par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
parch = st.selectbox('Number of parents / children aboard' ,[0, 1,2,3,4,5,6])
fare = int(st.number_input('Fare', 0, 500, 0))

st.button('Predict')

prediction_state = st.markdown('Getting Prediction ...')


# data as dataframe : 
data1 = pd.DataFrame({
    'Pclass' : [pclass],
    'Sex' : [sex],
    'Age' : [age], 
    'SibSp' : [sibsp],
    'Parch' : [parch], 
    'Fare' : [fare]
})

# loading the preprocessor file :
preprocessor_pickle = pickle.load(open('preprocessor.pkl', 'rb'))
data1_scaled = preprocessor_pickle.transform(data1)


# loading best model file :
model_pickle = pickle.load(open('best_dt_clf.pkl', 'rb'))


# get predictions : 
pred = model_pickle.predict(data1_scaled)

if pred[0] == 0:
    msg = 'This passenger is predicted to be: **died**'
else:
    msg = 'This passenger is predicted to be: **survived**'

prediction_state.markdown(msg)