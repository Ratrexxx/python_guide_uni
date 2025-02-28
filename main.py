from exercises import first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth
from descriptions import descriptions
import sys

def run_exercise(number, solution, description):
     print(f"\nExercise {number}")
     print("-" * 80)
     print(description)
     print("-" * 80)
     solution()
       

def main():
    exercise_map = {
        1: first.solution,
        2: second.solution,
        3: third.solution,
        4: fourth.solution,
        5: fifth.solution,
        6: sixth.solution,
        7: seventh.solution,
        8: eighth.solution,
        9: ninth.solution,
        10: tenth.solution
    }
    
    exercise_descriptions = descriptions()
    
    if len(sys.argv) > 1:
        try:
            selected_exercises = [int(arg) for arg in sys.argv[1:]]
            for number in selected_exercises:
                if number in exercise_map:
                    run_exercise(
                        number=number,
                        solution=exercise_map[number],
                        description=exercise_descriptions[number - 1]
                    )
                else:
                    print(f"Exercise {number} not found.")
        except ValueError:
            print("Invalid exercise number. Please provide integers.")
            return
    else:
        for number, solution in exercise_map.items():
            run_exercise(
                number=number,
                solution=solution,
                description=exercise_descriptions[number - 1]
            )

if __name__ == "__main__":
    main()
    