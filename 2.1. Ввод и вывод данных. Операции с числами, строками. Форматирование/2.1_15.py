n = int(input())
m = int(input())
t = int(input())
minute = n * 60 + m + t
hour = minute // 60
delivery_minute = minute % 60
if hour > 23:
    hour %= 24
if hour < 10:
    if delivery_minute < 10:
        print(f"0{hour}:0{delivery_minute}")
    else:
        print(f"0{hour}:{delivery_minute}")
else:
    if delivery_minute > 10:
        print(f"{hour}:{delivery_minute}")
    else:
        print(f"{hour}:0{delivery_minute}")
