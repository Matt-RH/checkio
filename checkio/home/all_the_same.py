from typing import Any, List


def all_the_same(elements: List[Any]) -> bool:
    """
    In this mission you should check if all elements in the given list
    are equal.

    Input: List.
    Output: Bool.
    """

    return all([True if x == elements[0] else False for x in elements])


if __name__ == "__main__":
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1])
    assert not all_the_same([1, 2, 1])
    assert all_the_same(["a", "a", "a"])
    assert all_the_same([])
    assert all_the_same([1])
    print("Challenge Complete!")
