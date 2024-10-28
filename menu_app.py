import streamlit as st
import panda as pd

st.set_page_config(page_title="Meu site")

with st.container():
    st.write("Meu primeiro site com streamlite")
    st.title("Dashboards de contrator")
    st.write("Informações sobre os contratos fechados pela empresa ao longo do ano")

with st.container():
    st.write("---")
    dados = pd.read_csv("resultados.csv")
    st.area_char(dados, x="Data", y="Contratos")