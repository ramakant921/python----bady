from openai import OpenAI

# Initialize client with your API key
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Send a chat message
response = client.chat.completions.create(
    model="gpt-2.5-turbo",   # you can also use "gpt-4o-mini" or "gpt-4o"
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Jarvis."},
        {"role": "user", "content": "Hello Jarvis, how are you?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)
