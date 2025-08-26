import os
import json

def load_config():
    """
    Load configuration settings for the application
    """
    config = {
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "default_temperature": 0.7,
        "football_expertise_levels": ["Basic", "Intermediate", "Expert", "Professional"],
        "supported_languages": ["English", "Spanish", "French", "German"]
    }
    
    return config