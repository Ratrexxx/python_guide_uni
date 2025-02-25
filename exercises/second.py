def solution():
    base_salary = float(input("Please enter the base salary: "))
    commission_rate = 0.10

    sale1 = float(input("Please enter the amount of the first sale: "))
    sale2 = float(input("Please enter the amount of the second sale: "))
    sale3 = float(input("Please enter the amount of the third sale: "))
    total_sales = sale1 + sale2 + sale3

    commission = total_sales * commission_rate
    total = base_salary + commission

    print(f"The commission for the three sales will be: {commission}")
    print(f"The total amount after a month will be: {total}")