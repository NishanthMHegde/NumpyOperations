import numpy as np 

#Convert a list to a 1D array
my_list = [1, 2, 3]
arr = np.array(my_list)
print("1D numpy array")
print(arr)
print("\n\n")
#convert a list of lists to a numpy matrix 
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(my_list)
print("2D numpy array or a numpy matrix")
print(arr)
print("\n\n")
#1D zeros array
arr = np.zeros(5)
print("1D zeros array")
print(arr)
print("\n\n")
#numpy zeros matrix
arr = np.zeros((5, 5))
print("2D zeros matrix")
print(arr)
print("\n\n")
#1D ones array
arr = np.ones(5)
print("1D ones array")
print(arr)
print("\n\n")
#numpy ones matrix
arr = np.ones((5, 5))
print("2D zeros matrix")
print(arr)
print("\n\n")
#numpy range array 1D
arr = np.arange(0, 10)
print("numpy range array 1D")
print(arr)
print("\n\n")
#numpy arange array 1D with steps
arr = np.arange(0, 10 ,2)
print("numpy arange array 1D with step size of 2")
print(arr)
print("\n\n")
#numpy linspace (numbers within a range which are equally seperated)
arr = np.linspace(0, 5, 100)
print("numpy linspace (numbers within a range which are equally seperated)")
print(arr)
print("\n\n")
#random uniformly distributed numpy array
arr = np.random.rand(10)
print("random uniformly distributed numpy array")
print(arr)
print("\n\n")
#random normally distributed numpy array
arr = np.random.randn(10)
print("random normally distributed numpy array")
print(arr)
print("\n\n")
#random integers within a given range as numpy array
arr = np.random.randint(0, 100, 15)
print("random integers within a given range as numpy array")
print(arr)
print("\n\n")

#starting shape operations
print("starting shape operations")
print("Shape of previously constructed numpy array is %s"%(arr.shape))

#resizing the 1D array to a 2D array
print("resizing the 1D array to a 2D array")
arr = arr.reshape(3, 5)
print("Resized array is")
print(arr)
print("Shape of resized numpy array is %s"%(str(arr.shape)))
print("\n\n")