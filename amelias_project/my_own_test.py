# Import python's built-in regular expression library
import re
import anthropic
import os

# Retrieve the API_KEY & MODEL_NAME variables from the IPython store
API_KEY = os.getenv("MY_API_KEY")
MODEL_NAME = "claude-3-opus-20240229"

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt: str = "") -> str:
    """Helper function: sends prompt to Claude and returns the response."""
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return ''.join(block.text for block in message.content)

