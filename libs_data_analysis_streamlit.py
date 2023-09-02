
import streamlit as st
import pandas as pd

# Function to import data (adapted from the original code)
def import_data():
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Imported Successfully")
        st.write(df)
        return df

# Streamlit App
def main():
    st.title("LIBS Data Analysis")
    
    st.sidebar.header("Menu")
    if st.sidebar.button("Import Data"):
        import_data()

if __name__ == "__main__":
    main()
