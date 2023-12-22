from anim import loading_animation
from blink import blink
from clear import clear
from quiz import quiz
import os
import sys
import time

print("\033[1mWelcome to Quiz Game\033[0m")

while True:
    yes_or_no = input("Do you want to start the game?(Yes/No) ").lower().strip()
    if yes_or_no == "yes":
        break
    elif yes_or_no == "no":
        print("Exiting",end = "")
        quit(loading_animation())
blink("Quiz Starts Now",4)
clear()
quiz()