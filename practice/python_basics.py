# Day 2: Python core refresher

numbers = [5, 10, 15, 20, 25]

# Print each number and its squares

for n in numbers:
    print(n, n**2)

# TASK A: Create a dictionary

numbers = [2, 4, 6, 8]

squares_dict = {}

for n in numbers:
    squares_dict[n] = n**2

print(squares_dict)

# Task B: student filtering

students = [
    {"name": "Ali", "marks": 78},
    {"name": "Sara", "marks": 85},
    {"name": "Ahmed", "marks": 92},
    {"name": "Ayesha", "marks": 67}
]
high_scores = []

for s in students:
    if s["marks"] > 80:
        high_scores.append(s["name"])

print("High scores :", high_scores)

# Task C: Statistics functions 

def basic_stats(nums):
    total = sum(nums)
    count = len(nums)
    mean = total/count
    minimum = min(nums)
    maximum = max(nums)

    return mean, minimum, maximum


numbers = [2, 4, 6]

mean, minimum, maximum = basic_stats(numbers)

print("mean", mean)
print("minimum", minimum)
print("maximum", maximum)

# Task C: pythonic version
# even_squares = [n**2 for n in range(1, 11) if n % 2 == 0]
# print(even_squares)

even_squares = []
for n in range(1, 11):
    if n % 2 == 0:
        even_squares.append(n**2)
    
print(even_squares)
# Task D: Mini Quizz

employees = [
    {"name":"Usman", "salary": 50000},
    {"name":"Hina", "salary": 75000},
    {"name":"Bilal", "salary": 60000},
]

for e in employees:
    if e["salary"] > 60000:
        print(e["name"])
