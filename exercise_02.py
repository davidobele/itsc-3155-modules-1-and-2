def suffix_finder():
    word1 = str(input("Enter a string: "))
    word2 = str(input("Enter another string: "))
    return word1.endswith(word2) or word2.endswith(word1)
