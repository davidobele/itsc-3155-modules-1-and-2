def shift():
    sentence = str(input("Enter a string: "))
    lower = ""
    upper = ""

    for char in sentence:
        if char.islower():
            lower += char
        elif char.isupper():
            upper += char

    new_sentence = lower + upper
    print(new_sentence)

   
