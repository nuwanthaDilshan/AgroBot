#import libraries
import unittest
import App

class test(unittest.TestCase):

# Response test
    def test_Agro(self):
        self.assertIsInstance(App.Agro("what is biological science"), str)

if __name__ == "__main__":
    unittest.main()