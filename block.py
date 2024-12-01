# block.py
import streamlit as st
import hashlib

def display_block():
    st.header("Block Functionality")
    st.write("This section demonstrates block creation with real-time hash generation.")
    
    # Input fields for block data and nonce
    block_data = st.text_area("Enter Block Data:", placeholder="Type the data for the block here...")
    nonce = st.number_input("Enter Nonce:", min_value=0, step=1, value=0)
    
    # Generate hash in real time
    block_info = f"{block_data}{nonce}"
    block_hash = hashlib.sha256(block_info.encode()).hexdigest()
    
    # Display the dynamically calculated hash
    st.write(f"Block Hash: `{block_hash}`")
