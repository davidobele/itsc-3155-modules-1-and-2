def split():
    sentence = str(input("Enter a string: "))

    new_list = [sentence[i:i+3] for i in range(0, len(sentence), 3)]
    #Online resource: ChatGPT code splits inputted string into three parts 
    print(new_list)
   
