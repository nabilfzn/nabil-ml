import streamlit as st

st.title('🐱‍👤 ML Data Penjualan')

st.write('''
Hallo semuanya saya Nabil, disini saya menyediakan 
sebuah website untuk demo melihat perkembangan suatu perusahaan
melalui data penjualannya dari waktu ke waktu
 ''')

st.sidebar.radio
radio = st.sidebar.radio(
    "Choose a shipping method",
    ("Standard (5-15 days)", "Express (2-5 days)")
)