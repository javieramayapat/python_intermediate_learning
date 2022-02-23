def check_palindrome(string: str) -> bool:
    """Check palindrome word

    Args:
        string (str): String to check

    Returns:
        bool: Result of comparation
    """
    assert len(string) > 0, 'A empty string is no acceptable'
    assert string, 'The function check_palindrome only recieve strings'
    return string == string[::-1]


def run():
    string = input('Write a word an validate if it is a palindrome: ')
    result = check_palindrome(string)
    print(result)


if __name__ == '__main__':
    run()
