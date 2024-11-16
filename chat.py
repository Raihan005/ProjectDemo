import streamlit as st
import random
import time
import pathlib

# Function to load CSS from file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
css_path = pathlib.Path("styles.css")
load_css(css_path)

# Check if we are on the chat page
if st.session_state.page == "chat":
    st.title("What brings you in today?")
    st.sidebar.success("Change Personality")

    # Options for personalities, add the selected personality
    personalities = [
        "Kanye West",
        "Gordon Ramsay",
        "Dwayne Johnson",
        "Kevin Hart",
        "Cat",
        "Steve Harley"
    ]

    # Use selected personality from the previous page
    selected_personality = st.session_state.selected_personality

    # Custom button using HTML
    st.sidebar.write(f"You selected: **{selected_personality}**")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Streamed response emulator
        def response_generator():
            response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            for word in response.split():
                yield word + " "
                time.sleep(0.05)

        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear the sidebar content to mimic closing it
