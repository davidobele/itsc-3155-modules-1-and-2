def five_words():

    word_list = []
    sentence = ""
    for i in range(5):
        word = str(input("Enter a word: "))
        word_list.append(word)
        
    for w in word_list:
        sentence += w + " "

    print("Words: ", word_list)
    print(sentence)