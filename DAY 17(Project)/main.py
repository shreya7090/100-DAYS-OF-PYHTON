#The main file main.py puts everything together and executes the game.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#Imports the necessary modules.

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    #Converts raw question data into Question objects.
    #Stores them in a list (question_bank).

quiz = QuizBrain(question_bank)
#Creates an instance of QuizBrain using question_bank.

while quiz.still_has_questions():
    quiz.next_question()
    #Loops through all questions and asks them one by one.

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
#Shows a completion message and final score.