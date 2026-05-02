from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


def get_embedding(text: str, model_name: str = "gemini-embedding-001") -> list[float]:
    """
    Convert text to embeddings using Gemini API.
    
    Args:
        text: The text to convert to embeddings.
        model_name: The embedding model to use. Default is "text-embedding-004".
    
    Returns:
        A list of floats representing the embedding vector.
    """
    client = genai.Client()
    
    response = client.models.embed_content(
        model=model_name,
        contents=text
    )
    
    return response.embeddings[0].values


if __name__ == "__main__":
    sample_text = "This is a sample text for embedding generation."
    embedding = get_embedding(sample_text)
    
    print(f"Embedding dimension: {len(embedding)}")
    print(f"First 10 values: {embedding[:10]}")
