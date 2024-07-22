#!/usr/bin/env python3

""""  Library with OpenAI solustions as functions
"""

import os
import openai


def submit_question(text):
    """This submits a question to the openai API and returns the response"""

    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response["choices"][0]["message"]["content"]


# let's build a fucntion that converts commemnts innto code in any language
def code_generator(text, language):
    """
    Submits a prompt to the OpenAI API to generate code in the specified programming language and returns the response.

    Parameters:
    text (str): The prompt describing the code to be generated.
    language (str): The programming language for the generated code.

    Returns:
    str: The generated code from the OpenAI API.
    """

    openai.api_key = os.getenv("OPENAI_API_KEY")
    # Construct the prompt to include the desired programming language
    prompt = f"Convert the following description into {language} code:\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    return response["choices"][0]["message"]["content"]
