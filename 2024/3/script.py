import os
import re

# ####### A ########

# Get the folder containing the current file
current_folder = os.path.dirname(os.path.abspath(__file__))

# define file path
file_path = "data.txt"

# initialize two empty lists
lines = []

# read file
with open(os.path.join(current_folder, file_path), "r") as file:
    for line in file:

        # split the line
        lines.append(line)

res = 0

for line in lines:
    x = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)

    for found in x:
        nums = list(map(int, found[4:-1].split(',')))
        res += nums[0]*nums[1]

print(res)


# ####### B ########
res = 0
start = 1

for line in lines:
    dos = [match.start() for match in re.finditer(r"do\(\)", line)]
    donts = [match.start() for match in re.finditer(r"don't\(\)", line)]
    check = [0] * len(line)
    check[0] = start

    for i in dos:
        check[i] = 1

    for i in donts:
        check[i] = -1

    for i in range(len(line)-1):
        if check[i+1] == 0:
            check[i+1] = check[i]

    start = check[-1]

    x = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', line)

    for match in x:
        if check[match.start()] == 1:
            nums = list(map(int, match.group(0)[4:-1].split(',')))
            res += nums[0]*nums[1]

print(res)
