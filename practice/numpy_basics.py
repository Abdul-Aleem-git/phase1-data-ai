import numpy as np

# Making numpy array

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Type:", type(arr))

# Basic operations

print("Add 5:", arr + 5)
print("Multiply 2", arr * 2)

# Mean, Minimum, Maximum

print("Mean:", arr.mean())
print("Minimum:", arr.min())
print("Maximum:", arr.max())

# Difference between Python List and Numpy

numbers = [10,20, 30, 40, 50]

# Python result

python_list_result = [n * 2 for n in numbers]
print("Python result:", python_list_result)

# Numpy result

np_list_result = arr * 2
print("Numpy Result:", np_list_result)

# Data cleaning 

data = np.array([10, 20, np.nan, 40, 50])

print("Data:", data)
print("Mean data(no nan):", np.nanmean(data))
