import streamlit as st
import function

todos = function.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo + "\n")
        function.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        st.rerun()

st.text_input(
    label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo"
)
