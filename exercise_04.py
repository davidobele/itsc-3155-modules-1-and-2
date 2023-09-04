from statistics import mean 

def mean_four_numbers():
    number = int(input("Enter a number: "))
    mean_list = []

    for i in range(number):
        sum = float(input("Enter number 1: "))
        mean_list.append(sum)
    
    print("List: ", mean_list)
    Average = mean(mean_list)
    print("Average: ", Average) 

