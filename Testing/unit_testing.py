import unittest
import code

class Testcap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        res = code.capital_text(text)
        self.assertEqual(res, 'Python')

    def test_multiple_word(self):
        text = 'i am using python'
        res = code.capital_text(text)
        self.assertEqual(res, 'I Am Using Python')

if __name__ == '__main__':
    unittest.main()