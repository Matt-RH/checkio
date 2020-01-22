def checkio(words: str) -> bool:
    """
    Let's teach the Robots to distinguish words and numbers.
    You are given a string with words and numbers separated by whitespaces
    (one space). The words contains only letters. You should check if the
    string contains three words in succession. For example, the string
    "start 5 one two three 7 end" contains three words in succession.

    Input: A string with words.
    Output: The answer as a boolean.
    Precondition: The input contains words and/or numbers. There are no mixed
    words (letters and digits combined).
    """

    count = 0
    for w in words.split():
        try:
            int(w)
            count = 0
        except ValueError:
            count += 1
        if count >= 3:
            return True
        else:
            pass
    return False


if __name__ == "__main__":
    print("Example:")
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello"), "Hello"
    assert not checkio("He is 123 man"), "123 man"
    assert not checkio("1 2 3 4"), "Digits"
    assert checkio("bla bla bla bla"), "Bla Bla"
    assert not checkio("Hi"), "Hi"
    print("Challenge Complete!")
