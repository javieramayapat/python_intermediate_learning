def run():
    word = input("write a word: ")
    palindrome = lambda string: string == string[::-1]
    print(palindrome(word))


if __name__ == '__main__':
    run()