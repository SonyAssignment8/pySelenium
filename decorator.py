import time
def cube(n):
    start = time.time()
    for i in range(n):
        res =i**3
    end=time.time()
    print("Total time taken is : ", end-start)
cube(1000000)