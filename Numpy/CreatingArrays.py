import numpy as np

# Create an array by converting a list
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print my_array1

my_list2 = [11,22,33,44]
my_lists = [my_list1,my_list2]
my_array2 = np.array(my_lists)
print my_array2
print 'Shape of array: ' + str(my_array2.shape)
print 'Type of array: ' + str(my_array2.dtype)

zero_array = np.zeros(5)
print zero_array
print 'Shape of array: ' + str(zero_array.shape)
print 'Type of array: ' + str(zero_array.dtype)

ones_array = np.ones([5,25])
print ones_array
print 'Shape of array: ' + str(ones_array.shape)
print 'Type of array: ' + str(ones_array.dtype)

identity_array = np.eye(5)
print identity_array
print 'Shape of array: ' + str(identity_array.shape)
print 'Type of array: ' + str(identity_array.dtype)

print np.arange(5)

print np.arange(5,50,2)