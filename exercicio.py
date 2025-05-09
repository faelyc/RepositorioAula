import streamlit as st
import pandas as pd
import numpy as np

st.title("Produção de recicláveis no Brasil conforme o Atlas Brasileiro da Reciclagem")

data = pd.read_excel("dados.xlsx")

data['Ano'] = ['2020', '2021', '2022']

print(data)

data['Toneladas'] = ['907.934,20', '585.979,90', '758.444,08']

print(data)

st.line_chart(data)

