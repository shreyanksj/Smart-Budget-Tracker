import streamlit as st
import pandas as pd
from data_cleaning import clean_data  # Remove 'src.' prefix
from classification import classify_transaction
from export_to_excel import export_to_excel

st.title("Smart Budget Tracker")

st.sidebar.header("Upload Transaction Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    data = pd.read_csv(uploaded_file)
    
    # Display the raw data
    st.subheader("Raw Transaction Data")
    st.write(data)

    # Clean the data
    cleaned_data = clean_data(data)  # Update function name
    st.subheader("Cleaned Transaction Data")
    st.write(cleaned_data)

    # Classify transactions
    classified_data = classify_transaction(cleaned_data)
    st.subheader("Classified Transaction Data")
    st.write(classified_data)

    # Export to Excel
    if st.button("Export to Excel"):
        export_to_excel(classified_data)
        st.success("Data exported successfully!")

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(classified_data.describe())