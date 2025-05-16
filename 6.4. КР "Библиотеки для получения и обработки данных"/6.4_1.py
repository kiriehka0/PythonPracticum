import math
import sys


def f(x):
    numerator = (math.sin(x - math.pi) *
                 math.cos(x + 2 * math.pi) *
                 math.sin(4 * math.pi - x))

    denominator = (math.sin(math.pi / 2 + x) *
                   (1 / math.tan(2 * math.pi - x)) *
                   (1 / math.tan(3 * math.pi / 2 + x)))

    if denominator == 0:
        return float('inf')

    return numerator / denominator


for line in sys.stdin:
    x = float(line)
    result = f(x)
    print(f"{result:.3f}")
