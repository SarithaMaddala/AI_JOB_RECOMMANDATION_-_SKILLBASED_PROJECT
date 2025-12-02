import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI




load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY)



def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file: A file-like object (e.g., from Flask upload)

    Returns:
        str: The extracted text
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_openai(prompt, max_tokens=500, temperature=0.5):
    """
    Sends a prompt to the OpenAI API and returns the response.

    Args:
        prompt (str): Text input for the model.
        max_tokens (int): Response length.
        temperature (float): Creativity level.

    Returns:
        str: Model output text.
    """
    completion = client.chat.completions.create(
        
        model="gpt-4.1-mini",
        messages=[
            {  
                "role": "user",
                "content":prompt
            }
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )

    return completion.choices[0].message.content





client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);


