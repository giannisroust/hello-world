ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.

#The above has no issues, so the program continues running. 
# If the ages list were not sorted, the assert statement would raise an AssertionError and stop the program.

#Below we will see an example of an assert statement that fails and raises an AssertionError.

'''
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
ages
[73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.
'''

