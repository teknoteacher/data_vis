# creates a text file with 2 million bits to illustrate what 2 Megabits might look like

import random

with open("2Mb_visual.txt", "w") as myfile:
    for size in range (2000000):
        bit = random.randint(0,1)
        myfile.write(str(bit))

print("Done")
