import unittest

def multiply(x,y):
    return x+y

class TestMultiply(unittest.TestCase):

    def test_multiply(self):

        test_x = 5
        test_y = 10

        self.assertEqual(multiply(test_x,test_y),50,"Should be 50")

if __name__ == "__main__":
    unittest.main()

# another way to run test is to pass art unittest when running py file
# py -m unittest mult -v
# -v is optional and is used for more detailed output