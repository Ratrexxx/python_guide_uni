# Suponga que un individuo desea invertir su capital en un banco
# y desea saber cuanto dinero ganara después de un mes si el banco
# paga a razón de 2% mensual

investment = float(input("Please enter the amount of money you want to invest: "))
interest_rate = 0.02
profit = investment * interest_rate
total = investment + profit

print(f"The profit after a month will be: {profit}")
print(f"The total amount after a month will be: {total}")