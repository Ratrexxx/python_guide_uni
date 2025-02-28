from utils import get_float_input

def solution():
    investment = get_float_input("Please enter the amount of money you want to invest: ", min_value=0)
    interest_rate = 0.02
    profit = investment * interest_rate
    total = investment + profit
    
    print(f"The profit after a month will be: {profit:.2f}")
    print(f"The total amount after a month will be: {total:.2f}")