
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