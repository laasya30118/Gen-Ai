
# WEEK 2 – Provider-Agnostic LLM Client

## Aim
To develop a provider-agnostic LLM client using Python that supports multiple AI providers, including Google Gemini API and a locally running Ollama model, through a common interface.

## Technologies Used
- Python
- Google Gemini API
- Ollama
- Qwen 2.5 (0.5B)
- Requests
- Python Virtual Environment

## Tools Used
- Visual Studio Code
- Python
- Google AI Studio
- Ollama

## Project Structure

WEEK 2/
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
├── Modelfile
└── README.md

## Installation Steps

1. Install Python 3.10.
2. Install Ollama.
3. Open the project in VS Code.
4. Create a virtual environment:

   python -m venv venv

5. Activate the environment:

   .\venv\Scripts\Activate.ps1

6. Install dependencies:

   python -m pip install -r requirements.txt

7. Download the Ollama model:

   ollama pull qwen2.5:0.5b

8. Configure the Gemini API key in the .env file:

   GEMINI_API_KEY=your_api_key_here

## Execution Steps

Run the application:

   python main.py

Choose an AI provider:
- gemini
- ollama

Enter a question and receive the AI-generated response.

## Testing

Run the unit test:

   python -m unittest test_client.py

Expected result:

   Ran 1 test

   OK

## Result

Successfully developed a provider-agnostic LLM client using Python that supports Google Gemini API and the locally running Ollama model through a common interface.
