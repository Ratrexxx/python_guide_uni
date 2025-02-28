from utils import get_float_input

def solution():
    total_purchase = get_float_input("Please enter the total amount of your purchase: ", min_value=0)
    discount_rate = 0.15
    
    discount = total_purchase * discount_rate
    
    final_amount = total_purchase - discount
    
    print(f"The discount will be: {discount:.2f}")
    print(f"The final amount to pay will be: {final_amount:.2f}")