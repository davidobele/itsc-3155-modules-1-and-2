def common_values():
    list_one = []
    list_two = []

    for i in range(5):
        num = int(input("Enter a number for the first list: "))
        list_one.append(num)

    for i in range(5):
        num = int(input("Enter a number for the second list: "))
        list_two.append(num)
    

    print("First List:", list_one)
    print("Second List:", list_two)
    print("Common List:", list(set(list_one) & set(list_two)))


