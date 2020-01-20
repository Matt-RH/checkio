def mult_two(a, b):
    """
    In this mission you should write a function that introduces a person with
    the given parameter's attributes.

    Input: Two arguments. String and positive integer.
    Output: String.
    """

    return a * b


if __name__ == "__main__":
    print("Example:")
    print(mult_two(3, 2))

    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Challenge Complete!")
