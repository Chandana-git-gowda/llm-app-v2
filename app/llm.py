import os
from anthropic import Anthropic

# Create Anthropic client
# API key is read from environment variable (never hardcoded)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def ask_llm(prompt):
    """Send a prompt to Claude and return the response."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
