def enter_quit():
    user = input("Enter a number or QUIT to quit: ")
    all_nums = []
    even_numbers = []

    while user != "QUIT":

        all_nums.append(int(user))
        user = input("Enter a number or QUIT to quit: ")

    print("All Numbers: ", all_nums)

    for num in all_nums:
        if num % 2 == 0:
            even_numbers.append(num)

    print("Even Numbers: ", even_numbers)

