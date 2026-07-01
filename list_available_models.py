from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

for model in client.models.list():
    if 'generateContent' in model.supported_actions and "gemma" in model.name:
        print(f"Model Name: {model.name}") 
        print(f"Description: {model.description}\n")