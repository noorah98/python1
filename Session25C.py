import numpy as np

numbers = [1, 1, 1, 1, 1, 1, 1, 1]
array1 = np.ones(8)

array2 = np.zeros(8)

array3 = np.array(numbers)

print(array1)
print()
print(array2)
print()
print(array3)

print(array1.shape)  # takes less time
print(array2.shape)
print(array3.shape)

print(len(array1))   # takes more time

# reshaping
# but, shape must be even

array = array1.reshape(2, 2, 2)
print(array)
print(array.shape)

print()

originalArray = array.ravel()
print(originalArray)
print(originalArray.shape)


# explore : reshape function