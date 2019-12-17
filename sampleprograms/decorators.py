import time
# def add(a,b):
#     start=time.time()
#     time.sleep(3)
#     print(a+b)
#     end=time.time()
#     print("total time taken is:",start-end)
# def sub(a,b):
#     start = time.time()
#     time.sleep(3)
#     print(a -b)
#     end = time.time()
#     print("total time taken is:", start - end)
# add(5,10)
# sub(20,3)

def timer(func):
    def inner(a,b):
        start=time.time()
        func(a,b)
        end=time.time()
        print("total time taken is:", start - end)
    return inner
@timer
def add(a,b):
    print(a+b)
add(2,3)