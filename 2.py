import streamlit as st
import pandas as pd
import numpy as np

st.title("図形描画")

st.write("## 1. 折れ線グラフ")
dataWave = pd.DataFrame(
    {
        "x": np.arange(0, 10, 0.1),
        "sin": np.sin(np.arange(0, 10, 0.1)),
        "cos": np.cos(np.arange(0, 10, 0.1)),
        "tan": np.tan(np.arange(0, 10, 0.1)),
    }
)
st.line_chart(dataWave)
