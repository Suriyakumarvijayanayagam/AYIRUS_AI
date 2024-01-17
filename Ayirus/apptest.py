import streamlit as st
import google.generativeai as genai
import logging
import json
from loghandler import MaxLinesRotatingFileHandler
import time  # Import the time module

import requests
from bs4 import BeautifulSoup
import urllib.parse

with open('api.json', 'r') as f:
    data = json.load(f)

# Configure the GenerativeAI API key
genai.configure(api_key=data['api'])

# Create a GenerativeModel instance
model = genai.GenerativeModel('gemini-pro')

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Set up logging
# Configure the logger with the custom handler
log_filename = 'logs/chat_log.txt'
max_lines = 1000
logging.basicConfig(handlers=[MaxLinesRotatingFileHandler(log_filename, max_lines=max_lines)],
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Streamlit app
def main():
    st.set_page_config(
        page_title="ᴀʏɪʀᴜꜱ​",
        page_icon="🤖",
        layout="centered"
    )

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'leetcoding' not in st.session_state:
        st.session_state.leetcoding = False

    if 'hackerranking' not in st.session_state:
        st.session_state.hackerranking = False

    st.error("##### 🚨ᴀʏɪʀᴜꜱ ᴀɪ ​🇮​​🇸​ ​🇦​​🇳​ ​🇮​​🇳​​🇳​​🇴​​🇻​​🇦​​🇹​​🇮​​🇻​​🇪​ ​​🇼​​🇪​​🇧​ ​🇦​​🇵​​🇵​​🇱​​🇮​​🇨​​🇦​​🇹​​🇮​​🇴​​🇳​ ​🇵​​🇴​​🇼​​🇪​​🇷​​🇪​​🇩​ ​🇧​​🇾​ ​🇬​​🇪​​🇳​​🇪​​🇷​​🇦​​🇹​​🇮​​🇻​​🇪​​🇦​​🇮​ ")

    st.info("###### 👉🏻 🇬​​🇪​​🇹​ ​🇵​​🇪​​🇷​​🇸​​🇴​​🇳​​🇦​​🇱​​🇮​​🇿​​🇪​​🇩​ ​🇬​​🇺​​🇮​​🇩​​🇦​​🇳​​🇨​​🇪​ ​🇦​​🇳​​🇩​ ​🇮​​🇱​​🇱​​🇺​​🇸​​🇹​​🇷​​🇦​​🇹​​🇮​​🇻​​🇪​ ​🇪​​🇽​​🇦​​🇲​​🇵​​🇱​​🇪​​🇸​ ​🇹​​🇴​ ​🇹​​🇦​​🇨​​🇰​​🇱​​🇪​ ​🇾​​🇴​​🇺​​🇷​ ​🇨​​🇴​​🇩​​🇮​​🇳​​🇬​ ​🇨​​🇭​​🇦​​🇱​​🇱​​🇪​​🇳​​🇬​​🇪​​🇸​.")

    st.markdown("#### 👨‍🔧 ​​🇱​​🇺​​🇨​​🇮​​🇩​ ​🇦​​🇵​​🇵​​🇷​​🇴​​🇦​​🇨​​🇭​ ​🇹​​🇴​ ​🇵​​🇷​​🇴​​🇧​​🇱​​🇪​​🇲​-​🇸​​🇴​​🇱​​🇻​​🇮​​🇳​​🇬​,​🇼​​🇮​​🇹​​🇭​ ​🇨​​🇱​​🇪​​🇦​​🇷​  ​🇬​​🇺​​🇮​​🇩​​🇦​​🇳​​🇨​​🇪​")
        

    st.markdown("<h1 style='text-align: center;'>ᴀʏɪʀᴜꜱ ᴀɪ</h1>", unsafe_allow_html=True)

    st.sidebar.write("")
    user_prompt = st.sidebar.text_area("ᴛᴇʟʟ ᴍᴇ ᴡʜᴀᴛ ɪꜱ ɪᴛ", value="", height=150, key="user_input", placeholder="​🇸​​🇦​​🇾​ ​🇸​​🇴​​🇲​​🇪​​🇹​​🇭​​🇮​​🇳​​🇬​...🥱")

    try:
        if st.sidebar.button("​🇸​​🇺​​🇧​​🇲​​🇮​​🇹​🙋🏻‍♂"):
            if user_prompt:
                user_message = {"role": "user", "content": user_prompt, "timestamp": time.time()}
                st.session_state.messages.append(user_message)
                with st.chat_message("user"):
                    st.write(user_prompt)
                    logging.info(f'user: {user_prompt}')

                # Check which button is clicked
                if st.session_state.leetcoding:
                    base_url = "https://walkccc.me/LeetCode/"
                    # Fetch the main page content
                    response = requests.get(base_url)
                    soup = BeautifulSoup(response.text, "html.parser")

                    # Find relevant pages based on user input
                    relevant_pages = []
                    for link in soup.find_all("a"):
                        page_url = urllib.parse.urljoin(base_url, link.get("href"))
                        if user_prompt.lower() in link.text.lower():  # Case-insensitive search
                            relevant_pages.append(page_url)

                    # Assign the output to a variable
                    filtered_page_urls = relevant_pages

                    if filtered_page_urls:
                        st.info("Relevant pages found:")
                        for page_url in filtered_page_urls:
                            st.info(page_url)
                    else:
                        st.info("No relevant pages were found.")

                    # Generate content for Leetcode with a predefined prompt
                    predefined_prompt = "clearly explain about the problem statement with the same sample input and output leetcode has used for this problem clearly explain the problem and guide the user to what they do to solve this problem and give them a optimized solution for this problem and provide any additional reference related to this problem statement and the problem is"

                    combined_prompt = f"{predefined_prompt} {user_prompt}"
                    generate_and_display_output(combined_prompt)
                   
                elif st.session_state.hackerranking:
                    # Generate content for Hackerrank with a predefined prompt
                    predefined_prompt = "clearly explain about the problem statement with the same sample input and output hackerrank used for this problem clearly explain the problem and guide the user to what they do to solve this problem and give them a optimized solution for this problem and provide any additional reference related to this problem statement and the problem is "
                    combined_prompt = f"{predefined_prompt} {user_prompt}"
                    generate_and_display_output(combined_prompt)
                else:
                    generate_and_display_output(user_prompt)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        logging.error(f'Error: {str(e)}')

    # Separate buttons for leetcode and hackerrank
    if st.button("ʟᴇᴇᴛᴄᴏᴅᴇ"):
        st.session_state.leetcoding = True
        st.session_state.hackerranking = False
        st.error("🚀 **ʀᴇᴀᴅʏ ᴛᴏ ꜱᴏʟᴠᴇ?** ꜱʜᴀʀᴇ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍ ꜱᴛᴀᴛᴇᴍᴇɴᴛ, ᴀɴᴅ ʟᴇᴛ  ᴍᴇ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇꜱᴛ!")
        logging.info("assistant: 🚀 **ʀᴇᴀᴅʏ ᴛᴏ ꜱᴏʟᴠᴇ?** ꜱʜᴀʀᴇ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍ ꜱᴛᴀᴛᴇᴍᴇɴᴛ, ᴀɴᴅ ʟᴇᴛ  ᴍᴇ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇꜱᴛ!")

    if st.button("ʜᴀᴄᴋᴇʀʀᴀɴᴋ"):
        st.session_state.leetcoding = False
        st.session_state.hackerranking = True
        st.error("🚀 **ʀᴇᴀᴅʏ ᴛᴏ ꜱᴏʟᴠᴇ?** ꜱʜᴀʀᴇ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍ ꜱᴛᴀᴛᴇᴍᴇɴᴛ, ᴀɴᴅ ʟᴇᴛ  ᴍᴇ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇꜱᴛ!")
        logging.info("assistant: 🚀 **ʀᴇᴀᴅʏ ᴛᴏ ꜱᴏʟᴠᴇ?** ꜱʜᴀʀᴇ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍ ꜱᴛᴀᴛᴇᴍᴇɴᴛ, ᴀɴᴅ ʟᴇᴛ  ᴍᴇ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇꜱᴛ!")


# Function to generate and display output
def generate_and_display_output(prompt):
    response = model.generate_content(prompt)

    if response and hasattr(response, 'text'):
        assistant_message = {"role": "assistant", "content": response.text, "timestamp": time.time()}
        st.session_state.messages.append(assistant_message)
        with st.chat_message("assistant"):
            st.write(response.text)
            logging.info(f'assistant: {response.text}')
    else:
        st.warning("Failed to generate content. Please try again.")


if __name__ == "__main__":
    main()

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.caption("ᴄʀᴇᴀᴛᴇᴅ  🎭 ʙʏ ꜱᴜʀɪʏᴀ")
