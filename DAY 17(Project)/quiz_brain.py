#Runs the quiz using QuizBrain (quiz_brain.py).
'''
The class QuizBrain is responsible for:
1.Keeping track of the current question number.
2.Asking questions and taking user input.
3.Checking if the user's answer is correct.
4.Updating the score.
'''


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0 #Tracks which question the user is on.
        self.score = 0 # Tracks the user's score.
        self.question_list = q_list #Stores all the questions as a list.

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #Checks if there are more questions left to ask.
    '''
    What's happening?
        1.len(self.question_list) gives the total number of questions.
        2.self.question_number keeps track of how many have been asked.
        3.If question_number is less than total questions, it returns True (meaning we still have more questions to ask).
    Why do we need this?
        Helps decide whether to continue or stop the quiz.

    '''

    def next_question(self):
        #Gets the current question from the list.
        current_question = self.question_list[self.question_number]
        #Moves to the next question after asking this one.
        self.question_number += 1
        #Displays the question and takes user input.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        #Calls check_answer() to see if the answer is correct.
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        #Checks if the user's answer is correct.
        #Updates the score if correct.
        #Shows the correct answer and the current score.

