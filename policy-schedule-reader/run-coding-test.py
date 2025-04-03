# %% SET UP LANGUAGE MODEL AND PROMPTS (NO NEED TO EDIT THIS PART)

from google import genai
from google.genai import types
from validate import validate_output_pydantic


def generate(prompt: str, pdf_data: bytes, response_mime_type: str = "text/plain"):
    """A function to generate a response from the model using a prompt and PDF data.

    Args:
        prompt (str): Prompt to be sent to the model
        pdf_data (bytes): PDF data in bytes format to be sent to the model

    Returns:
        str: prompt returned from the model
    """
    
    client = genai.Client(
        vertexai=True,
        project="msmg-datascience-explore",
        location="us-central1",
    )

    prompt_part = types.Part.from_text(text=prompt)

    document_part = types.Part.from_bytes(
        data=pdf_data,
        mime_type="application/pdf",
    )
    
    model = "gemini-2.0-flash"
    contents = [
        types.Content(
        role="user",
        parts=[
            prompt_part,
            document_part,
        ]
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        top_p = 0.95,
        max_output_tokens = 8192,
        response_mime_type=response_mime_type,  # "application/json" or "text/plain"
        safety_settings = [types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="OFF"
        )],
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
    ):
        response += chunk.text

    return response

# %% EDIT BELOW THIS LINE

ipid_path = "gigasure-essential-ipid-october-24.pdf"

# Load the PDF as bytes data here
data = ...

# Write an prompt to accurately extract ONLY the specified fields (see README) from the PDF
prompt = ""

# Generate Response
response = generate(prompt, data, response_mime_type="text/plain")

# Validate the output
# It should look something like this:
# example_output = """{
#     "Hospital Benefit": 10000,
#     "Personal Accident": 5000,
#     "Standard Sports and Activities": "Included"
# }"""

validated_output = validate_output_pydantic(response)

print("Validated Output:")
print(validated_output.model_dump_json(indent=4, by_alias=True))


# %%