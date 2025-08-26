import google.generativeai as genai
import os
from utils.vector_store import VectorStore

vector_store = VectorStore()

def setup_gemini():
    try:
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        return True
    except Exception as e:
        print(f"Error setting up Gemini: {str(e)}")
        return False

def process_football_query(query: str, model: str = "gemini-2.5-flash") -> str:
    """
    Process football-related queries with memory (FAISS).
    """
    try:
        if not setup_gemini():
            return "Error: Unable to configure Gemini API. Please check your API key."

        past_contexts = vector_store.retrieve(query)
        context_text = "\n".join(past_contexts)

        prompt = f"""
        You are Football Genius, an expert football analyst.
        
        Context from past conversation (use it to stay consistent):
        {context_text}
        
        Current question: {query}
        
        Ensure your response is:
        1. Accurate and up-to-date
        2. Easy to understand
        3. Backed by statistics when relevant
        4. Engaging and informative
        """

        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)

        answer = (
            response.text
            if response and response.text
            else "I apologize, but I couldn't generate a response. Please try again."
        )

        vector_store.add(f"User: {query}\nAssistant: {answer}")

        return answer

    except Exception as e:
        print(f"Error in process_football_query: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."