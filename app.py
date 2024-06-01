import streamlit as st
import json

def load_tasks():
   try:
       with open('tasks.json', 'r') as f:
           return json.load(f)
   except FileNotFoundError:
       return []

def save_tasks(tasks):
   with open('tasks.json', 'w') as f:
       json.dump(tasks, f)

st.set_page_config(page_title="To-Do List", layout="wide")

st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .stButton button {
        width: 100%;
        margin-bottom: 10px;
    }
    .stTextInput input {
        width: 100%;
    }
    .stCheckbox div {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("To-Do List App")

tasks = load_tasks()

new_task = st.text_input("New Task")
if st.button("Add Task"):
   if new_task:
       tasks.append({"task": new_task, "completed": False})
       save_tasks(tasks)
       st.experimental_rerun()

for idx, task in enumerate(tasks):
   col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
   with col1:
       if task['completed']:
           st.text(f"✔️ {task['task']}")
       else:
           st.text(task['task'])
   with col2:
       if st.button("Edit", key=f"edit{idx}"):
           edited_task = st.text_input("Edit Task", value=task['task'])
           if st.button("Save", key=f"save{idx}"):
               tasks[idx]['task'] = edited_task
               save_tasks(tasks)
               st.experimental_rerun()
   with col3:
       if st.button("Delete", key=f"delete{idx}"):
           del tasks[idx]
           save_tasks(tasks)
           st.experimental_rerun()
   col4, col5 = st.columns([0.8, 0.2])
   with col5:
       if st.checkbox("Completed", value=task['completed'], key=f"complete{idx}"):
           tasks[idx]['completed'] = not task['completed']
           save_tasks(tasks)
           st.experimental_rerun()
