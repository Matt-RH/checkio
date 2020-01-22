def checkio(data: str) -> bool:
    """
    The password will be considered strong enough if its length is greater
    than or equal to 10 symbols, it has at least one digit, as well as
    containing one uppercase letter and one lowercase letter in it. The
    password contains only ASCII latin letters or digits.

    Input: A password as a string.
    Output: Is the password safe or not as a boolean or any data type that can
    be converted and processed as a boolean.
    """

    if len(data) < 10:
        return False
    contains_num = any(x.isdigit() for x in data)
    contains_upper = any([True if x.isupper() else False for x in data])
    contains_lower = any([True if x.islower() else False for x in data])
    return all([contains_num, contains_upper, contains_lower])


if __name__ == "__main__":
    assert not checkio("A1213pokl"), "1st example"
    assert checkio("bAse730onE4"), "2nd example"
    assert not checkio("asasasasasasasaas"), "3rd example"
    assert not checkio("QWERTYqwerty"), "4th example"
    assert not checkio("123456123456"), "5th example"
    assert checkio("QwErTy911poqqqq"), "6th example"
    print("Challenge Complete!")
