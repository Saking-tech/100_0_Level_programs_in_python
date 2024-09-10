# Program to create a simple quiz game

# Define questions and answers
quiz = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
}

# Initialize score
score = 0

# Ask questions
for question, correct_answer in quiz.items():
    answer = input(f"{question} ")
    if answer.lower() == correct_answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}")

# Display the final score
print(f"\nYour final score is {score}/{len(quiz)}")
