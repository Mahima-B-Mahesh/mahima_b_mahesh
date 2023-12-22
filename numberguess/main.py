import random
def main():
    while True:
        print("Enter the limit upto which you want to guess: ",end="")
        while True:
            try:
                number = int(input())
            except ValueError:
                print("Please enter a Number: ",end="")
            else:
                if number <= 100:
                    print("Please enter a number greater than Hundred: ", end= "")
                else:
                    break

        random_number = random.randint(0,number)
        guesses = guesser(random_number)
        if guesses < 20:
            print(f"You won in {guesses} guesses")
            score = score_calculator(guesses)
            if score >= 10:
                print(f"Congrats! You scored {score}")
            else:
                print(f"You scored {score}. Try more next time :)")
        exit_code()

def exit_code():
    code = input("Type 0 to exit\nType 1 to play again\n")
    if code == "0":
        quit()
    elif code == "1":
        pass
        

def guesser(random_number):
    guesses = 0
    guess = 0
    while True:
        guesses += 1
        if guesses == 20:
            print("You reached the maximum number of guesses :(")
            print("Try again next time")
            break
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter a number")
        else:
            if guess == random_number:
                print("You Won!")
                break
            elif guess < random_number:
                print("You were below the number")
            else:
                print("You were above the number")
    return guesses
        
def score_calculator(num):
    if num <= 5:
        score = 20
    elif num <= 10:
        score = 15
    elif num <= 15:
        score = 10
    else:
        score = 5
    return score    

if __name__ == "__main__":
    main()