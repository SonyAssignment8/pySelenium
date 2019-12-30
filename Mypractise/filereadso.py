count = {}
for w in open('atul.txt').read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print ("%s was found %d times" % (word, times))