import math
print(math.sqrt(16))

from math import sqrt, pi
print(sqrt(25))

import random

number = random.randint(1,50)
choice = random.choice(["Mingo", "Panda", "Poppy", "Moo Moo"])

print(number)
print(choice)

import os

current_dir = os.getcwd()
print(f"current directory {current_dir}")

import pandas as pd

data = set([1,2,3])
print(pd.DataFrame(data))



