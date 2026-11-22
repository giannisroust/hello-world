print('Hello, world!')
print(2+2)

spam = 40
print(spam)


print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')

name = input("What is your name? ")
if name == "Alice":
    print("Hi, Alice.")
else:
    print("Hello, stranger.")