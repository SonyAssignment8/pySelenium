# 4. Program to read a file and reverse each line
# Writing data into a file
f1 = open("fData.txt", 'w')
f1.write("In Fibonacci series, next number is the sum of previous two numbers.\nThe first two numbers of Fibonacci "
         "series are 0 and 1.")
f1.close()

# Reading data from a file
'''1. User must enter a file name.
2. The file is opened using the open() function and all lines are stored in a list.
3. reversed() function produces a reverse iterator.
4. All the lines are then printed in reverse order using a for loop and 
rstrip() function strips all the blank spaces from the end of the line.'''

filename = input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
f1.close()
