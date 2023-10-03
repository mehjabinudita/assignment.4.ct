def calculate_grade(score):
    if score < 0 or score > 100:
        return "Error, please enter a numeric input between 0 and 100"
    elif score >= 90:
        return "Grade is A"
    elif score >= 80:
        return "Grade is B"
    elif score >= 70:
        return "Grade is C"
    elif score >= 60:
        return "Grade is D"
    else:
        return "Grade is F"

while True:
    user_input = input("Enter a score between 0 and 100: ")
    
    try:
        score = float(user_input)
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(grade)
        else:
            print("Error, please enter a numeric input between 0 and 100")
    except ValueError:
        print("Error, please enter a numeric input between 0 and 100")