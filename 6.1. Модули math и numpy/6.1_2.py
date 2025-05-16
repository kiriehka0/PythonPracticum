import math
import sys


def main():
    for line in sys.stdin:
        numbers = list(map(int, line.split()))
        print(math.gcd(*numbers))


if __name__ == "__main__":
    main()
