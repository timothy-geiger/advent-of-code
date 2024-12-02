import os
from collections import Counter


# ####### A ########

# Get the folder containing the current file
current_folder = os.path.dirname(os.path.abspath(__file__))

# define file path
file_path = "data.txt"

# initialize two empty lists
list1 = []
list2 = []

# read file
with open(os.path.join(current_folder, file_path), "r") as file:
    for line in file:

        # split the line into two numbers
        num1, num2 = map(int, line.split())

        # append the numbers to their respective lists
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()

res1 = sum([abs(a-b) for a, b in zip(list1, list2)])
print(res1)


# ####### B ########
cnt_dict = Counter(list2)
res2 = 0

for num in list1:
    res2 += num * cnt_dict[num]

print(res2)
