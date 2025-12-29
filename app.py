import streamlit as st
import pandas as pd
# title
st.markdown("<h1 style='color:yellow'> 🎓 Administrative / Management Dashboard</h1>",unsafe_allow_html=True)

# function to clear details
def clear():
    st.session_state["student"]=[]
    st.success("Data clear successfully")
    st.rerun()
    

# Initialize session state
if "student" not in st.session_state:
    st.session_state["student"] = []

if "counter" not in st.session_state:
    st.session_state.counter = 1


st.sidebar.markdown("<h3 style='color:yellow'> Student System </h3>", unsafe_allow_html=True)
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Register", "Manage Records", "About"]
)


if page == "Home":
    st.markdown("---")

    total = len(st.session_state["student"])
    st.metric("Total Students", total)

    st.write("Welcome! Use the sidebar to register and manage students.")



elif page == "Register":
    st.title("📝 Register Student")

    with st.form("register_form", clear_on_submit=True):
        name = st.text_input("Student Name")
        age = st.number_input("Age", min_value=1, step=1)
        course = st.text_input("Course")

        submitted = st.form_submit_button("Register")

    if submitted and name.strip():
        student_id = st.session_state.counter
        st.session_state.counter += 1

        st.session_state["student"].append({
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        })

        st.success("Student registered successfully")

elif page == "Manage Records":
  
    if st.session_state["student"]:
        df = pd.DataFrame(st.session_state["student"])
        st.dataframe(df, use_container_width=True)

        # -------- DELETE SECTION --------
        st.markdown("<h3 style='color:yellow'> Delete Student </h3>", unsafe_allow_html=True)

    
        delete_id = st.selectbox(
            "Select student to delete",
            df["id"].tolist(),
            key="delete_select"
        )

        if st.button("Delete student", key="delete_btn"):
            st.session_state["student"] = [
                s for s in st.session_state["student"] if s["id"] != delete_id
            ]
            st.success("Student deleted successfully")
            st.rerun()

        if st.button("Clear all data", key="clear_btn"):
            clear()

        # -------- EDIT SECTION --------
        st.markdown("<h3 style='color:yellow'> Edit Student </h3>", unsafe_allow_html=True)

        edit_id = st.selectbox(
            "Select student to edit",
            df["id"].tolist(),
            key="edit_select"
        )

        selected_student = next(
            (s for s in st.session_state["student"] if s["id"] == edit_id),
            None
        )

        if selected_student:
            with st.form("Edit_Form"):
                name = st.text_input("Name", value=selected_student["name"])
                age = st.number_input("Age", min_value=1, value=selected_student["age"])
                course = st.text_input("Course", value=selected_student["course"])
                update = st.form_submit_button("Update student")

            if update:
                for s in st.session_state["student"]:
                    if s["id"] == selected_student["id"]:
                        s["name"] = name
                        s["age"] = age
                        s["course"] = course
                        break

                st.success("Student updated successfully")
                st.rerun()



# about section
elif page == "About":
    st.title("ℹ️ About")

    st.write("""
    This Student Registration System was built using **Streamlit**.

    **Features:**
    - Register students
    - View records
    - Delete records
    - Persistent session state

    **Built for learning and real-world practice.**
    """)





    st.markdown(
    "<h3 style='color:orange; border-bottom:2px solid #ccc;'>Developed By Iddrisu Inusah Adelga (Impact)</h3>",
    unsafe_allow_html=True
    )



st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0 • Student Management Dashboard")
