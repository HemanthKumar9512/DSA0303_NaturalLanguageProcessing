from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-5-mini",
    input="Write a short story about a robot."
)

print(response.output_text)
