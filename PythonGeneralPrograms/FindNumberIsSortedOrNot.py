def issorted(list):
    previous=list[0]
    for number in list:
        if number<previous:
            return False
        previous=number
    return True

l=['1','3','3']
print(issorted(l))
