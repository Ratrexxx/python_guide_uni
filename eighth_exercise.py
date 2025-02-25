# Escribir un programa de desglose cierta cantidad de segundos introducida
# por teclado en su equivalente en semanas, días, horas, minutos y segundos.

def get_valid_seconds(prompt: str) -> int:
    while True:
        seconds = int(input(prompt))
        if seconds > 0:
            return seconds
        else:
            print("Invalid seconds. Please enter a positive number.")

seconds = get_valid_seconds("Please enter the amount of seconds you want to break down: ")
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
weeks = days // 7

print(f"{seconds} seconds are equivalent to:")
print(f"{seconds} seconds")
print(f"{minutes} minutes")
print(f"{hours} hours")
print(f"{days} days")
print(f"{weeks} weeks")