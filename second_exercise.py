# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas
# el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones
# por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones

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