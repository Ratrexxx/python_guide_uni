from utils import get_float_input

def solution():
    base_salary = get_float_input("Please enter the base salary: ", min_value=0)
    commission_rate = 0.10
    
    sale1 = get_float_input("Please enter the amount of the first sale: ", min_value=0)
    sale2 = get_float_input("Please enter the amount of the second sale: ", min_value=0)
    sale3 = get_float_input("Please enter the amount of the third sale: ", min_value=0)
    total_sales = sale1 + sale2 + sale3
    
    commission = total_sales * commission_rate
    total = base_salary + commission
    
    print(f"The commission for the three sales will be: {commission:.2f}")
    print(f"The total amount after a month will be: {total:.2f}")