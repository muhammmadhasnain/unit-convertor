import streamlit as st



def unit_convertor(value , unit_from , unit_to):

    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters" : 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000

    }

    key = f"{unit_from}_{unit_to}"

    for key in conversions:
        conversion = conversions[key]
        return value * conversion
    else: 
        return "value not supported"
    

st.title("Unit Convertor")
value = st.number_input("Enter the value: ", min_value=1.0 , step=1.0)

unit_from = st.selectbox("Convert from: ", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to: ", ["meters", "kilometers", "grams", "kilograms"])


if st.button("convert"):
    result = unit_convertor(value , unit_from , unit_to)
    st.write(f"converted value: {result}")