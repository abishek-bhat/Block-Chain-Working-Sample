import hashlib
import streamlit as st

# Function to calculate hash based on data input
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Streamlit Layout
st.title("Blockchain Hash Value Simulator")

# Input field to accept data, and hash gets updated dynamically
data_input = st.text_area("Enter Data:", key="data_input")

# If the data is not empty, calculate and display the hash
if data_input:
    hash_value = calculate_hash(data_input)
    st.write("**Hash Value:**", hash_value)
else:
    st.write("**Hash Value:** No data entered")
