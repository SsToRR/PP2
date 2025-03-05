from functools import reduce
from operator import mul
import time
import math
def true(elements):
    return all(elements)

print(true((True, True, True)))
print(true((True, False, True)))