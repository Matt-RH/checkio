import re
import itertools


def count_digits(text: str) -> int:
    """
    You need to count the number of digits in a given string.
    Input: A Str.
    Output: An Int.
    """
    digits = re.findall(r"\d+", text)
    combined = itertools.chain.from_iterable(digits)
    return len(list(combined))


if __name__ == "__main__":
    print("Example:")
    print(count_digits("hi"))

    assert count_digits("hi") == 0
    assert count_digits("who is 1st here") == 1
    assert count_digits("my numbers is 2") == 1
    assert (
        count_digits(
            "This picture is an oil on canvas "
            "painting by Danish artist Anna "
            "Petersen between 1845 and 1910 year"
        )
        == 8
    )
    assert count_digits("5 plus 6 is") == 2
    assert count_digits("") == 0
    print("Challenge complete!")
