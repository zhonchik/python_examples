
def is_palindrome(s: str) -> bool:
    middle = len(s) // 2
    head = s[:middle]
    tail = s[:-(middle + 1):-1]
    for left, right in zip(head, tail):
        if left != right:
            return False
    return True
