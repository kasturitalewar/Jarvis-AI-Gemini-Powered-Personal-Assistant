import streamlit as st
from gemini import chat_with_gemini

st.set_page_config(
    page_title="Jarvis",
    page_icon="🤖"
)

st.title("🤖 Jarvis AI Assistant")
st.write("Your Personal AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! My name is Jarvis. How may I help you?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask Jarvis anything...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response = chat_with_gemini(user_input)
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })