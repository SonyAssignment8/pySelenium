def filecreation():
    ofile = open("Story.txt", "w+")
    choice = True
    while True:
        line = input("\n Enter a sentence")
        ofile.write(line)
        choice = input("Enter more?-Y/N")
        if choice == 'N': break
