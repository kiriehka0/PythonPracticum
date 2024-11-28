def main():
    with open("numbers.num", "rb") as f:
        a = f.read()

    result = 0
    for i in range(0, len(a), 2):
        result += int.from_bytes(a[i: i + 2], "big")
    result = result % 2**16

    print(result)


if __name__ == "__main__":
    main()
