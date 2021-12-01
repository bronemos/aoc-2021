# PT 1

with open("input.txt") as f:
    measurements = list(map(int, f.readlines()))
    cnt = 0
    for x, y in zip(measurements[:-1], measurements[1:]):
        if y > x:
            cnt +=1
    print(cnt)

# PT 2

with open("input.txt") as f:
    measurements = f.readlines()
    windows = zip(measurements[:-2], measurements[1:-1], measurements[2:])
    sums = [int(x) + int(y) + int(z) for x, y, z in windows]
    cnt = 0
    for x, y in zip(sums[:-1], sums[1:]):
        if y > x:
            cnt +=1
    print(cnt)
