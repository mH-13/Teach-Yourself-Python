import numpy as np 

arra = np.array([1,2,3,4])
print(arra)
print(type(arra))

x = np.array([1,2,3,4])
y = np.append(x, [20,30])
z = np.delete(y, [20,30])
sorted_z = np.sort(z)


2d_arra = np.array([1,2,3], [4,5,6]) 
# len(2d_arra) = 2
#2d_arra.shape = (2,3) // Tuple of array dimensions
#2d_arra.ndim = number of array dimension
#print(2d_arra[1,2]) // 3rd element of 2nd dim


# from 2nd element, index 1 to  4:
#print(arr[1, 1:4])
#from both elements, index 1 to  4:
#print(arr[0:2, 1:4])
