# Define a list of questions and answers
questions = [
    {
        "question": "What is the capital of telangana?",
        "answer": "hyderabad"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "answer": "Blue whale"
    }
]

# Initialize score
score = 0

# Iterate over each question
for i, qna in enumerate(questions, start=1):
    print(f"Question {i}: {qna['question']}")
    user_answer = input("Your answer: ")
    if user_answer.lower() == qna['answer'].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {qna['answer']}\n")

# Print final score
print(f"Your score: {score}/{len(questions)}")
