import streamlit as st
import functions

todos = functions.get_todos()

st.title("My app todo")

st.subheader("This is mytodo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
