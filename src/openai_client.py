from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Set your OpenAI API key from the .env file
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)


def generate_embeddings(text: str) -> List[float]:
    """
    Generates embeddings for the given text using OpenAI's API.
    """
    try:
        response = client.embeddings.create(input=text, model="text-embedding-ada-002")
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return None
