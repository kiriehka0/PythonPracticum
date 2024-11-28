from sys import stdin

inf = [x.split() for x in stdin]
sr_1 = sum([int(i[1].strip("\n")) for i in inf]) / len([int(i[1].strip("\n")) for i in inf])
sr2 = sum([int(i[2].strip("\n")) for i in inf]) / len([int(i[2].strip("\n")) for i in inf])
print(round(sr2 - sr_1))
