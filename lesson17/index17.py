import streamlit as st

"""col1, col2, col3, col4 = st.columns(4, gap='small')

with col1:
    st.header("Column1")
    st.write("this is content of col 1")

with col2:
    st.header("Column2")
    st.write("this is content of col 2")

with col3:
    st.header("Column3")
    st.write("this is content of col 3")

with col4:
    st.header("Column4")
    st.write("this is content of col 4")"""



with st.form("my_form", clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age', min_value=0, max_value=100)
    email = st.text_input('Email')
    biography = st.text_area('Short bio')
    terms = st.checkbox('I agree to the terms and conditions')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name:{name}")
    st.write(f"Age:{age}")
    st.write(f"Email:{email}")
    st.write(f"Short Bio:{biography}")

    if terms :
        st.write("Your agreed to the terms and conditions !")
    else:
        st.write('You did not agree to the terms and conditions!')


tab1, tab2, tab3 =st.tabs(["Tab1", "Tab2", "Tab3", ])


with tab1:
    st.header("Column1")
    st.write("column1")

with tab2:
    st.header("Column2")
    st.write("column2")

with tab3:
    st.header("Column3")
    st.write("column3")





















