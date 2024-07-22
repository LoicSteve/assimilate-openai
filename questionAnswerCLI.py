#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model to answer questions. I also used AI via GitHub Copilot to generate this code. 
"""

import openai
import os
import click


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


@click.command()
@click.argument("text")
def main(text):
    """
    This is the main function that you ask the Open AI API a question to get an answer
    example: python questionAnswerCLI.py "What is the capital of Nigeria?"
    """

    response = submit_question(text)
    print(response)


if __name__ == "__main__":
    main()
