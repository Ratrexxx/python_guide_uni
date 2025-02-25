from exercises import first, second, third, fourth, fifth, sixth, seventh
from descriptions import descriptions

def run_exercise(number, solution, description):
    try:
        print(f"\nExercise {number}")
        print("-" * 80)
        print(description)
        print("-" * 80)
        solution()
    except Exception as e:
        print(f"Error in exercise {number}: {str(e)}")

def main():
    exercise_map = {
        1: first.solution,
        2: second.solution,
        3: third.solution,
        4: fourth.solution,
        5: fifth.solution,
        6: sixth.solution,
        7: seventh.solution
    }
    
    exercise_descriptions = descriptions()
    
    for number, solution in exercise_map.items():
        run_exercise(
            number=number,
            solution=solution,
            description=exercise_descriptions[number - 1]
        )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Program terminated with error: {str(e)}")