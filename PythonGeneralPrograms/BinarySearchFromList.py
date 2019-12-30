def search(args, b):
    l = 0
    h = len(args) - 1
    while l <= h:
        m = (l + h) // 2
        if args[m] == b:
            return m
        elif args[m] < b:
            h = m - 1
            return h
        else:
            l = m + 1
            return l

    return -1


lst = [1, 2, 4, 5, 6]
print("if o/p is -1 then value not available in list", search(lst, 8))
