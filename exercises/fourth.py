from utils import get_float_input

def solution():
    def get_valid_score(prompt: str) -> float:
        return get_float_input(prompt, min_value=0.1, max_value=5)

    first_score = get_valid_score("Please enter the first score: ")
    second_score = get_valid_score("Please enter the second score: ")
    third_score = get_valid_score("Please enter the third score: ")

    average_score = (first_score + second_score + third_score) / 3

    final_exam_score = get_valid_score("Please enter the final exam score: ")

    final_work_score = get_valid_score("Please enter the final work score: ")

    final_score = (average_score * 0.55) + (final_exam_score * 0.30) + (final_work_score * 0.15)

    print(f"The final score will be: {final_score:.2f}")

