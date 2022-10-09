from pydoc import doc
import unittest
import chatBot

class test(unittest.TestCase):

    def test_greeting(self):
        self.assertIsInstance(chatBot.greeting("hi"), str)

    def test_Basic_Q_1(self):
        self.assertIsInstance(chatBot.basic1("help me"), str)

    def test_Basic_Q_2(self):
        self.assertIsInstance(chatBot.basic2("ok"), str)

    def test_Basic_Q_3(self):
        self.assertIsInstance(chatBot.basic3("nop"), str)

    def test_Basic_Q_4(self):
        self.assertIsInstance(chatBot.basic4("yep"), str)


if __name__ == "__main__":
    unittest.main()


