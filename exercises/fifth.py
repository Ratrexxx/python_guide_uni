from utils import get_int_input

def solution():
    girls_amount = get_int_input("Please enter the amount of girls in the group: ", min_value=0)
    boys_amount = get_int_input("Please enter the amount of boys in the group: ", min_value=0)

    total_students = girls_amount + boys_amount
    
    if total_students == 0:
        print("Error: The total number of students cannot be zero.")
        return
        
    girls_percentage = girls_amount / total_students * 100
    boys_percentage = boys_amount / total_students * 100

    print(f"The percentage of girls in the classroom is {girls_percentage:.2f}%")
    print(f"The percentage of boys in the classroom is {boys_percentage:.2f}%")
