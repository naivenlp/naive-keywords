import unittest

from .extractor import KeywordsExtractor


class ExtractorTest(unittest.TestCase):

    def testExtractor(self):
        e = KeywordsExtractor(None, None, None)
        print('hello ')


if __name__ == "__main__":
    unittest.main()