# f = open("atul.txt","w")
# choice = True
# while True:
#    line = input("\n Enter first sentence")
#    f.writelines(line)
#    choice = input("Enter more ?-Y/N :")
#    if choice == "n" : break
# f.close()


def reversec():
    h = open("Story.txt", "r")
    k = h.readlines()
    t = reversed(k)
    for i in t:
        print(i.rstrip())



