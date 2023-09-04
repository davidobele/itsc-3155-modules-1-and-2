def appear_twice():

    orig_list = []
    new_list = []

    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        orig_list.append(num)

    print("Original list", orig_list)

    new_list = [num for num in orig_list if orig_list.count(num) == 1]


    print("Names that appear once", new_list)