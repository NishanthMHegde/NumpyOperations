import numpy as np 

arr = np.arange(0, 10)
print("Initial array")
print(arr)
print("\n\n")
#Max
print("Max")
print(arr.max())
print(np.max(arr))
print("\n\n")
#Min
print("Min")
print(arr.min())
print(np.min(arr))
print("\n\n")
#Position of max element
print("Position of Max")
print(arr.argmax())
print(np.argmax(arr))
print("\n\n")
#Position of min element
print("Position of Min")
print(arr.argmin())
print(np.argmin(arr))
print("\n\n")
#Mathematical operations of numpy arrays
print("Mathematical operations of numpy arrays")
bool_arr = arr > 3
print(bool_arr)
print("\n\n")
#another way
bool_arr = arr[arr > 3]
print(bool_arr)
print("\n\n")
print(arr[bool_arr])
print("\n\n")
#group operation
print("group operation")
arr [7:] = 100
print(arr)
print("\n\n")
#Mathematical operations
print("Mathematical operations")
arr = arr + arr 
print(arr)
print("\n\n")
arr = arr - arr
print(arr)
print("\n\n")
arr = np.arange(0, 10)
arr = arr / arr 
print(arr)
print("\n\n")
arr = np.arange(0, 10)
arr = arr * arr 
print(arr)
print("\n\n")
arr = np.arange(0, 10)
arr = arr ** 2
print(arr)
print("\n\n")

arr = np.arange(0, 10)
print(1/arr)

#Trignometric operations
print("Trignometric operations")
arr = np.arange(0, 10)

print(np.sin(arr))
print("\n\n")
print(np.tan(arr))
print("\n\n")
print(np.log(arr))
print("\n\n")
