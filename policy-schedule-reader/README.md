# Installation Instructions

Install python 3.12

Create a virtual environment and install requirements.txt


# Data Scientist Prompt Engineering Test
## Task Overview

Your task is to extract specific information from an Insurance Product Information Document (IPID) by creating an effective prompt for the Gemini language model.

You can find the document in this folder (gigasure-essential-ipid-october-24.pdf).

## Requirements

Open the file run-coding-test.py.

Here, you'll find a function called `generate()`. This function contains all code required to invoke Google's Gemini LLM with a prompt and a decoded pdf file, and return a response of the specified MIME type (defaulting to plain text).

Your **first task** is to write some code to read the IPID PDF document as bytes. Line 77.

Your **second task** is to construct the prompt, which should instruct the model to:

Extract the following key information from the IPID document:

- Hospital Benefit (integer)
- Personal Accident (integer)
- Standard Sports and Activities (str: valid options = ["Included", "Not Included"])

Return the data in a structured JSON format. The response will be a string, and the rest of the script has been set up to parse and validate the output (see validate.py).

Notes:

- Focus on creating a clear, specific prompt that will reliably extract the required information.
- Consider how to make your prompt robust to variations in document formatting.

Good luck!