import os
import random


def randomize():
    dir = os.getcwd()
    names = os.listdir(".")
    random.seed()
    for item in names:
        _, ext = os.path.splitext(item)
        os.rename(os.path.join(dir, item), os.path.join(dir, str(random.uniform(0, len(names))) + ext))


if __name__ == "__main__":
    randomize()