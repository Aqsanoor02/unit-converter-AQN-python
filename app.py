import streamlit as st 
from io import BytesIO
from pint import UnitRegistry
import json

st.set_page_config("Unit Converter", layout="wide")
st.markdown(
    """
    <style>
    .stApp{
    background-color:#0f134a
    }
    <\style>

    """,unsafe_allow_html=True
)
st.title("Unit Converter :")

with open("units.json","r") as file:
    unit_data= json.load(file)

all_categories = list(unit_data.keys())

ureg= UnitRegistry()

category = st.selectbox("Select the dimension for unit conversion : ", all_categories)
unit_from = st.selectbox("Convert from", unit_data[category])
unit_to = st.selectbox("Convert to", unit_data[category])


if category =="Temperature":
    value = float(st.number_input("Enter a value : ",format="%.4f"))
else:
    value = float(st.number_input("Enter a value : ",min_value=0.0, format="%.4f"))


try:
    if category =="Temperature":
        input_value= ureg.Quantity(value,unit_from)
        output_value = input_value.to(unit_to)
    
    else:
        input_value= value*ureg(unit_from)
        output_value = input_value.to(unit_to)
    st.success(f"{value} {unit_from} = {output_value:.4f}")
except Exception as e:
    st.error(f"Conversion failed : {e}")
