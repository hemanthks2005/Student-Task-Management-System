import streamlit as st

st.title(" Student Task Management System")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "done": False})
        st.success("Task added!")

st.subheader("Your Tasks")

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4,1])
    
    with col1:
        if t["done"]:
            st.write(f"~~{t['task']}~~")
        else:
            st.write(t["task"])
    
    with col2:
        if st.button("Done", key=i):
            st.session_state.tasks[i]["done"] = True