import streamlit as st
import pandas as pd

st.title("คูณเป็นโรคหัวใจรึเปล่า")

st.image('./img/three.jpg')
st.subheader("Kairung Hengpraprohm")

dt=pd.read_csv('./data/heart.csv')
st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลโรคหัวใจ")



st.subheader('ข้อมูลแยกตามเพศ')
count_male = dt.groupby('Sex').size()[0]
count_female = dt.groupby('Sex').size()[1]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)


st.subheader('ข้อมูลค่าเฉลี่ยอายุแยกตามเพศ')
average_male_age = dt[dt['Sex'] == 0]['Age'].mean()
average_female_age = dt[dt['Sex'] == 1]['Age'].mean()

dxage = [average_male_age, average_female_age]
dxage2 = pd.DataFrame(dxage, index=["Male", "Female"])
st.bar_chart(dxage2)