import os


# ####### A ########

# Get the folder containing the current file
current_folder = os.path.dirname(os.path.abspath(__file__))

# define file path
file_path = "data.txt"

# initialize two empty lists
reports = []

# read file
with open(os.path.join(current_folder, file_path), "r") as file:
    for line in file:

        # split the line
        reports.append(list(map(int, line.split())))

res = 0

for report in reports:
    isIncreasing = (report[0] < report[1])
    found = True

    for i in range(len(report)-1):
        if abs(report[i]-report[i+1]) > 3:
            found = False
            break

        if isIncreasing and report[i] >= report[i+1]:
            found = False
            break

        if not isIncreasing and report[i] <= report[i+1]:
            found = False
            break

    if found:
        res += 1

print(res)

res = 0


# ####### B ########
# Function to check if a report is safe
def is_safe(report):
    isIncreasing = report[0] < report[1]
    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3 or \
           (isIncreasing and report[i] >= report[i + 1]) or \
           (not isIncreasing and report[i] <= report[i + 1]):
            return False
    return True


# Function to check if a report can be made safe by removing one level
def can_be_made_safe(report):
    for i in range(len(report)):
        # Create a modified report by removing the current level
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


# Count safe reports considering the Problem Dampener
res = 0
for report in reports:
    if is_safe(report) or can_be_made_safe(report):
        res += 1

print(res)
