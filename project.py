import streamlit as st
import pandas as pd

st.title("คูณเป็นโรคหัวใจรึเปล่า")

st.image('./img/three.jpg')
st.subheader("Kairung Hengpraprohm")

dt=pd.read_csv('./data/heart.csv')
st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")
st.write('ผลรวม')

count_male = dt.groupby('Sex').size()[1]
count_female = dt.groupby('Sex').size()[0]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)
