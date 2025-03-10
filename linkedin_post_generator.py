import os
import streamlit as st
import openai

# Set the API key for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title
st.title("📝 LinkedIn Post Generator")
st.markdown("""
    <style>
        /* Full background */
        .stApp {
            background: url("https://i.imgur.com/qf5gEik.jpeg") no-repeat center center fixed;
            background-size: cover;
        }
        /* General design */
        * {
            direction: ltr; /* Set the text direction to left-to-right */
            text-align: left; /* Align text to the left */
            font-family: 'Arial', sans-serif;
            color: black; /* All text will be in black */
        }
        h1 {
            color: black; /* Main title in black */
        }
        .stTextInput, .stSelectbox, .stRadio, .stButton {
            border-radius: 12px;
            padding: 10px;
            margin-bottom: 15px;
            background-color: rgba(211, 211, 211, 0.8); /* Light gray color (#D3D3D3) */
        }
        .stTextInput input, .stSelectbox div, .stRadio label, .stButton button {
            font-size: 16px;
        }
        .stTextArea textarea {
            border-radius: 12px;
            padding: 12px;
        }
        .stButton button {
            background-color: #4B6A8D; /* Light blue-gray color for the button */
            color: white;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #3F5971; /* Darker color when hovering over the button */
        }
        .post-container {
            background-color: #D3D3D3; /* Light gray color */
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            color: black; /* Inside the container, the text color will be black */
        }
        /* Change the color of the input field labels only */
        .stTextInput label, .stSelectbox label, .stRadio label {
            color: black; /* The text color inside the gray background will be black */
        }
        /* Remove button container */
        .stButton {
            box-shadow: none;
            border: none;
        }
        /* Add space between containers */
        .spacer {
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# User input fields
topic = st.text_input("🔹 What is the topic of the post?")
style = st.selectbox("🎭 Choose a style:", ["Professional", "Funny", "Inspirational", "Marketing", "Personal Story", "Academic", "Friendly"])
goal = st.selectbox("🎯 What is the goal of the post?", ["Personal Branding", "Job Search", "Inspiration", "Marketing", "Networking", "Sharing Insights", "Creating Discussion"]) 
length = st.radio("📏 Choose the post length:", ["Short", "Medium", "Long"])

# Button to create the post
if st.button("✨ Create Post"):
    with st.spinner("Creating post... 🎨"):
        # Mapping post lengths
        length_map = {"Short": "up to 150 words", "Medium": "up to 300 words", "Long": "over 500 words"}

        # Create the prompt
        prompt = f"Write a LinkedIn post in English on the topic '{topic}' in the style of {style}, with the goal of {goal}, and length {length_map[length]}."

        # Call the OpenAI API to generate the post
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are writing LinkedIn posts"},
                      {"role": "user", "content": prompt}]
        )

        post_text = response["choices"][0]["message"]["content"]

        # Display the generated post
        st.success("🎉 Here's your post:")
        st.markdown(f"""
            <div class="post-container">
                {post_text}
            </div>
        """, unsafe_allow_html=True)

        # Add space before the Markdown code block
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

        # Display the Markdown code for copying
        st.markdown("📋 Copy the content:")
        st.code(post_text, language="markdown", height=150)
