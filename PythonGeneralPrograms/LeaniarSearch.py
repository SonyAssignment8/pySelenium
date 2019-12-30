def search(args, b):
    for i in args:
        if i == b:
            return i
    return -1
lst = [11, 12, 45, 67]
print("number present in a list is :",search(lst, 12))
