import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Hello World")

st.title("dataTable")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

st.write(df)

char_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.title("line chart")
st.line_chart(char_data)

st.title("area chart")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(map_data)

st.title("checkbox")

df = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
    }
)

option = st.sidebar.selectbox("Which number do you like best?", df["first column"])

st.write("You selected:", option)


st.write("Starting a long computation...")

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

st.write("...and now we're done!")
