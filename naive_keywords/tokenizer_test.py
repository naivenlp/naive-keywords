import unittest


from .tokenizer import *


class TokenizerTest(unittest.TestCase):

    def testJiebaTokenizer(self):
        spliter = TokenSpliter()
        concater = TokenConcatenater()
        tokenizer = JiebaTokenizer(spliter=spliter, concater=concater)

        tokens = tokenizer.tokenize('advanced javadeveloper')
        self.assertListEqual(['advanced', 'javadeveloper'], tokens)

        tokenizer.force_split('java developer')
        tokens = tokenizer.tokenize('advanced javadeveloper')
        self.assertListEqual(['advanced', 'java', 'developer'], tokens)

        tokenizer.force_concate('javadeveloper')
        tokens = tokenizer.tokenize('advanced javadeveloper')
        self.assertListEqual(['advanced', 'javadeveloper'], tokens)


if __name__ == "__main__":
    unittest.main()
