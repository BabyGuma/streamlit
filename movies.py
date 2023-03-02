import pandas as pd
import streamlit as st
from PIL import Image 

st.title('Netflix App')

DATA_URL=('movies.csv')

st.sidebar.image("angel.jpeg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data
def load_data_byname(name):

    data = pd.read_csv(DATA_URL,index_col=0, encoding='latin-1')
    filtered_data_byname = data[data['name'].str.contains(name)]
    return filtered_data_byname

def load_data_bydirector(director):
    data = pd.read_csv(DATA_URL, index_col=0, encoding='latin-1')
    filtered_data_bysex = data[data[ 'director' ] == director]

    return filtered_data_bysex

data_load_state = st.text('Nombre: Angel Guarneros Maldonado')
data_load_state = st.text('Matricula: zS20020316')
data_load_state = st.text('Experiencia educativa: Ingenieria en software')
data = load_data(500)
st.header("Todos los filmes")


sidebar = st.sidebar
agree = sidebar.checkbox("Mostrar todos los filmes")
if agree:
    
  st.dataframe(data.lower)

myname = sidebar.text_input('Titulo del filme :')
btnRange = sidebar.button('Buscar filmes')

if (myname):
    if (btnRange):
        filterbyname = load_data_byname(myname)
        count_row = filterbyname.shape[0]
        st.write(f"Buscar filmes : {count_row}")
        st.dataframe(filterbyname)


selected_director = sidebar.selectbox("Seleccionar director: ", data ['director'].unique())
btnFilterbyDirector = sidebar.button('Filtrar director')

if (btnFilterbyDirector):
    filterbyDirector = load_data_bydirector(selected_director)
    count_row = filterbyDirector.shape[0]
    st.write(f"Total items : {count_row}")
    st.dataframe(filterbyDirector)


