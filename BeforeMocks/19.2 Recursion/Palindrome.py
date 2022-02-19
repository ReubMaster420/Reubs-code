def Palindrome(word):
    word= word.lower()
    length = len(word)
    if length < 2:
        return True
    elif word[0] == word[length- 1]:
        return Palindrome(word[1: length - 1])
    else:
        return False

