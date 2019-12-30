# Hint: Can you use only two variables in the generator function? Remember that assignments can be done
# simultaneously. The code :
a = 1
b = 2
a, b = b, a
print(a,b)
# will simultaneously switch the values of a and b.
# fill in this function
def fib():
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
