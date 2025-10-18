import os
from google import genai
from google.genai import types

# --- 1. CLIENT INITIALIZATION ---

def get_gemini_client():
    """Initializes and returns the Gemini client using the environment key."""
    # This assumes GEMINI_API_KEY has been loaded into the environment by main.py
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        # Raise an error if the key isn't found, indicating a setup issue
        raise ValueError("GEMINI_API_KEY environment variable not set. Please check your .env file and main.py setup.")
        
    return genai.Client(api_key=api_key)

# --- 2. THE CORE RECONSTRUCTION FUNCTION ---

def reconstruct_text(fragmented_text: str) -> str:
    """
    Sends the fragmented text to the Gemini API for reconstruction 
    and returns the coherent, reconstructed version.
    """
    
    try:
        client = get_gemini_client()
    except ValueError as e:
        print(f"Initialization Error: {e}")
        return "ERROR: API Client failed to initialize."
        
    # Prompt Engineering: Act as an AI Archaeologist
    prompt = f"""
    You are Project Chronos, an AI Archaeologist specializing in reconstructing fragmented digital text from the past.
    Your goal is to fill in missing context, expand all slang, abbreviations, and acronyms, and produce a single,
    coherent, complete, and contextually plausible reconstruction of the original text.

    You must only return the reconstructed, expanded text and nothing else.
    Do not add any greetings, explanations, or quotes around the output.

    FRAGMENTED TEXT TO RECONSTRUCT:
    "{fragmented_text}"
    """

    print("--- ⏳ Sending fragment to AI for reconstruction... ---")

    try:
        # Use a fast and capable model for text completion
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        # Extract and clean the reconstructed text
        reconstructed_text = response.text.strip()
        return reconstructed_text

    except Exception as e:
        print(f"An error occurred during Gemini API call in reconstruct.py: {e}")
        return "ERROR: Could not reconstruct text."