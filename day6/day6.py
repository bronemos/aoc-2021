with open("input.txt") as f:
    day_1 = list(map(int, f.readline().strip().split(",")))
fish = {k: day_1.count(k) for k in range(0, 9)}
for _ in range(256):
    zero_cnt = fish[0]
    for k in range(1, 9):
        fish[k - 1] = fish[k]
    fish[8] = zero_cnt
    fish[6] += zero_cnt

print(sum(fish.values()))
