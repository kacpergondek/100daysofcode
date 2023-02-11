from objects import Quiz,Question
from question_bank import questions

question_data = []
for question in questions:
    question_question = question["question"]
    question_answer = question["correct_answer"]
    question_all_answers = question["all_answers"]

    new_question = Question(question_question, question_answer, question_all_answers)
    question_data.append(new_question)

quiz = Quiz(question_data)

while quiz.checkRemaining():
    quiz.printQuestion()

print(f"You have now completed the Quiz, with a total score of {quiz.score}/{quiz.question_number}")