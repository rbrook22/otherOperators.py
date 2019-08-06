#File using other built in functions/operators
print('I will be printing the numbers from range 1-11')
for num in range(11):
    print(num)

#Printing using range and start position
print("I will be printing the numbers from range 1-11 starting at 4")
for num in range(4,11):
    print(num)

#Printing using range, start, and step position
print("I'll print the numbers in range to 11, starting at 2, with a step size of 2")
for num in range(2,11,2):
    print(num)

#Using the min built in function

print('This is the minimum age of someone in my family:')
myList = [30, 33, 60, 62]
print(min(myList))

#Using the max built in function

print('This is the maximum age of someone in my family:')
print(max(myList))

