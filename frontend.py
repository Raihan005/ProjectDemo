import streamlit as st
from sample import cat
import random
import time
import pathlib
from Main import *
key = ""
msg = ""
# Function to load CSS from file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file for chat page
css_path = pathlib.Path("styles.css")

# Check if page state exists in session state, otherwise initialize it
if "page" not in st.session_state:
    st.session_state.page = "selection"  # Start on selection page

# Page for selecting personality
if st.session_state.page == "selection":
    # Custom CSS to style the cards, layout, and buttons
    custom_css = """
    <style>
    input:placeholder{
        color:white;
        opacity:1
    }
    .title-style {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 25px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
    .button-55 {
        align-self: center;
        background-color: #fff;
        border-radius: 15px;
        border-style: solid;
        border-width: 2px;
        box-shadow: rgba(0, 0, 0, 0.2) 15px 28px 25px -18px;
        color: #;
        cursor: pointer;
        display: inline-block;
        font-family: Neucha, sans-serif;
        font-size: 1rem;
        line-height: 23px;
        outline: none;
        padding: 0.75rem;
        text-decoration: none;
        transition: all 235ms ease-in-out;
        width: 100%;
        text-align: center;
        margin-top: 10px;
    }
    .button-55:hover {
        box-shadow: rgba(0, 0, 0, 0.3) 2px 8px 8px -5px;
        transform: translate3d(0, 2px, 0);
    }
    input {
        color: red;  /* Set text color */
        background-color: #333; /* Set input background color for contrast */
        border: 1px solid #444; /* Optional: Add border */
        padding: 10px; /* Optional: Add some padding */
        border-radius: 5px; /* Optional: Add border radius */
    }
    input::placeholder {
        color: white; /* Change placeholder color */
    }
</style>
    """
    
    # Inject the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Set the title of the app with a styled class
    st.markdown('<div class="title-style">Yo, what\'s up? Pick your vibe, let\'s get this therapy session started!</div>', unsafe_allow_html=True)

    # Define the card data
    cards = [
        {"title": "Kanye West", "image": "kanye.png"},
        {"title": "Cat", "image": "cat.jpg"},
        {"title": "Gordon ", "image": "gorden.jpg"},
        {"title": "Steven He", "image": "steven.jpeg"},
    ]

    # Create columns for the cards to appear in the same row
    cols = st.columns(len(cards))

# Display each card in its own column
    for i, card_data in enumerate(cards):
        with cols[i]:
            st.image(card_data["image"], use_column_width=True)
            st.markdown(f"<div class='card-title'>{card_data['title']}</div>", unsafe_allow_html=True)

        # Add a button for selecting personality
            
            if st.button("Select", key=f"select_{i}"):  # Use st.button instead of injected HTML
                st.session_state.selected_personality = card_data["title"]

# Check if a personality has been selected
    if "selected_personality" in st.session_state:
        st.write(f"You selected: {st.session_state.selected_personality}")
    else:
        st.warning("Please select a personality.")

    # Add a "Next" button to proceed
    if st.button("Next"):
        if "selected_personality" in st.session_state:
            st.success(f"You are now proceeding with: {st.session_state.selected_personality}")
            st.session_state.page = "chat"  # Navigate to chat page
        else:
            st.warning("Please select a personality before proceeding.")


# Chat page
elif st.session_state.page == "chat":
    load_css(css_path)  # Load CSS for the chat page
    st.title("What brings you in today?")
    
    # Sidebar buttons
    st.sidebar.button("Home", on_click=lambda: st.session_state.update({"page": "selection", "messages": []}))  # Go to home
    if st.sidebar.button("Delete History"):
        st.session_state.messages = []  # Clear the chat history
        st.sidebar.success("Chat history deleted.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input(placeholder="What is up?"):
        key = st.session_state.selected_personality
        print(key)
        if (key == "Kanye West"):
            msg = kanye(prompt)
        elif key.strip() == "Gordon":
            print("Entered Here")
            msg  = Gordon(prompt)
        elif key == "Steven He":
            msg = Steven(prompt)
        else:
            msg = cat()
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Streamed response emulator
        def response_generator(msg):
            response = msg
            for word in response.split():
                yield word + " "
                time.sleep(0.05)

        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(msg))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
