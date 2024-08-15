import numpy as np 
import pandas as pd 

import streamlit as st

from sklearn import preprocessing
# import pickle

from predictions import predict


def main(): 
    st.title("FAST Mid-Year Prediction Scores") 
    html_temp = """

    <div style="background:#2131de ;padding:10px">
    <h2 style="color:white;text-align:center;">FAST Mid-Year Prediction Scores</h2>
    </div>

    """

    st.markdown(html_temp, unsafe_allow_html=True)

    Studentid = st.text_input("Student Id", "")
    Gender = st.selectbox("Gender", ["M", "F"])
    Tardies = st.text_input("Tardies", "")
    Absence= st.text_input("Absence", "")
    Transfers= st.text_input("Transfers", "")
    Suspended= st.text_input("Suspended", "")
    ESE = st.selectbox("ESE Status", ["Not ESE", "Specific Learning Disability", "Speech Impaired", "Gifted", "Other Health Impaired", "Autistic Spectrum Disorders", "Intellectual Disabilities", "Deaf/Hard of Hearing", "Language Impaired"])
    Teacher= st.text_input("Teacher", "")
    Ethnicity = st.selectbox("Ethnicity", ["African American", "Caucasian", "Hispanic", "Multi-Racial", "Hawaiian / PI", "Other"])
    Previous_Year_Final_Score = st.text_input("Previous Year Final Scoree", "")
    Diagnostic = st.text_input("Disagnostic", "")
    Quarter_1_Assessment_1 = st.text_input("Quarter 1 Assessment 1", "")
    Quarter_1_Assessment_2 = st.text_input("Quarter 1 Assessment 2", "")
    Quarter_1_Assessment_3 = st.text_input("Quarter 1 Assessment 3", "")
    Quarter_1_Assessment_4 = st.text_input("Quarter 1 Assessment 4", "")
    Quarter_1_Assessment_5 = st.text_input("Quarter 1 Assessment 5", "")
    Quarter_2_Assessment_1 = st.text_input("Quarter 2 Assessment 1", "")
    Quarter_2_Assessment_2 = st.text_input("Quarter 2 Assessment 2", "")
    Quarter_2_Assessment_3 = st.text_input("Quarter 2 Assessment 3", "")
    Quarter_2_Assessment_4 = st.text_input("Quarter 2 Assessment 4", "")
    Quarter_2_Assessment_5= st.text_input("Quarter 2 Assessment 5", "")
    Quarter_1_Grade = st.text_input("Quarter 1 Grade", "")
    Quarter_2_Grade = st.text_input("Quarter 2 Grade", "")

    if st.button("predict"): 
        result = predict(np.array([[int(Studentid), str(Gender), str(Tardies), int(Absence),str(Transfers),int(Suspended),str(ESE),str(Teacher),str(Ethnicity),
                                    int(Previous_Year_Final_Score), int(Diagnostic), int(Quarter_1_Assessment_1), int(Quarter_1_Assessment_2), int(Quarter_1_Assessment_2),
                                    int(Quarter_1_Assessment_3), int(Quarter_1_Assessment_4), int(Quarter_1_Assessment_5), int(Quarter_2_Assessment_1), int(Quarter_2_Assessment_2),
                                    int(Quarter_2_Assessment_3), int(Quarter_2_Assessment_4), int(Quarter_2_Assessment_5), int(Quarter_1_Grade), int(Quarter_2_Grade)]]))
        st.text(result[0])




if __name__ == "__main__":
    main()