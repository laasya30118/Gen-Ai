
import os
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

# Load environment variables
load_dotenv()

# Select AI provider
provider_name = input(
    "Choose provider (gemini/ollama): "
).strip().lower()

# Initialize selected provider
if provider_name == "gemini":

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key not found in .env"
        )

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":

    provider = OllamaProvider("qwen2.5:0.5b")

else:
    raise ValueError("Invalid provider selected")

# Create common client
client = LLMClient(provider)

# Get user prompt
prompt = input("Enter your question: ")

# Generate response
try:
    answer = client.generate(prompt)

    print("\nLLM Response:")
    print(answer)

except Exception as e:
    print("\nError generating response:", e)
