import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(10000, 5),
     columns=['a', 'b', 'c', 'd', 'e'])

st.line_chart(chart_data)
st.dataframe(chart_data)

import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(5, 2) / [50, 50] + [18.834444, -97.151667],
    columns=['lat', 'lon'])

st.map(map_data)

import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)