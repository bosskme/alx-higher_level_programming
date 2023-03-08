#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        if i == 0 and j == 1:
            print("{:02d}".format(j), end='')
        else:
            print(", {:02d}".format(j), end='')
    if i < 9:
        print("", end='')
print("\n", end='')
