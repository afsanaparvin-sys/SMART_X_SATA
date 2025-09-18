import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PROJECT_NAME = os.getenv("PROJECT_NAME", "SATA Content Generator")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # OpenAI settings
    DEFAULT_MODEL = "gpt-4"
    MAX_TOKENS = 1500
    TEMPERATURE = 0.7
    
    # Content settings
    BRAND_GUIDELINES = {
        "organization": "SATA CommHealth",
        "full_name": "Singapore Anti-Tuberculosis Association",
        "mission": "Here to Care for the Health of Seniors and the Vulnerable",
        "tone": "professional and empathetic",
        "target_region": "Singapore"
    }