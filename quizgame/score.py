from anim import loading_animation
from clear import clear
def main():
    score = 5
    score_calculator(score)

def score_calculator(score):
    print("Calculating scores",end = "")
    loading_animation()
    loading_animation()
    print()
    clear()
    match score:
        case 0 | 1 | 2:
            print(f"You scored {score} out of 5")
            print("Try more next time :)")
        case 3 | 4:
            print(f"You scored {score} out of 5")
            print("Good!")
        case 5:
            print(f"You scored {score} out of 5")
            print("Excellent!")
            
    
if __name__ == "__main__":
    main()