import numpy as np

# arr = np.array([10, 20, 30])
# print(arr.dtype)

# arr_float = np.array([10, 20, 30], dtype='float64')
# print(arr_float.dtype)

# student_dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('marks', 'f4')])

# students = np.array([
#     ('Arush', 21, 14.4),
#     ('Aryan', 34, 45)
# ], dtype=student_dtype)

# print(students)
# print(students['name'])
# print(students['marks'])

# This is used to print the uninitialized array
# arr = np.empty((2, 3))
# print(arr)

# This is used to create a matrix of zeroes and ones which we can use it for adding the padding in the images
# zero_arr = np.zeros([3,2])
# ones_arr = np.ones([1,3])
# print(zero_arr)
# print(ones_arr)

# It is used to create an numpy array we use it because it more faster
# list = [1, 2, 3]
# arr = np.asarray(list)
# print(arr.dtype)

# It includes the first number and exclude the last number
# arange(start,end,step)
# arr = np.arange(0, 11, 5)
# print(arr)

# arr = np.linspace(0 , 5, 10)
# print(arr)

# arr = np.logspace(1, 3, 5)
# print(arr)

# arr = np.array([1, 4, 9, 16])
# # It is used to give the square root of the given number
# print(np.sqrt(arr))
# print(np.exp(arr))
# #It is used to give the square of the number
# print(np.power(arr, 2))

# angles = np.array([0, np.pi/2, np.pi])

# print(np.sin(angles))
# print(np.cos(angles))
# print(np.tan(angles))

arr = np.array([1.1234, 2.678, 3.999])
print(np.round(arr, 2))
print(np.floor(arr))
print(np.ceil(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.argmin(arr))

# arr = np.array([-1, 10, 12, 3, -4, 5])

# print(np.mean(arr))
# print(np.median(arr))
# print(np.average(arr))

# print(np.sort(arr))
# print(np.argsort(arr))
# print(np.where(arr > 5))

# The main difference between this two is the 'view' make changes directly into the main array
# even if we call the main variable
# arr = np.array([10, 20, 30])
# view_arr = arr.view()
# copy_arr = arr.copy()

# view_arr[0] = 100
# copy_arr[1] = 0
# print(arr)
# print(copy_arr)

# [2 1]
# [3 4]
# mat = np.matrix([[2, 1], [3, 4]])
# arr = np.array([[2, 1], [3, 4]])
# print(mat)
# print(mat.T)
# print(mat.I)
# print(np.linalg.det(mat))
# print(np.linalg.inv(arr))
# print(np.linalg.eigvals(mat))

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[2, 0], [1, 3]])
# print(np.dot(A, B))
# print(A @ B)