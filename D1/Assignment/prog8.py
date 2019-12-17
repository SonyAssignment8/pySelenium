#WAP to swap 2 variables
#1.with & without temp variables
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)


# Python program to swap two variables without using temp variables
     

num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers without using temporary variable
num1, num2 = num2, num1

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)