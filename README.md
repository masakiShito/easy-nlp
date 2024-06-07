# EasyNLP

EasyNLP is a simple and easy-to-use natural language processing (NLP) library designed to help you with text preprocessing, sentiment analysis, text generation, translation, and summarization tasks. With EasyNLP, you can quickly integrate powerful NLP capabilities into your Python projects with minimal effort.

## Features

- **Text Preprocessing**: Clean and preprocess text data easily.
- **Sentiment Analysis**: Analyze the sentiment of text (positive, negative, neutral).
- **Text Generation**: Generate coherent and contextually relevant text based on a given prompt.
- **Translation**: Translate text between different languages.
- **Summarization**: Summarize long articles or documents into concise summaries.

## Installation

Install EasyNLP via pip:

```bash
pip install git+https://github.com/yourusername/easy-nlp.git
```

# Usage

## Text Preprocessing

```python
from easynlp.preprocessing import TextProcessor

processor = TextProcessor()
cleaned_text = processor.clean("This is an example sentence.")
print(cleaned_text)
```

## Sentiment Analysis

```python
from easynlp.sentiment_analysis import SentimentAnalyzer

analyzer = SentimentAnalyzer()
result = analyzer.analyze("I love this library!")
print(result)
```

## Text Generation

```python
from easynlp.text_generation import TextGenerator

generator = TextGenerator()
generated_text = generator.generate("Once upon a time")
print(generated_text)
```

## Translation

```python
from easynlp.translation import Translator

translator = Translator()
translated_text = translator.translate("Hello, how are you?")
print(translated_text)
```

## Summarization

```python
from easynlp.summarization import Summarizer

summarizer = Summarizer()
summary = summarizer.summarize("This is a long article that needs to be summarized.")
print(summary)
```

# Contributing

We welcome contributions! Feel free to open issues or submit pull requests on [GitHub](https://github.com/masakiShito/easy-nlp).

# License

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/masakiShito/easy-nlp/blob/main/LICENSE) file for details.
