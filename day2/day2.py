with open("input.txt") as f:
    horizontal = 0
    vertical = 0
    for cmd, amt in [line.strip().split() for line in f.readlines()]:
        amt = int(amt)
        if cmd == "forward":
            horizontal += amt
        elif cmd == "down":
            vertical += amt
        else:
            vertical -= amt
    print(horizontal * vertical)

with open("input.txt") as f:
    horizontal = 0
    aim = 0
    depth = 0
    for cmd, amt in [line.strip().split() for line in f.readlines()]:
        amt = int(amt)
        if cmd == "forward":
            horizontal += amt
            depth += aim * amt
        elif cmd == "down":
            aim += amt
        else:
            aim -= amt
    print(horizontal * depth)
