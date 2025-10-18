# Project title: The AI Archeologist

# Student Name(s) and ID(s)
 T Kiran Shanmukha Sai 
 SE25UCSE009

# Project Description
 Project Chronos is an AI-powered Python application that reconstructs fragmented, informal, or ancient-style messages into clear, full sentences. Using the Google Gemini API, it acts like a digital archeologist — decoding cryptic internet slang, poetic fragments, and symbolic language into readable form. The goal is to preserve meaning across time and context, making even the most obscure messages understandable.

# Setup Instructions
 ## 1. Repository Clone:
 ### To begin, clone this repository to your local machine:
  git clone https://github.com/kiranshanmukha83099-eng/project-chronos.
  cd project-chronos

 ## 2. Environment Setup:
 It is highly recommended to use a Python virtual environment to manage dependencies:
  ### Create the environment
  python -m venv venv
  ### Activate the environment (Windows PowerShell)
   .\venv\Scripts\activate

 ## 3.Install Dependencies 
 ### With the virtual environment active, install all required libraries:
 python -m pip install -r requirements.txt

 ## 4. API Key Configuration
 ### set up API key for the Gemini model:
  Create a file named .env in the root of the project directory.
  #### Add your Google Gemini API key to this file in the following format:
  GEMINI_API_KEY="YOUR_API_KEY_HERE"
# Usage Guide: 
 The application is run directly from the terminal, taking the fragmented text as a command-line argument enclosed in quotes.
 ## Example 1: Ancient Indian Script Fragment.
 python main.py "When the bow of Lord Sri Rama sang, silence fell upon Lanka."
 ## Example 2: Obscure Gaming Acronyms.
 python main.py "brb, I need to check my ICQ. My AOL just crashed again. n00b error."



  



