import os


def clear():
    # Clear screen command for Windows
    if os.name == "nt":
        os.system("cls")
    # Clear screen command for Unix/Linux/MacOS
    else:
        os.system("clear")


if __name__ == "__main__":
    clear()
