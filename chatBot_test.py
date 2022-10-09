import unittest
import chatBot

class test(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(chatBot.greeting("hi"), "hey")

    def test_IntroduceMe(self):
        self.assertEqual(chatBot.IntroduceMe(
            "your name"), "My name is AgroBot.")


if __name__ == "__main__":
    unittest.main()


