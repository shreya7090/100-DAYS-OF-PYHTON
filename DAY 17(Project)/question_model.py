#Creates Question objects from the data (question_model.py).
'''
We use a class because we need a structured way to store each question's text and answer.
A class is like a blueprint for creating question objects.
'''

class Question:

    def __init__(self, q_text, q_answer): 
        self.text = q_text #text → Holds the question
        self.answer = q_answer #answer → Holds the correct answer

'''
What's happening here?
1.class Question: → Creates a blueprint (class) for all questions.
2.__init__() method (Constructor)
    Runs automatically when we create a new Question object.
    Takes two inputs: q_text (question text) and q_answer (correct answer).
    Stores them in self.text and self.answer so they can be used later.
'''