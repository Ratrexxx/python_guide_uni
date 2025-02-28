from utils import get_float_input

def solution():
    number = get_float_input("Please enter a number: ")
    square = number ** 2
    cube = number ** 3

    print(f"The square of the number is: {square:.2f}")
    print(f"The cube of the number is: {cube:.2f}")