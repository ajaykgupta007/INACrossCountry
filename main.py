import streamlit as st
import pandas as pd
import time
import os

# Path to the dynamic file
file_path = 'dynamic_data.csv'

# Function to read data from the file
def read_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

# Function to watch file changes
def watch_file(file_path, last_mod_time):
    if os.path.exists(file_path):
        mod_time = os.path.getmtime(file_path)
        if mod_time != last_mod_time:
            return mod_time
    return last_mod_time

# Title
st.title("Real-Time File Upload and Display")

# Placeholder for the table
table_placeholder = st.empty()

# Initial file modification time
last_mod_time = None

# Read initial data and display
initial_data = read_data(file_path)
table_placeholder.table(initial_data)

# Interval for updating the table (in seconds)
update_interval = 2

while True:
    last_mod_time = watch_file(file_path, last_mod_time)
    if last_mod_time:
        # Read the updated data and display
        new_data = read_data(file_path)
        table_placeholder.table(new_data)
    time.sleep(update_interval)
    st.experimental_rerun()
