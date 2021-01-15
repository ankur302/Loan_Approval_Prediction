# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:45:17 2021

@author: hp
"""


import streamlit as st
import numpy as np
from PIL import Image
import pickle

pickle_in = open('loan_prediction.pkl','rb')
rfc = pickle.load(pickle_in)

def welcome():
    return 'Welcome All'
def model_predict2(Encoded_Property_Area,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History):
  x = np.zeros(13)
  
  if (Encoded_Property_Area =='Rural'):
            
      Encoded_Property_Area = 0

  elif (Encoded_Property_Area=='SemiUrban'):
            
      Encoded_Property_Area = 1
            
  else:
             
      Encoded_Property_Area = 2
  
    
  
    
  if(Credit_History == 'Has All debts Paid'):
            
         Credit_History = 1   
         
  else:
         Credit_History = 0
  
    
  x[0] = Encoded_Property_Area
  x[1] = ApplicantIncome
  x[2] = CoapplicantIncome
  x[3] = LoanAmount
  x[4] = Loan_Amount_Term
  x[5] = Credit_History

  pred =  rfc.predict([x])[0]
  
  if pred == 1:
      return "Approved"
  else:
      return 'Not Approved'

def main():
    st.title("Loan Approval Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Loan Approval Prediction App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Property_Area_location = st.selectbox("Property Area Location",['Rural','Urban','SemiUrban'])
    ApplicantIncome = st.slider("Applicant's Yearly Income(in hundreds)",min_value = 0,max_value = 81000,value = 1000,step = 81)
    CoapplicantIncome = st.slider("Yearly Income of Coapplicant(in hundreds)",min_value = 0,max_value = 42000,value = 1000,step = 42)
    LoanAmount = st.slider("Loan Amount(in 1k)",min_value = 0,max_value = 800,value = 50,step = 16)
    Loan_Amount_Term = st.slider("Term of the Loan Amount(in days)",min_value = 0,max_value = 360,value =90,step = 4)
    Credit_History = st.selectbox("Credit History",['Has All debts Paid','Not Paid'])
    result=""
    if st.button("Predict"):
        result=model_predict2(Property_Area_location,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History)
    st.success('Your Loan will be {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()