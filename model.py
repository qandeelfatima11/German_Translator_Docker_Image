
from fastapi import FastAPI
import pickle
import uvicorn
import transformers
from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import sacremoses
import sentencepiece


def translate_text(text, target_Language):
    print(text)
    target_code = target_language
    translator = Translator(to_lang-target_code)
    translation = translator.translate(text)
    return translation
# Load a pre-trained translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
text = "my name is nimra?"
translated_text = translator(text, max_length=50)

# Print the translated text
print(f"Translated Text: {translated_text}")

print('hi')
app = FastAPI()


@app.get("/app")
async def root():
    return {text: translated_text}
   

