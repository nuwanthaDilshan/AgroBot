from chatBot import basic1, basic2, greeting, IntroduceMe

# greeting test
def test_greeting():
    assert greeting("hi") == "hello"


if __name__ == "__main__":
    test_greeting()
    print("Everything passed")

# IntroduceMe test
def test_IntroduceMe():
    assert IntroduceMe("your name") == "My name is AgroBot."


if __name__ == "__main__":
    test_IntroduceMe()
    print("Everything passed")

# Basic_Q_1 test
def test_Basic_Q_1():
    assert basic1("can you help me") == "yes I can"

if __name__ == "__main__":
    test_Basic_Q_1()
    print("Everything passed")

# Basic_Q_2 test
def test_Basic_Q_2():
    assert basic2("Okay") == "Is there anything else to know?"

if __name__ == "__main__":
    test_Basic_Q_2()
    print("Everything passed")

