import streamlit as st
from watchdog.observers.fsevents2 import message


def main():
    st.title("Hello World")

if __name__ == '__main__':
    main()



if st.button("Click Me"):
    st.write("Clicker")

    st.checkbox("Check ME")

if st.checkbox("Check for some text"):
    st.write("You are seeing this text because you checked the button!")


user_input = st.text_input('Enter text', "Shkruaj nje text")
st_write("You entered: " , user_input)


age = st.number_input("enter your age" , min_value= 1, max_value= 100)
st.write(f"Your age: {age}")

message = st.text_area ("Enter a message")
st.write(f"Your message: {message}")

choice = st.radio("Choose one: " ['Choice 1, Choice 2, Choice 3'])
st.write(f"You chose , {choice}")


if st.button("Succes"):
    st.succes()

try:
    1/0
except Exception as e:
    st.write(e)