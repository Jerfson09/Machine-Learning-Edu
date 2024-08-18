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

    Studentid = st.number_input("Student Id", value=0 )
    Absence= st.number_input("Absence", value=0 )
    Suspended= st.number_input("Suspended", value=0 )
    Previous_Year_Final_Score = st.number_input("Previous Year Final Scoree", value=0.00 )
    Diagnostic = st.number_input("Disagnostic", value=0.00)
    Quarter_1_Assessment_1 = st.number_input("Quarter 1 Assessment 1", value=0.00 )
    Quarter_1_Assessment_2 = st.number_input("Quarter 1 Assessment 2", value=0.00)
    Quarter_1_Assessment_3 = st.number_input("Quarter 1 Assessment 3", value=0.00 )
    Quarter_1_Assessment_4 = st.number_input("Quarter 1 Assessment 4", value=0.00)
    Quarter_1_Assessment_5 = st.number_input("Quarter 1 Assessment 5", value=0.00 )
    Quarter_2_Assessment_1 = st.number_input("Quarter 2 Assessment 1", value=0.00 )
    Quarter_2_Assessment_2 = st.number_input("Quarter 2 Assessment 2", value=0.00)
    Quarter_2_Assessment_3 = st.number_input("Quarter 2 Assessment 3", value=0.00 )
    Quarter_2_Assessment_4 = st.number_input("Quarter 2 Assessment 4", value=0.00)
    Quarter_2_Assessment_5= st.number_input("Quarter 2 Assessment 5", value=0.00 )
    Quarter_1_Grade = st.number_input("Quarter 1 Grade", value=0 )
    Quarter_2_Grade = st.number_input("Quarter 2 Grade", value=0)

    
 

 

    if st.button("predict"): 
        result = predict(np.array([[int(Studentid),int(Absence), int(Suspended),int(Previous_Year_Final_Score), int(Diagnostic), int(Quarter_1_Assessment_1), int(Quarter_1_Assessment_2),
                                  int(Quarter_1_Assessment_3), int(Quarter_1_Assessment_4), int(Quarter_1_Assessment_5), int(Quarter_2_Assessment_1), int(Quarter_2_Assessment_2),
                                    int(Quarter_2_Assessment_3), int(Quarter_2_Assessment_4), int(Quarter_2_Assessment_5), int(Quarter_1_Grade), int(Quarter_2_Grade)]]))
        st.text(result[0])




if __name__ == "__main__":
    main()