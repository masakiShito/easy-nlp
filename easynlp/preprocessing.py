import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

class TextProcessor:
    def __init__(self, language='english'):
        self.stop_words = set(stopwords.words(language))
        self.punctuation = string.punctuation

    def clean(self, text):
        # トークン化
        words = word_tokenize(text)
        # 小文字化と不要な単語の削除
        cleaned_words = [word.lower() for word in words if word.lower() not in self.stop_words and word not in self.punctuation]
        return ' '.join(cleaned_words)
