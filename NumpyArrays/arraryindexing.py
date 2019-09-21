import numpy as np 

arr = np.random.randint(0, 20, 15)
print("Initial array")
print(arr)
print("\n\n")
#Indexing a 1D array 
print("Indexing a 1D array")
print(arr[2])
print(arr[3])
print(arr[5])
print(arr[6])
print("\n\n")
#Indexing like slices
print("Indexing like slices")
print(arr[2:])
print(arr[1:8])
print(arr[:])
print("\n\n")
#Working with 2D arrays indexing
print("Working with 2D arrays indexing")
arr = arr.reshape(3, 5)
print("\n\n")
#original 2D numpy matrix
print("original 2D numpy matrix")
print(arr)
print("\n\n")
#Indexing particular rows and columns
print("Indexing particular rows and columns")
print(arr[2][3])
print(arr[2, 4])
print("\n\n")
#Indexing a group of rows and columns
print("Indexing a group of rows and columns")
#select first 2 rows and all columns
print("select first 2 rows and all columns")
print(arr[:2])
print("\n\n")
#select first 2 columns and all rows
print("select first 2 columns and all rows")
print(arr[:, :2])
print("\n\n")
#all rows all columns
print("all rows all columns")
print(arr[:,:])
print("\n\n")
#another way
print("another way")
print(arr[:][:])

print("\n\n")