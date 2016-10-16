from __future__ import division
import numpy as np

# Create array of values from 0 to 10
arr = np.arange(0,11)
print arr
print arr[8]
print arr[-1]
print arr[0:5]

# Set the first 5 values to 100
arr[0:5] = 100
print arr

# Create a slice of an array
arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print slice_of_arr
slice_of_arr[:] = 100
print slice_of_arr
print arr

# Indexing on two-dimensional array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Return a row
print arr_2d[1]

# Return a cell
print arr_2d[1][1]

# slice a 2d array
print arr_2d[:2,1:]


