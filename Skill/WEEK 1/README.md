# WEEK 1 – First LLM API Call Using Google Gemini

## Aim
To connect Google Colab with Google's Gemini API and generate AI responses using Python prompts.

## Technologies Used
- Python
- Google Gemini API
- Google GenAI SDK
- Google Colab
- API Key Authentication

## Tools Used
- Google Colab
- Google AI Studio

## Project Structure

```text
WEEK 1/
├── README.md
└── Week1_First_LLM_API_Call_Gemini.ipynb
```

## Implementation Steps

1. Install the Google GenAI Python package.
2. Generate a Gemini API key using Google AI Studio.
3. Store the API key securely using Google Colab Secrets.
4. Retrieve the API key using `userdata.get()`.
5. Import and initialize the Gemini client.
6. Send prompts to the Gemini model.
7. Generate and display AI responses.

## Installation

```python
!pip install -q google-genai
```

## API Configuration

Store the API key in Google Colab Secrets using the name:

`GEMINI_API_KEY`

Never expose your actual API key in public repositories.

## Execution

1. Open the Google Colab notebook.
2. Run the required code cells.
3. Configure the Gemini API key.
4. Initialize the Gemini client.
5. Enter a prompt.
6. View the generated AI response.

## Result

Successfully connected Google Colab with the Google Gemini API, initialized the Gemini client and generated AI responses using Python.

## Conclusion

The first LLM API call was successfully implemented using Google Colab and the Google Gemini API.
