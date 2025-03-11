import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

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


html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ทำนายข้อมูล</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

A1 = st.number_input("ข้อมูล 1")
A2 = st.number_input("ข้อมูล 2")
A3 = st.number_input("ข้อมูล 3")  
A4 = st.number_input("ข้อมูล 4")
A5 = st.number_input("ข้อมูล 5")
A6 = st.number_input("ข้อมูล 6")
A7 = st.number_input("ข้อมูล 7")
A8 = st.number_input("ข้อมูล 8")
A9 = st.number_input("ข้อมูล 9")
A10 = st.number_input("ข้อมูล 10")
A11 = st.number_input("ข้อมูล 11")



if st.button("ทำนายผล"):
    #st.write("ทำนาย")
   dt = pd.read_csv("./data/iris-3.csv") 
   X = dt.drop('HeartDisease', axis=1)
   y = dt.variety   

   Knn_model = KNeighborsClassifier(n_neighbors=3)
   Knn_model.fit(X, y)  
    
   x_input = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11]])
   st.write(Knn_model.predict(x_input))
   
   out=Knn_model.predict(x_input)

   if out[0] == 'Setosa':
    st.image("./img/one.jpg")
   elif out[0] == 'Setosa':
    st.image("./img/two.jpg")
 
else:
    st.write("ไม่ทำนาย")