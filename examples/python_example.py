#!/usr/bin/env python3
"""
GLM-4.6-FP8 OpenAI-Compatible API Example (Python)
VERIFIED working example using the Zai Inference Provider
"""

import os
from openai import OpenAI

# Initialize the OpenAI client with Zai Inference Provider
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

# Create a chat completion
completion = client.chat.completions.create(
    model="zai-org/GLM-4.6-FP8:zai-org",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

# Print the response
print("Response:")
print(completion.choices[0].message.content)
