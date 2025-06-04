import streamlit as st
import pandas as pd
import io

st.title("Merge Same Data in One Cell & Download")

# Upload the file
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.write("Original Data:")
    st.dataframe(df)

    # Select columns to merge duplicates on
    col = st.selectbox("Choose the column to merge same data (remove duplicates by this column)", df.columns)

    # Remove duplicates based on selected column
    merged_df = df.drop_duplicates(subset=[col])
    
    st.write("Data after merging duplicates in column:", col)
    st.dataframe(merged_df)

    # Download button
    csv = merged_df.to_csv(index=False)
    st.download_button(
        label="Download merged data as CSV",
        data=csv.encode('utf-8'),
        file_name='merged_data.csv',
        mime='text/csv',
    )

    st.success("Done! Upload a new file to process again.")
else:
    st.info("Please upload a CSV or Excel file to get started.")