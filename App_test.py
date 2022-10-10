import unittest
import App

class test(unittest.TestCase):

    def test_Agro(self):
        self.assertIsInstance(App.Agro("what type of desises"), str)

if __name__ == "__main__":
    unittest.main()