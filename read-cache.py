import pandas as pd
import streamlit as st

st.title("streamlit con cache")

DATA_URL = "Ddataset.csv"

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text("Loading data...")
data = load_data(13)
data_load_state.text("Done ! (using st.cache)") 

st.dataframe(data)



