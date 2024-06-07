from transformers import pipeline

class Translator:
    def __init__(self):
        self.translator = pipeline('translation_en_to_fr')

    def translate(self, text):
        return self.translator(text)[0]['translation_text']
