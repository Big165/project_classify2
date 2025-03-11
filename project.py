import streamlit as st
import pandas as pd

st.title("คูณเป็นโรคหัวใจรึเปล่า")

st.image('project_classify2/img/three.jpg')
st.subheader("Kairung Hengpraprohm")

dt=pd.read_csv('project_classify2/data/heart.csv')
st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write('ผลรวม')
