import streamlit as st
import requests

st.title("Aplikasi Pengecekan Kelulusan Siswa")
code_module = st.selectbox("Code Module", ['BBB' ,'EEE', 'AAA', 'FFF' ,'DDD' ,'GGG' ,'CCC'])
code_presentation = st.selectbox("Code Presentation",['2013J', '2014J' ,'2014B' ,'2013B'])
gender = st.selectbox("Gender",['M', 'F'])
highest_education = st.selectbox("Highest Education", ['A Level or Equivalent', 'Lower Than A Level' ,'HE Qualification',
 'No Formal quals'])
imd_band = st.selectbox('IMD Band',['80-90%', '30-40%', '50-60%' ,'70-80%' ,'10-20' ,'60-70%' ,'90-100%' ,'0-10%',
 '40-50%' ,'20-30%'])
age_band = st.selectbox("Age Band", ['35-55', '0-35', '55<='])
num_of_prev_attempts = st.number_input("Previous Attempts")
studied_credits = st.number_input('Studied Credits')
disability = st.selectbox("Disability",['Y','N'])

# inference
data = {'codeModule':code_module,
        'codePresentation':code_presentation,
        'Gender': gender,
        'highestEducation':highest_education,
        'imdBand':imd_band,
        'ageBand':age_band,
        'numOfPrevAttempts':num_of_prev_attempts,
        'studiedCredits':studied_credits,
        'Disability': disability}

URL = "http://127.0.0.1:5000/predict" # sebelum push backend
# URL = "https://afif-deployment-backend.herokuapp.com/predict" # setelah push backend

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['class_name'])
elif r.status_code == 400:
    st.title("ERROR BOSS")
    st.write(res['message'])