# import streamlit as st
# import pickle
# import pandas as pd

# with open('gender_classification_model.pkl', 'rb') as file:
#     model = pickle.load(file)


# def predict_gender(features):
#     prediction = model.predict([features])
#     return "Male" if prediction[0] == 1 else "Female"

# st.title("Gender Classification Model")

# long_hair = st.number_input("Size of Long Hair:")
# forehead_width_cm = st.number_input("Size of forehead_width_cm:")
# forehead_height_cm = st.number_input("Size of forehead_height_cm:")
# nose_wide = st.number_input("Size of nose_wide:")
# nose_long = st.number_input("Size of nose_long:")
# lips_thin = st.number_input("Size of lips_thin:")
# distance_nose_to_lip_long = st.number_input("Size of distance_nose_to_lip_long:")


# if(st.button("Predict Gender :")):
#     features = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
#     prediction = predict_gender(features)
#     st.write(f"The Predicted Gender is : {prediction}")

import streamlit as st
import pickle
import pandas as pd

with open('gender_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_gender(features):
    prediction = model.predict([features])
    return "Male" if prediction[0] == 1 else "Female"

st.title("Gender Classification Model")

long_hair = st.radio("Does the person have long hair?", ("Yes", "No"))
long_hair = 1 if long_hair == "Yes" else 0

forehead_width_cm = st.slider("Forehead Width (cm)", min_value=10.0, max_value=20.0, step=0.1)
forehead_height_cm = st.slider("Forehead Height (cm)", min_value=5.0, max_value=15.0, step=0.1)

nose_wide = st.radio("Is the nose wide?", ("Yes", "No"))
nose_wide = 1 if nose_wide == "Yes" else 0

nose_long = st.radio("Is the nose long?", ("Yes", "No"))
nose_long = 1 if nose_long == "Yes" else 0

lips_thin = st.radio("Are the lips thin?", ("Yes", "No"))
lips_thin = 1 if lips_thin == "Yes" else 0

distance_nose_to_lip_long = st.radio("distance_nose_to_lip_long?", ("Yes", "No"))
distance_nose_to_lip_long = 1 if distance_nose_to_lip_long == "Yes" else 0


# Predict button and display prediction
if st.button("Predict Gender"):
    features = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
    prediction = predict_gender(features)
    st.write(f"The Predicted Gender is: {prediction}")
