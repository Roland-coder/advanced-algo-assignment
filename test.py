from main import sockMerchant
import unittest

class Test(unittest.TestCase):
    def test_thirty(self):
        ar = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        n = 30
        expected = 10
        self.assertEqual(sockMerchant(n, ar), expected)

    def test_eighty(self):
        ar = [12, 12, 34, 12, 34, 12, 56, 12,  55, 12, 55, 12,
              34, 12, 34, 12, 55, 12, 34, 55, 12, 34, 34, 12, 55,
              12, 55, 34, 55, 12, 34, 55, 34, 12, 55, 12, 55, 34, 12,
              55, 12, 12, 34, 12, 34, 12, 56, 12,  55, 12, 55, 12, 34,
              12, 34, 12, 55, 12, 34, 55, 12, 34, 34, 12, 55, 12, 55, 34, 55, 12, 34, 55, 34, 12, 51, 23, 54, 89, 13, 43]
        n = 80
        expected = 36
        self.assertEqual(sockMerchant(n, ar), expected)

if __name__ == '__main__':
    unittest.main()
