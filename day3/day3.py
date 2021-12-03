from copy import deepcopy

with open("input.txt") as f:
    readlines = f.readlines()

# pt1 

gamma = int("".join(["1" if bit_arr.count("1") >= 500 else "0" for bit_arr in list(map(list, zip(*[[bit for bit in x.strip()] for x in readlines])))]), 2)
print(gamma*(gamma^int("1"*12, 2)))

# pt2

most_common_numbers = [x.strip() for x in readlines]
least_common_numbers = deepcopy(most_common_numbers)
mc_id = 0
lc_id = 0
while len(most_common_numbers) != 1:
    most_common_bit = "1" if [number[mc_id] for number in most_common_numbers].count("1") >= len(most_common_numbers) / 2 else "0"
    most_common_numbers = [number for number in most_common_numbers if number[mc_id] == most_common_bit]
    mc_id += 1

while len(least_common_numbers) != 1:
    least_common_bit = "1" if [number[lc_id] for number in least_common_numbers].count("1") < len(least_common_numbers) / 2 else "0"
    least_common_numbers = [number for number in least_common_numbers if number[lc_id] == least_common_bit]
    lc_id += 1

print(int(most_common_numbers[0], 2) * int(least_common_numbers[0], 2))


