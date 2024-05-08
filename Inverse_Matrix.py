# Importing Library 
import numpy as np 

# inverse of 1X1 matrix 
arr = np.array([[7]]) 
inverse_array = np.linalg.inv(arr) 
print("Inverse Matrix 1x1 is ") 
print(inverse_array)

# inverse of 2X2 matrix 
arr = np.array([[3, 7], [8, 2]]) 
inverse_array = np.linalg.inv(arr) 
print("Inverse Matrix 2x2 is ") 
print(inverse_array) 
print() 
  
# inverse of 3X3 matrix 
arr = np.array([[3, 9, 7],  
                [4, 8, 2],  
                [6, 5, 9]]) 
  
inverse_array = np.linalg.inv(arr) 
print("Inverse Matrix 3x3 is ") 
print(inverse_array) 
print() 
  
# inverse of 4X4 matrix 
arr = np.array([[10, 20, 30, 40],  
                [5, 12, 18, 6], 
                [7, 17, 5, 9],  
                [1, 2, 3, 4]]) 
  
inverse_array = np.linalg.inv(arr) 
print("Inverse Matrix 4x4 is ") 
print(inverse_array) 
print() 
  
