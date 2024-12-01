import streamlit as st
from hash import display_hash
from block import display_block
from blockchain import create_block

# Set Streamlit page configuration
st.set_page_config(page_title="Blockchain Demo", layout="wide")

# Title and navigation bar setup
st.title("Blockchain Demo")

# Navigation menu
menu = st.radio(
    "Navigation",
    options=["Hash", "Block", "Blockchain", "Distributed", "Tokens", "Coinbase"],
    horizontal=True,  # To display buttons horizontally
)

# Store the blockchain (a list of blocks)
blockchain = []

# Function to create a new block and add it to the blockchain
def create_and_add_block(previous_hash, block_number, data, nonce):
    new_block = create_block(previous_hash, block_number, data, nonce)
    blockchain.append(new_block)

# Display content based on selected menu item
if menu == "Hash":
    st.header("Hash Function")
    st.write("""
        A hash function takes an input and returns a fixed-size string of characters, which is typically a hash value.
        In the case of blockchain, the hash function is used to ensure data integrity and to link blocks in the chain.
    """)
    display_hash()  # Call the function from hash.py

elif menu == "Block":
    st.header("Block Creation")
    st.write("""
        A block in the blockchain consists of three main components:
        1. Data: Information that is stored within the block.
        2. Previous Hash: The hash of the previous block in the chain.
        3. Hash: A unique identifier for the block created by the hash function.
    """)
    display_block()  # Call the function from block.py

elif menu == "Blockchain":
    st.header("Blockchain Creation")
    st.write("""
        A blockchain is a chain of blocks, each containing data and linked to the previous block using a hash function.
        The blockchain ensures data integrity and transparency, with each block being immutable once added.
    """)

    # User inputs for creating a new block
    previous_hash = st.text_input("Previous Hash", "0")  # Genesis block's previous hash is "0"
    block_number = len(blockchain) + 1
    data = st.text_input("Block Data", "Sample Data")  # Input for the block data (e.g., "Genesis Block")
    nonce = st.number_input("Nonce", min_value=0, value=12345)  # Input for the nonce

    if st.button("Create Block"):
        create_and_add_block(previous_hash, block_number, data, nonce)
        st.success(f"Block {block_number} added to the blockchain!")

    # Display the blockchain
    st.write("### Blockchain:")
    for block in blockchain:
        st.write(f"Block {block['block_number']} - Hash: {block['hash']}")
        st.write(f"Data: {block['data']}")
        st.write(f"Previous Hash: {block['previous_hash']}")
        st.write(f"Nonce: {block['nonce']}")
        st.write("-" * 40)

elif menu == "Distributed":
    st.header("Distributed Blockchain")
    st.write("""
        A distributed blockchain is a decentralized ledger that is maintained by multiple 
        nodes (computers) across the globe. This structure ensures that the data is secure, 
        immutable, and transparent, as no single entity has control over the entire blockchain.
    """)
    st.write("""
        In a distributed blockchain, each participant has a copy of the blockchain, 
        and every new block is verified by the network. This prevents tampering and ensures consensus.
    """)

elif menu == "Tokens":
    st.header("Blockchain Tokens")
    st.write("""
        Tokens in blockchain are digital assets that can represent various forms of value, 
        such as currency (cryptocurrencies), ownership rights, or access to services within a blockchain system.
    """)
    st.write("""
        Tokens are typically built on existing blockchain platforms, such as Ethereum, using smart contracts 
        to define their behavior and properties.
    """)

elif menu == "Coinbase":
    st.header("Coinbase Transactions")
    st.write("""
        A coinbase transaction is the first transaction in a block. It's unique because it 
        doesn't have a sender and typically rewards the miner for validating the block.
    """)
    st.write("""
        The miner receives a block reward in the form of new coins, along with any transaction fees included 
        in the block. This process is crucial for the creation of new cryptocurrency units and incentivizes miners.
    """)

# Additional styling for horizontal buttons in navigation bar
st.markdown(
    """
    <style>
    [data-testid="stHorizontalBlock"] {
        gap: 10px;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
