def row_and_column():
    row = int(input("Enter a row number from 1 to 5: "))
    col = int(input("Enter a column number from 1 to 5: "))

    for i in range(1,6):
        for j in range(1,6):
            if i == row and j == col:
                print("1", end = " ")
            else:
                print("0", end = " ")
        print()
        
