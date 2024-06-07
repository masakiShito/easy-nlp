from transformers import pipeline

class TextGenerator:
    def __init__(self):
        self.generator = pipeline('text-generation')

    def generate(self, prompt, max_length=50):
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']
