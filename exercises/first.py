def solution():
    investment = float(input("Please enter the amount of money you want to invest: "))
    interest_rate = 0.02
    profit = investment * interest_rate
    total = investment + profit

    print(f"The profit after a month will be: {profit}")
    print(f"The total amount after a month will be: {total}")