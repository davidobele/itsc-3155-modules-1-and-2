def calculate_grade():
    grade = int(input("Enter a grade from 0 to 100: "))

    if grade >= 90:
        return "Your grade is an A"
    elif grade >= 80:
        return "Your grade is a B"
    elif grade >= 70:
        return "Your grade is a C"
    elif grade >= 60:
        return "Your grade is a D"
    else:
        return "Your grade is a F"
