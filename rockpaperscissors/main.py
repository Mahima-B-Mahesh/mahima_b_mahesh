import random
from time import sleep
from clear import clear
from anim import loading_animation

def main():
    choices = ["Rock", "Paper", "Scissors"] 
    print("Welcome!")
    user_score = 0
    computer_score = 0
    times = 10
    while True:
        user_choice = input("1.Rock 2.Paper 3.Scissors    ").title().strip()
        computer_choice = random.choice(choices)
        print(computer_choice)
        sleep(1)
        times -= 1
        if (user_choice == "1" and computer_choice == "Paper") or (user_choice == "2" and computer_choice == "Scissors") or (user_choice == "3" and computer_choice == "Rock"):
            print("I won")
            computer_score += 1
            print(f"[You: {user_score}     Me: {computer_score}]     Chances Left: {times}")
        elif (user_choice == "1" and computer_choice == "Scissors") or (user_choice == "2" and computer_choice == "Rock") or (user_choice == "3" and computer_choice == "Paper"):
            print("You won")
            user_score += 1
            print(f"[You: {user_score}     Me: {computer_score}     Chances Left: {times}]")
        else:
            print("Tie")
            print(f"[You: {user_score}     Me: {computer_score}     Chances Left: {times}]")
        
        if times == 0:
            break
        sleep(1)
        clear()
    clear()
    print("Calculating Scores", end = "")
    loading_animation()
    loading_animation()
    print()
    print(f"You Scored {user_score} and I scored {computer_score}")
    sleep(1)
    if computer_score > user_score:
        print("You Lost.")
        print("Try Again!")
    elif computer_score < user_score:
        print("You Won!")
        print("Congrats!")
    else: 
        print("Aww! We both share prize ;)")
    
    
if __name__ == "__main__":
    main()