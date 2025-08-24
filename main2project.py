import random

# Event descriptions
Dependence = "We pick out two cards from a standard deck of 52 cards without replacement. Event A is that we pick an Ace on the first draw. Event B is that we pick an Ace on the second draw."
mutually_exclusive = "Suppose we flip a coin ten times. Event A is that we flip all heads on the first five flips. Event B is that we flip all heads on the second five flips."
not_mutually_exclusive = "We roll a dice once. Event A is rolling an odd number. Event B is rolling a number greater than four."
independent = "We roll a fair die twice. Event A is that the first roll is a 6. Event B is that the second roll is a 3."

# Put them into a list
event_lst = [Dependence, mutually_exclusive, not_mutually_exclusive, independent]

def guess_the_type(event):
    print(
        "Guess whether this is a: \n"
        " 1) Dependent \n"
        " 2) Independent \n"
        " 3) Mutually Exclusive \n"
        " 4) Not Mutually Exclusive \n"
    )
    print("Event:", event, "\n")
    answer = int(input("Enter your answer (1-4): "))

    # Check answers with feedback
    if event == Dependence:
        if answer == 1:
            print(" Correct! Drawing without replacement makes the events dependent.\n")
            return 'correct'
        else:
            print(" Wrong. These events are dependent because the first draw affects the second.\n")
            return 'wrong'

    if event == not_mutually_exclusive:
        if answer == 4:
            print("Correct! Rolling an odd number and rolling greater than 4 can overlap (like 5).\n")
            return 'correct'
        else:
            print(" Wrong. These are not mutually exclusive because both can occur together.\n")
            return 'wrong'

# Run the quiz
results = []
for event in event_lst:
    results.append(guess_the_type(event))

# Final check
if all(r == 'correct' for r in results):
    print("\n 🎉 You guessed all the events correctly! Here's some cookies: 🍪🍪🍪 \n")
else:
    print("\n Keep practicing! 💪 \n")
