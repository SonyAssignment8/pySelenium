import random
def lottery():
    for i in range(2):
        yield random.randint(1, 10)

print(lottery())
# print(lottery())
for randomnumber in lottery():
    print("And the next number is... %d!" %(randomnumber))

# This function decides how to generate the random numbers on its own, and executes the yield statements one at a
# time, pausing in between to yield execution back to the main for loop. Write a generator function which returns the
# Fibonacci series. They are calculated using the following formula: The first two numbers of the series is always
# equal to 1, and each consecutive number returned is the sum of the last two numbers. Hint: Can you use only two
# variables in the generator function? Remember that assignments can be done simultaneously. The code