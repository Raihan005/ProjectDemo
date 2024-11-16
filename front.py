import streamlit as st

# Custom CSS to style the cards and layout
custom_css = """
<style>
    .title-style {
        font-size: 2.5em;
        color: #1DB954;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .card {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 10px;
        display: inline-block;
        width: 100%;
    }
    
    .card:hover {
        background-color: #e0e0e0;
    }

    .personality-image {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .personality-name {
        font-size: 1.2em;
        margin-top: 10px;
        font-weight: bold;
    }

    .select-button {
        background-color: #1DB954;
        color: white;
        font-size: 1.0em;
        padding: 8px 15px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        margin-top: 10px;
    }

    .select-button:hover {
        background-color: #17a34a;
    }
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Set the title of the app with a styled class
st.markdown('<div class="title-style">Yo, what\'s up? Pick your vibe, let\'s get this therapy session started!</div>', unsafe_allow_html=True)

# Define the personalities and their attributes
personalities = [
    {"name": "Kanye West", "image": "kanye.png"},
    {"name": "Gordon", "image": "gorden.jpg"},
    {"name": "Cat", "image": "cat.jpg"}
]

# Create a selection variable
selected_personality = None

# Display cards for personalities using columns for layout
col1, col2, col3 = st.columns(3)

for i, personality in enumerate(personalities):
    with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
        st.markdown(
            f"""
            <div class="card">
                <img src="data:image/png;base64,{st.image(personality["image"], use_column_width=True)}" class="personality-image" alt="{personality["name"]}">
                <div class="personality-name">{personality["name"]}</div>
                <button class="select-button">{personality['name']}</button>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Use Streamlit's button for interaction
        if st.button(f"Select {personality['name']}", key=personality["name"]):
            selected_personality = personality["name"]

# Proceed Button
if st.button("Next"):
    if selected_personality:
        st.write(f"You selected: **{selected_personality}**")
    else:
        st.warning("Please select a personality before proceeding.")
