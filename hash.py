# hash.py
import streamlit as st

def display_hash():
    st.header("Hash Function")
    st.write("This section explains and demonstrates how a hash function works.")
    # Add your hash-related code or logic here
    data = st.text_input("Enter data to hash:")
    if data:
        import hashlib
        hash_result = hashlib.sha256(data.encode()).hexdigest()
        st.write(f"SHA-256 Hash: `{hash_result}`")
