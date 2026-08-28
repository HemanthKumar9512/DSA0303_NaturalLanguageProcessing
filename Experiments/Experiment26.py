from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "I love learning Python."

result = translator(text)

print(result[0]["translation_text"])
