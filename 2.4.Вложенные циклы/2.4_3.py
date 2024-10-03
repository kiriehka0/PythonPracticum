for i in range(1, x := int(input()) + 1):
    if i in (sum(range(j)) for j in range(x)):
        print(i)
    else:
        print(i, end=' ')
