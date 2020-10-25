from palindrome import is_palindrome

def test_is_palindrome_1():
    assert is_palindrome('a')


def test_is_palindrome_2():
    assert is_palindrome('aa')
    assert not is_palindrome('ab')


def test_is_palindrome_3():
    assert is_palindrome('aba')
    assert not is_palindrome('abc')


def test_is_palindrome_4():
    assert is_palindrome('abba')
    assert not is_palindrome('abcd')


def test_is_palindrome_5():
    assert is_palindrome('abcba')
    assert not is_palindrome('abcde')
