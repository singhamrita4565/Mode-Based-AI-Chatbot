from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

model = ChatMistralAI(model="mistral-small-2603")

st.set_page_config(
    page_title="Mode Based AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#4F8BF9;'>
        🤖 Mode Based AI Chatbot
    </h1>

    <p style='text-align:center;font-size:18px;'>
        Choose your AI personality and start chatting
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------------- Personality ----------------

choice = st.selectbox(
    "Choose AI Personality",
    (
        "😡 Angry AI",
        "😂 Funny AI",
        "😢 Sad AI",
    )
)

if choice == "😡 Angry AI":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == "😂 Funny AI":
    mode = "You are a funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a sad AI agent. You respond emotionally and sadly."


# ---------------- Session ----------------

if (
    "messages" not in st.session_state
    or st.session_state.get("mode") != choice
):

    st.session_state.mode = choice

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]


# ---------------- Reset ----------------

if st.button("🔄 Reset Chat"):

    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

    st.rerun()


st.divider()


# ---------------- Chat History ----------------

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user", avatar="🧑"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)


# ---------------- Input ----------------

prompt = st.chat_input("Type your message...")

if prompt:

    if prompt == "0":
        st.stop()

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):

        response = model.invoke(
            st.session_state.messages
        )

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response.content)
        