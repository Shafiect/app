import streamlit as st
st.set_page_config(page_title="Finding Largest Number",layout='wide')
with st.container():
    st.subheader(" Hi , This is my Week 8 Tools in Data Science project ")
    st.title(" Large Number finder ")
    st.write(" Please insert 3 number in the following boxes ")
with st.container():
    num1=st.number_input(" NUM 1 ")
    num2=st.number_input(" NUM 2 ")
    num3=st.number_input(" NUM 3 ")
maxi=num1
if(num2>maxi):
    maxi=num2
if(num3>maxi):
    maxi=num3
with st.container():
    st.subheader(" The largest Number is ")
    st.write(maxi)
