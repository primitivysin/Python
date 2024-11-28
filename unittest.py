import unittest

class XXXTextCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_YYY(self):
        a=1
        self.assertEqual(a, 1)

if __name__== '__main__':
    unittest.main()
    
        