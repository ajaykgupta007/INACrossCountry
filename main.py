import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import time

# Define the page layout
st.set_page_config(page_title="Home Page", layout="wide")

# Load your icons (ensure you have the icons saved in your working directory)
left_icon = Image.open("NavyCrest.png")
right_icon = Image.open("INACrest.png")

# Resize icons to the same size
icon_size = (450, 400)  # Specify the size you want for the icons
left_icon = left_icon.resize((550, 400))
right_icon = right_icon.resize(icon_size)

# Create columns for layout
col1, col2, col3 = st.columns([1, 6, 1])

# Display the left icon in the first column
with col1:
    st.image(left_icon, use_column_width=True)

# Display the main content in the second column
with col2:
    st.title("Welcome to Indian Naval Academy")

# Display the right icon in the third column
with col3:
    st.image(right_icon, use_column_width=True)

st.title("Cross Country - Autumn Term 2024")

# Function to generate random data
def generate_data():
    data = {
        'Rank': np.random.randint(1, 100, 10),
        'Chest Number': np.random.random(10),
        'Name': np.random.choice(['A', 'B', 'C', 'D'], 10)
    }
    return pd.DataFrame(data)


def generate_runner_positions(num_runners):
    data = {
        'Runner': [f'Runner {i+1}' for i in range(num_runners)],
        'Position': np.random.randint(1, 101, num_runners),
        'Distance Covered (km)': np.round(np.random.uniform(0, 10, num_runners), 2)
    }
    return pd.DataFrame(data).sort_values(by='Position')

# Number of runners
num_runners = 10

# Title
st.header("Real-Time Updates of Cross Country Runners' Positions")

# Placeholder for the table
table_placeholder = st.empty()

# Interval for updating the table (in seconds)
update_interval = 5

while True:
    # Generate new positions data
    df = generate_runner_positions(num_runners)
    
    # Display the updated table
    with table_placeholder.container():
        st.table(df)
    
    # Wait for the specified interval
    time.sleep(update_interval)
