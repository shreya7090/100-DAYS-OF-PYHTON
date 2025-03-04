'''
Life in Weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
**Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!
'''

def life_in_weeks(age):
      
      lifespan = 90
      weeks_in_year = 52

      total_weeks = lifespan * weeks_in_year
      weeks_lived = age * weeks_in_year
      weeks_remaining = total_weeks - weeks_lived

      print(f"You have {weeks_remaining} weeks left.")

life_in_weeks()

'''
You need to modify the function to accept the age as a parameter instead of using input() directly. 
This approach makes it suitable for testing or automated environments where input() is not feasible.
'''

