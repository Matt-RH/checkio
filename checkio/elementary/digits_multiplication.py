def checkio(number: int) -> int:
    """
    You are given a positive integer. Your function should calculate the
    product of the digits excluding any zeroes. For example: The number
    given is 123405. The result will be 1*2*3*4*5=120
    (don't forget to exclude zeroes).

    Input: A positive integer.
    Output: The product of the digits as an integer.
    """

    nums = [int(x) for x in str(number)]
    prod = 1
    for i in nums:
        if i != 0:
            prod *= i
        pass
    return prod


if __name__ == "__main__":
    print("Example:")
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Challenge Complete!")
