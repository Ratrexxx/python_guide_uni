# Un alumno desea saber cuál será su calificación final en la materia Programación I.
# Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales
# 30% de la calificación del examen final, 15% de la calificación de un trabajo final.

def get_valid_score(prompt: str) -> float:
    while True:
        score = float(input(prompt))
        if 0.1 <= score <= 5:
            return score
        else:
            print("Invalid score. Please enter a value between 0.1 and 5.")

first_score = get_valid_score("Please enter the first score: ")
second_score = get_valid_score("Please enter the second score: ")
third_score = get_valid_score("Please enter the third score: ")

average_score = (first_score + second_score + third_score) / 3

final_exam_score = get_valid_score("Please enter the final exam score: ")

final_work_score = get_valid_score("Please enter the final work score: ")

final_score = (average_score * 0.55) + (final_exam_score * 0.30) + (final_work_score * 0.15)

print(f"The final score will be: {final_score:.2f}")

