import math
def is_perfect_square(number):
    square_root=math.sqrt(number)
    square_root_floor=int(square_root)
    return square_root_floor*square_root_floor==number


perfect_square=list(filter(is_perfect_square,range(10)))
print(perfect_square)

#  l=[x for x in range(101) if int(x**0.5)==x**0.5]
#  print(l)
#
# print(lambda n:n*n)
