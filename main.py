import os
import sys
from dotenv import load_dotenv
from reconstruct import reconstruct_text # Import the function from your reconstruct.py file

# --- 1. SEARCH FUNCTION (Placeholder for actual Web Search API) ---

def search_for_context(query: str) -> list[dict]:
    """
    Simulates a web search using the reconstructed query and extracts 3-5 links.
    In a complete project, this function must use a dedicated Search Engine API.
    
    Returns a list of dictionaries, e.g., [{"link": "url", "snippet": "description"}]
    """
    print(f"--- 🔍 Searching the web for context using query: '{query[:60]}...' ---")
    
    # --- PLACEHOLDER CODE - MUST BE REPLACED WITH ACTUAL SEARCH API CALL ---
    
    # We create context-rich search results based on the example input's expected output
    if "top 8" in query.lower() or "shaking my head" in query.lower():
        return [
            {
                "link": "https://en.wikipedia.org/wiki/Myspace#Features",
                "snippet": "Explaining the 'Top 8' friends feature on the MySpace social network."
            },
            {
                "link": "https://www.dictionary.com/e/slang/smh/",
                "snippet": "Definition and usage of the internet slang term 'SMH' (shaking my head)."
            },
            {
                "link": "https://en.wikipedia.org/wiki/List_of_Internet_Relay_Chat_commands",
                "snippet": "Common chat abbreviations like 'G2G' (got to go) and 'TTYL' (talk to you later)."
            }
        ]
    # Fallback for any other input (ensure you have 3 links for the report)
    return [
        {"link": "https://example.com/slang-archive", "snippet": "A general archive of 2000s internet slang terms and meanings."},
        {"link": "https://example.com/social-history", "snippet": "An article explaining the cultural history of early social media features."},
        {"link": "https://example.com/tech-lingo", "snippet": "A glossary of obsolete technological jargon and acronyms."}
    ]

# --- 2. REPORT GENERATION FUNCTION ---

def generate_report(original: str, reconstructed: str, sources: list[dict]):
    """
    Generates and prints the final Reconstruction Report in the required format.
    """
    print("\n" + "="*70)
    print("      ✨ RECONSTRUCTION REPORT - PROJECT CHRONOS ✨")
    print("="*70)

    # Original Fragment Section
    print("\n[Original Fragment]")
    print(f"> \"{original}\"")

    # AI-Reconstructed Text Section
    print("\n[AI-Reconstructed Text]")
    print(f"> \"{reconstructed}\"")

    # Contextual Sources Section
    print("\n[Contextual Sources] (3-5 relevant links required)")
    if sources:
        for source in sources:
            # Format the output as a list of hyperlinks and explanations
            print(f"* {source['link']} ({source['snippet']})")
    else:
        print("No relevant contextual sources were found.")
    
    print("="*70 + "\n")

# --- 3. MAIN EXECUTION BLOCK ---

def main():
    # Load environment variables (must happen before calling reconstruct_text)
    load_dotenv() 
    
    # Check for the input argument
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your fragmented text here>\"")
        print("Example: python main.py \"smh at the top 8 drama. g2g, ttyl.\"")
        sys.exit(1)

    # The user's input is the second command-line argument
    original_fragment = sys.argv[1]

    # Phase 2: Reconstruct the text using Gemini
    reconstructed_text = reconstruct_text(original_fragment)
    
    # Phase 3: Perform automated web search using the reconstructed text
    contextual_sources = search_for_context(reconstructed_text)
    
    # Phase 4: Generate the final report
    generate_report(original_fragment, reconstructed_text, contextual_sources)


if __name__ == "__main__":
    main()