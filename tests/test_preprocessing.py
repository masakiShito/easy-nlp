import unittest
from easynlp.preprocessing import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = TextProcessor()

    def test_clean(self):
        self.assertEqual(self.processor.clean("This is an example sentence."), "example sentence")
        self.assertEqual(self.processor.clean("Another example!"), "another example")

if __name__ == '__main__':
    unittest.main()
