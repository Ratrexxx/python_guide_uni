# Una tienda ofrece un descuento del 15% sobre el total de la compra
# Un cliente desea saber cuánto deberá pagar finalmente por su compra.

total_purchase = float(input("Please enter the total amount of your purchase: "))
discount_rate = 0.15

discount = total_purchase * discount_rate

final_amount = total_purchase - discount

print(f"The discount will be: {discount}")
print(f"The final amount to pay will be: {final_amount}")