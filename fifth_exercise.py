
#Un profesor desea saber qué porcentaje de hombres
# y que porcentaje de mujeres hay en un grupo de estudiantes.

girls_amount = int(input("Please enter the amount of girls in the group: "))
boys_amount = int(input("Please enter the amount of boys in the group: "))

total_students = girls_amount + boys_amount

girls_percentage = girls_amount / total_students * 100
boys_percentage = boys_amount / total_students * 100

print(f"The percentage of girls in the classroom is {girls_percentage:.2f}%")
print(f"The percentage of boys in the classroom is {boys_percentage:.2f}%")