
import pandas as pd
import numpy as np
import streamlit as st
import pickle 
# from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('normalized_data')
df = df.drop(['Unnamed: 0'], axis=1)

LOGO_URL_LARGE= "C:/Users/Azri/OneDrive/Desktop/fdm-web-app/logo.jpeg"

st.image(
            LOGO_URL_LARGE 
        )

st.write(""" 
         # Inusra-Care
         ### classify customers at a *crash risk* and predict *premium coverage* estimate 
          
         Project GitHub link [Take me to the Repo](http://www.github.com)\n
         Project Dataset link [Take me to the data source](http://www.kaggle.com)\n
         Project Explainer Vid: [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
 
          """)




#********************************************************************************************************************************************************
#SIDEBAR #


st.sidebar.header('User Input Features')

uploaded_csv = st.sidebar.file_uploader("Uplaod your CSV file", type=["csv"])
if uploaded_csv is not None:
    input_df = pd.read_csv(uploaded_csv)
else:
    def user_input_feature():
        GENDER = st.sidebar.selectbox('Sex',('M','z_F'))
        GEN_AGE = st.sidebar.slider(("Client Age:"),value=[0])
        EDUCATION = st.sidebar.selectbox('Highest educational qualification',('<HighSchool','Bachelors', 'Masters', 'PhD','z_High School'))
        HOMEKIDS = st.sidebar.slider(("How many kids at home:"), value=[0])
        KIDSDRIV = st.sidebar.slider(("How many driving age children curently live with user:"),value=[0])
        OCCUPATION = st.sidebar.selectbox('Client Occupation',('Clerical','Doctor', 'Home Maker', 'Lawyer', 'Manager', 'Professional', 'Student', 'Blue Collar'))
        INCOME = st.sidebar.slider(("Yearly Income:"),value=[0])
        HOME_VAL = st.sidebar.slider(("Home value:"),value=[0])
        URBANICITY = st.sidebar.selectbox('Residencial enviorment:',('Highly Urban/Urban','z_Higly Rural/Rural'))
        MSTATUS = st.sidebar.selectbox("Marital Status:", ('Married','UnMarried'))
        PARENT1 = st.sidebar.selectbox("Is the customer a single parent?",('Yes','No'))
        YOJ = st.sidebar.slider(("Number of years on the current occupation:"),value=[0])
        TIF = st.sidebar.slider(("Time in force:"),value=[0])
        TRAVTIME = st.sidebar.slider(("Trvel time in hours:"),value=[0])
        BLUEBOOK = st.sidebar.slider(("Cost of vehicle (BlueBook):"),value=[0])
        CAR_USE = st.sidebar.selectbox('Vehicle Use Case',('Commercial','Private'))
        CAR_TYPE = st.sidebar.selectbox('Type of vehicle?',('Minivan', 'Panel Truck', 'Pickup','Sports Car', 'Van', 'z_SUV'))
        CAR_AGE = st.sidebar.slider(("Vehicle Age:"),value=[0])
        RED_CAR = st.sidebar.selectbox("Is the clients vehicle red?",('Yes','No'))
        REVOKED = st.sidebar.selectbox("Has the client had their license revoked ?",('Yes','No'))
        OLD_CLAIM = st.sidebar.slider(("Previous Claim amount if any:"),value=[0])
        CLM_FREQ = st.sidebar.slider(("No. of previous claims:"),value=[0])        
        MVR_PTS = st.sidebar.slider(("MVR point:"),value=[0])    
       
        data = {
            'KIDSDRIV': KIDSDRIV,
            'HOMEKIDS': HOMEKIDS,
            'YOJ':  YOJ,
            'INCOME': INCOME,
            'PARENT1':PARENT1, 
            'HOME_VAL': HOME_VAL,
            'MSTATUS': MSTATUS,
            'TRAVTIME': TRAVTIME,
            'BLUEBOOK': BLUEBOOK,
            'TIF':TIF,
            'RED_CAR': RED_CAR,
            'OLDCLAIM': OLD_CLAIM,
            'CLM_FREQ': CLM_FREQ,
            'REVOKED': REVOKED,
            'MVR_PTS': MVR_PTS,
            'CAR_AGE': CAR_AGE,
            'GEN_AGE': GEN_AGE,
            'GENDER': GENDER,
            'EDUCATION': EDUCATION,
            'OCCUPATION': OCCUPATION,
            'CAR_USE': CAR_USE,
            'CAR_TYPE':CAR_TYPE,
            'URBANICITY': URBANICITY}
    
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_feature()

#*********************************************************************************************************************************************************
#ENCODING INPUT VALUES#



# One hot encoding
one_hot_encode = ['GENDER',
                  'EDUCATION',
                  'OCCUPATION',
                  'CAR_USE',
                  'CAR_TYPE',
                  'URBANICITY',
                  ] 
for col in one_hot_encode:
    dummy = pd.get_dummies(input_df[col],prefix=col)
    input_df=pd.concat([input_df,dummy],axis=1)
    del input_df[col]
input_df = input_df[:1]



#Binary encode Marraige Status

mapping = {
    'Married': 1,
    'UnMarried':0
}
input_df['MSTATUS'] = input_df['MSTATUS'].replace(mapping)

#Binary encode PARENT1 (Is the client a single parent)
mapping = {
    'Yes':1,
    'No':0
}
input_df['PARENT1'] = input_df['PARENT1'].replace(mapping)

#Binary encode RED_CAR
mapping = {
    'Yes':1,
    'No':0
}
input_df['RED_CAR'] = input_df['RED_CAR'].replace(mapping)

#Binary encode Revoked (Has the clients license ever been revoked)
mapping = {
    'Yes':1,
    'No':0
}
input_df['REVOKED'] = input_df['REVOKED'].replace(mapping)


#************************************************************************************************************************************************
# Display the features input by the user
st.subheader('User Input features')

if uploaded_csv is not None:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded using example input parameters')
    st.write(input_df)



       

st.write(df)




