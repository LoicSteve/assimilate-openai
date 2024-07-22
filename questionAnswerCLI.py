#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model to answer questions. I also used AI via GitHub Copilot to generate this code. 
"""


import click


from oalib.solutions import submit_question


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
