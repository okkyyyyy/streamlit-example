import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="to-do list",
    page_icon="✋",
)

st.title("to do list")
menu = ["Create","Read","Update","Delete","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create":
    st.subheader("Add Items")

#Layout
col1,col2 = st.beta_columns(2)

with col1:
    task = st.text_area("Task To Do")

with col2: 
    task_status = st.selectbox("Status")
    task_due_date = st.date_input("Due Date")
                                

