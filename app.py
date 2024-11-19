import streamlit as st
import pickle
import numpy as np
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
st.markdown(" # House Price Predictor #")
st.subheader("This Website Predict the approxmiate price of House.")
AREA=st.number_input("Enter the Area:",key="input1")
INT_SQFT=st.number_input("Enter the Total_SQFT:",key="input2")
DIST_MAINROAD=st.number_input("Enter the DIST_FROM_MAINROAD:",key="input3")
N_BEDROOM=st.number_input("Enter the No_of_BEDROOM:",key="input4")
N_BATHROOM=st.number_input("Enter the No_of_BATHROOM:",key="input5")
N_ROOM=st.number_input("Enter the No_of_ROOM:",key="input6")
PARK_FACIL=st.selectbox("Enter the PARK_FACILITY:",options=("0.0","1"),key="input7")
BUILDTYPE=st.selectbox("Enter the BUILDTYPE:",options=("0.0","1","2"),key="input8")
QS_ROOMS=st.number_input("Enter the QS_ROOMS:")
QS_BATHROOM=st.number_input("Enter the QS_BATHROOM:")
QS_BEDROOM=st.number_input("Enter the QS_BEDROOM:")
QS_OVERALL=st.number_input("Enter the QS_OVERALL:")
REG_FEE=st.number_input("Enter the REG_FEE:")
COMMIS=st.number_input("Enter the COMMIS:")
SALE_YEAR=st.number_input("Enter the SALE_YEAR:")

SALE_MONTH=st.number_input("Enter the SALE_MONTH:")
BUILD_YEAR=st.number_input("Enter the BUILD_YEAR:")
BUILD_AGE=st.number_input("Enter the BUILD_AGE:")
if st.button("Predict"):
    query=np.array([[AREA,INT_SQFT,DIST_MAINROAD,N_BEDROOM,N_BATHROOM,N_ROOM,PARK_FACIL,BUILDTYPE,QS_ROOMS,QS_BATHROOM,QS_BEDROOM,QS_OVERALL,REG_FEE,COMMIS,SALE_YEAR,SALE_MONTH,BUILD_YEAR,BUILD_AGE]])
    
    if np.all(query=='0.0'):
        st.write(" # Enter the valid value please! #")
    else:
        st.title("The Predicted Price Of House is:"+str(float((pipe.predict(query)[0]))))
