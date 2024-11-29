import hashlib
import streamlit as st

# Function to create a block
def create_block(block_number, data, nonce, previous_hash):
    block = {
        'block_number': block_number,
        'data': data,
        'nonce': nonce,
        'previous_hash': previous_hash,
        'hash': hashlib.sha256(f'{block_number}{data}{nonce}{previous_hash}'.encode()).hexdigest()
    }
    return block

# Function to add block to blockchain
def add_block_to_chain(data, nonce):
    # Get the previous block's hash
    previous_hash = '0' * 64 if len(st.session_state.blockchain) == 0 else st.session_state.blockchain[-1]['hash']
    
    # Create a new block
    block = create_block(len(st.session_state.blockchain) + 1, data, nonce, previous_hash)
    
    # Append the new block to the blockchain
    st.session_state.blockchain.append(block)

# Streamlit setup for session state blockchain
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = []

# Layout for buttons
col1, col2, col3 = st.columns(3)  # Three columns

# Create a button for "Hash Value"
with col1:
    if st.button("Hash Value"):
        st.session_state.show_hash = True
        st.session_state.show_block = False
        st.session_state.show_blockchain = False

# Create a button for "Single Block"
with col2:
    if st.button("Single Block"):
        st.session_state.show_block = True
        st.session_state.show_hash = False
        st.session_state.show_blockchain = False

# Create a button for "Blockchain"
with col3:
    if st.button("Blockchain"):
        st.session_state.show_blockchain = True
        st.session_state.show_hash = False
        st.session_state.show_block = False

# Show Hash Value input and calculation
if st.session_state.get("show_hash", False):
    data_input = st.text_area("Enter Data for Hash Calculation:", key="data_input")

    if data_input:
        hash_value = hashlib.sha256(data_input.encode()).hexdigest()  # Default nonce is 0 for now
        st.write("**Hash Value:**", hash_value)
    else:
        st.write("**Hash Value:** No data entered")

# Show Single Block input for adding a block
if st.session_state.get("show_block", False):
    # Block data input
    block_data = st.text_area("Enter Block Data:", key="block_data")
    
    # Nonce value input
    nonce_input = st.number_input("Enter Nonce Value:", min_value=0, key="nonce_input")

    # Displaying block data, nonce, and hash live
    if block_data and nonce_input is not None:
        block_hash = hashlib.sha256(f'{block_data}{nonce_input}'.encode()).hexdigest()
        st.session_state.block_data = block_data
        st.session_state.block_nonce = nonce_input
        st.session_state.block_hash = block_hash

        st.write(f"**Block Data:** {st.session_state.block_data}")
        st.write(f"**Nonce:** {st.session_state.block_nonce}")
        st.write(f"**Block Hash:** {st.session_state.block_hash}")

        # Button to add block to blockchain
        if st.button("Add Block to Blockchain"):
            add_block_to_chain(st.session_state.block_data, st.session_state.block_nonce)
            st.success("Block added to blockchain!")
    else:
        st.write("**Block Data:** No data entered")

# Show Blockchain input and display blocks
if st.session_state.get("show_blockchain", False):


    # Block Data Input for 4 Blocks
    for i in range(1, 5):  # Loop through blocks 1 to 4
        st.subheader(f"Block {i}")
        block_data = st.text_input(f"Enter Data for Block {i}:")
        nonce_input = st.text_input(f"Nonce for Block {i}:")

        # Button to update hash for the current block
        if st.button(f"Update Hash for Block {i}"):
            if block_data and nonce_input:
                add_block_to_chain(block_data, nonce_input)
            else:
                st.error(f"Please enter both data and nonce for Block {i}")

    # Button to show blockchain
    if st.button("Show Blockchain"):
        st.subheader("Blockchain (Interconnected Blocks)")

        # Loop through each block in the blockchain and display details inside text area
        for block in st.session_state.blockchain:
            block_details = f"""
            **Block Number (BN):** {block['block_number']}
            **Block Data:** {block['data']}
            **Nonce:** {block['nonce']}
            **Previous Hash (PH):** {block['previous_hash']}
            **Block Hash:** {block['hash']}
            """
            st.text_area(f"Block {block['block_number']} Details", block_details, height=200)
