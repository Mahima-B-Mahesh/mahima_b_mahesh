import sys
import time
def main():
    n = 4
    string = input("Text: ")
    blink(string,n)
def blink(string,n):
    i = 0
    while i < 4:
        # Print the text in blinking style
        sys.stdout.write(f"\033[5m{string}\033[0m")
        sys.stdout.flush()
        time.sleep(0.5)
        # Clear the text
        sys.stdout.write("\033[2K\033[1G")
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1

    """except KeyboardInterrupt:
        pass

    finally:
        # Reset the terminal
        sys.stdout.write("\033[0m\033[2K\033[1G")
        sys.stdout.flush()"""


if __name__ == "__main__":
    main()