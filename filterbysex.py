import streamlit as st
import pandas as pd

st.title('Streamlit - Filter by sex')

DATA_URL= ('https://firebasestorage.googleapis.com/v0/b/streamlit-3f062.appspot.com/o/csv%2Fusuario%2Fdataset.csv?alt=media&token=a4bef4bf-05a5-44ef-8a1b-ee57ee867619')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['sex'] == sex]

    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select sex", data['sex'].unique())
btnFiltersex = st.button('Filter by sex')

if (btnFiltersex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0] #Gives number of rows
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbysex)



