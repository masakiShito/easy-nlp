import unittest
from easynlp.preprocessing import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def test_clean(self):
        processor = TextProcessor()
        text = "This is an example sentence to be cleaned!"
        cleaned_text = processor.clean(text)
        self.assertEqual(cleaned_text, "example sentence cleaned")

if __name__ == '__main__':
    unittest.main()
