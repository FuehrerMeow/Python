#
# Magic 8 ball
# Write a function that returns a random answer to a user’s question
# Question: user input
# Answer: saved in list, taken out at random

import random

answer_list = ["You will die in seven days.", "REDRUM", "Try again later.",
               "Why are you asking a plastic ball?", "Goodbye", "Looking like a solid no.",
               "Don't panic!", "Definitely maybe.",
               "Incorrect syntax!", "RUN!", "The answer you are looking for is... Yes?", "Generic response",
               "Not a chance.", "You wish!", "I don't know, ask a magic ball.", "Your Mom!"]

question = input("Please ask a question: ")
answer = random.choice(answer_list)

def give_answer():
   return random.choice(answer_list)

print(give_answer())
