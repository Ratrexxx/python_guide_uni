from utils import get_float_input

def solution():
    foots = get_float_input("Please enter the amount of foots you want to convert: ", min_value=0)

    yards = foots / 3
    inches = foots * 12
    centimeters = inches * 2.54
    meters = centimeters / 100

    print(f"{foots:.2f} foots are equivalent to:")
    print(f"{yards:.2f} yards")
    print(f"{inches:.2f} inches")
    print(f"{centimeters:.2f} centimeters")
    print(f"{meters:.2f} meters")