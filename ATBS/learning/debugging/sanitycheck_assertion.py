#The below has no issues, so the program continues running. 
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.


# If the ages list were not sorted, the assert statement would raise an AssertionError and stop the program.


##Below we will see an example of an assert statement that fails and raises an AssertionError.

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# print(ages)
# assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.

