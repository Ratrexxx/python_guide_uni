from utils import get_float_input

def solution():
    base = get_float_input("Please enter the base of the triangle: ", min_value=0)
    height = get_float_input("Please enter the height of the triangle: ", min_value=0)

    area = (base * height) / 2

    print(f"The area of the triangle is: {area:.2f}")

