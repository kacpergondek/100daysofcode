import random 

class Question:

    def __init__ (self, q_text, q_right_answer, q_all_answers):
        self.text = q_text
        self.right_answer = q_right_answer
        self.all_answers = q_all_answers

class Quiz:

    def __init__ (self, q_list):
        self.question_list = q_list
        self.score = 0
        self.question_number = 0

    #Check if there are any remaining questions
    def checkRemaining(self):
        return self.question_number < len(self.question_list)

    #Print the currect question
    def printQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input (f"Q.{self.question_number}: {current_question.text}\n1.{current_question.all_answers[0]} \n1.{current_question.all_answers[1]}\n2.{current_question.all_answers[2]}\n3.{current_question.all_answers[3]}\n")
        self.checkAnswer(user_answer, current_question.right_answer)


    #Check the answer  
    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That is correct")
        else:
            print("That is not correct")
            print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")

    