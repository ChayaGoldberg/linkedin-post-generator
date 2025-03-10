

# LinkedIn Post Generator

A Python-based web application that allows users to generate customized LinkedIn posts. The app uses OpenAI's GPT-3.5 to generate posts in Hebrew, based on a user-selected style, topic, and length.

## Features

- Generate LinkedIn posts in various styles (e.g., Professional, Funny, Inspirational, Marketing, Personal Story, Academic, Friendly).
- Choose from different post lengths: Short, Medium, and Long.
- Input a topic and goal for the post.
- Displays the generated post and allows users to copy it as Markdown.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChayaGoldberg/linkedin-post-generator.git

## Navigate to the project directory:

cd linkedin-post-generator

## Install the required dependencies:

pip install -r requirements.txt

## Set your OpenAI API key. You can store it in your environment variables:

export OPENAI_API_KEY="your-api-key-here"

## Run the app:

    streamlit run linkedin_post_generator.py

## Usage

    Open the web application.
    Enter the topic for the post.
    Choose the desired style and goal for the post.
    Select the length of the post.
    Click "Create Post" to generate your LinkedIn post.
    Copy the generated post or the Markdown content.

## Technologies Used

    Python
    Streamlit
    OpenAI API (GPT-3.5)
    GitHub

## License

This project is licensed under the MIT License - see the LICENSE file for details.

