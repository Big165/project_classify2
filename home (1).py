import streamlit as st
import pandas as pd

st.title("คูณเป็นโรคหัวใจรึเปล่า")

st.image('./img/3.jpg')
st.subheader("Kairung Hengpraprohm")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write('ผลรวม')
