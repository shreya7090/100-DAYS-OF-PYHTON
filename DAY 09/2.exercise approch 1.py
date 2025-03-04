student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def assign_grade(score):
    if 90 <= score <= 100:
        return"Outstanding"
    elif 81 <= score <=90:
        return"Exceeds Expectations"
    elif 71 <= score <= 80:
        return"Acceptable"
    else:
        return"Fail"

student_grade = {}
for student , score in student_scores.items():
    student_grade[student] = assign_grade(score)

for student,grade in student_grade.items():
    print(f"{student}: {grade}")



'''
Error details
Failed to import test module: evaluate
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.10/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "/eval/evaluate.py", line 3, in <module>
    from exercise import student_grades
ImportError: cannot import name 'student_grades' from 'exercise' (/eval/exercise.py)
'''