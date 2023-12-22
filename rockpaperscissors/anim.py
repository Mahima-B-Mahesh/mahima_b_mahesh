import time
import sys


def loading_animation():
    for i in range(4):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    return ""


if __name__ == "__main__":
    loading_animation()
