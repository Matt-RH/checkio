def find_message(text: str) -> str:
    """
    You are given a chunk of text. Gather all capital letters in one word in
    the order that they appear in the text. For example: text = "How are you?
    Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters,
    we get the message "HELLO".

    Input: A text as a string (unicode).
    Output: The secret message as a string or an empty string.
    """

    l_list = [i for i in text if i.isupper()]
    return "".join(l_list)


if __name__ == "__main__":
    print("Example:")
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    assert (
        find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    ), "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Challenge Complete!")
