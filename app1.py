# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:45:17 2021

@author: hp
"""

import streamlit as st
import numpy as np
import pickle

pickle_in = open('improved_loan_prediction.pkl', 'rb')
rfc = pickle.load(pickle_in)


def welcome():
    return 'Welcome All'


def model_predict2(Encoded_Property_Area, ApplicantIncome, CoapplicantIncome, LoanAmount, Married_Yes,
                   Credit_History):
    x = np.zeros(13)

    if (Encoded_Property_Area == 'Rural'):

        Encoded_Property_Area = 0

    elif (Encoded_Property_Area == 'SemiUrban'):

        Encoded_Property_Area = 1

    else:

        Encoded_Property_Area = 2

    if (Credit_History == 'Has All debts Paid'):

        Credit_History = 1

    else:
        Credit_History = 0

    if (Married_Yes == 'Yes'):

        Married_Yes = 1

    else:
        Married_Yes = 0


    x[0] = Encoded_Property_Area
    x[1] = ApplicantIncome
    x[2] = CoapplicantIncome
    x[3] = LoanAmount
    x[4] = Married_Yes
    x[5] = Credit_History
   

    mapping = {0: 'Not Approved',
               1: 'Approved'}
    return mapping[rfc.predict([x])[0]]


def main():
    st.title("Loan Approval Prediction")
    html_temp = """
    <div style="background-color:Blue;padding:20px">
    <h2 style="color:white;text-align:center;">Loan Approval Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Property_Area_location = st.selectbox("Property Area Location", ['Rural', 'Urban', 'SemiUrban'])
    
    ApplicantIncome = st.slider("Applicant's Yearly Income(in hundreds)", min_value=0, max_value=81000, value=1000,
                                step=81)
    
    st.write("Your value is ", ApplicantIncome)
    
    CoapplicantIncome = st.slider("Yearly Income of Coapplicant(in hundreds)", min_value=0, max_value=42000, value=1000,
                                  step=42)
    
    st.write("Your value is ", CoapplicantIncome)
    
    LoanAmount = st.slider("Loan Amount(in 1k)", min_value=0, max_value=800, value=50, step=16)
    
    st.write("Your value is ", LoanAmount)
    #Loan_Amount_Term = st.slider("Term of the Loan Amount(in days)", min_value=0, max_value=360, value=90, step=4)
    #st.write("Your value is ", Loan_Amount_Term)
    
    Credit_History = st.selectbox("Credit History", ['Has All debts Paid', 'Not Paid'])
    
    Married_Yes = st.selectbox("Are You Married ", ['Yes', 'No'])
    
    result = ""
    
    if st.button("Predict"):
    
        result = model_predict2(Property_Area_location, ApplicantIncome, CoapplicantIncome, LoanAmount,
                                Married_Yes, Credit_History)
    st.success('Your Loan will be {}'.format(result))
    
    if st.button("About"):
        st.text("Made With Streamlit")


if __name__ == '__main__':
    main()
