a = float(input())
b = float(input())
c = float(input())
if a == b and b == c and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    print(f"{-(c / b):.2f}")
elif a == b and b == 0:
    print("No solution")
elif a == c and c == 0:
    print("No solution")
else:
    d = (b ** 2) - (4 * a * c)
    if d == 0:
        print(f"{(-b) / (2 * a):.2f}")
    elif d > 0:
        x1 = (-b - (d ** 0.5)) / (2 * a)
        x2 = (-b + (d ** 0.5)) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
    else:
        print("No solution")