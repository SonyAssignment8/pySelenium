a=[2,3,6,5,4,7,8]
def check(self):
    if a%2==0:
        print("the even number is:")
        return a
    else:
        print("the odd number")
        return a

print(list(filter(lambda a:a%2==0,a)))


