import unittest
from easynlp.sentiment_analysis import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_analyze_positive(self):
        result = self.analyzer.analyze("I love this library!")
        self.assertEqual(result[0]['label'], 'POSITIVE')

    def test_analyze_negative(self):
        result = self.analyzer.analyze("I hate this library!")
        self.assertEqual(result[0]['label'], 'NEGATIVE')

if __name__ == '__main__':
    unittest.main()
