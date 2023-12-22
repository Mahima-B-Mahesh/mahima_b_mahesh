import random

upper = int(input("Enter the upper limit:"))
lower = 1
answer = ""

while answer != "c":
    if lower != upper:
        guess = random.randint(lower, upper)
    else:
        guess = lower
    answer = input(f"Is {guess} lower(L) or higher(H) or correct(C)? ").lower()
    if answer == "h":
        upper = guess - 1
    elif answer == "l":
        lower = guess + 1
    print("lower:",lower,"upper:",upper)

print("Wow! computer guessed your number.")