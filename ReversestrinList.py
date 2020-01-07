#Program to reverse list of string
def Reverse(l):
    new_lst = l[::-1]
    return new_lst


l=['apple','boy','girl','elephant','fox']
print(Reverse(l))