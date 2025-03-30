import streamlit as st # type: ignore



def length_converter(value , unit_from , unit_to):

    conversions = {
         "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701

    }

    return value * conversions[unit_to] / conversions[unit_from]


def weight_converter(value , unit_from , unit_to):
      
    conversions = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    }

    return value * conversions[unit_to] / conversions[unit_from]


def temperature_converter(value , unit_from , unit_to):
    
    if unit_from == "Celsius" and unit_to == "Fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 9/5
    elif unit_from == "Celsius" and unit_to == "Kelvin":
        return value + 273.15
    elif unit_from == "Kelvin" and unit_to == "Celsius":
        return value - 273.15
    elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    
    return value

  
    

st.title("🔄 Unit Converter")
st.write("Convert between different units of Length, Weight, and Temperature.")

conversion_type = st.radio("Select Conversion Type:", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value to convert: ", min_value=0.0 , step=1.0)

if conversion_type == "Length":
    units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)
    result = length_converter(value, from_unit, to_unit)

elif conversion_type == "Weight":
    units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)
    result = weight_converter(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)
    result = temperature_converter(value, from_unit, to_unit)

st.success(f"Converted Value: {result:.4f} {to_unit}")