import random

"""
Cheklovlar:
    -10 <= a, b <= 10
"""

def f(a, b):
    return a + b

nums = []
for i in range(10):
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    nums.append((a, b, f(a, b)))

