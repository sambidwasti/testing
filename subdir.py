# testing the subdirectory thingy

import os

print("hello World")
for dirs in os.walk("./learning_sphinx"):
    print(dirs)