with open('../../Mypractise/atul.txt') as infile:
    lines = 0
    words = 0
    characters = 0
    for line in infile:
        wordslist = line.split()
        lines = lines+1
        words = words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
print("Number of available lines:", lines)
print("Number of available Words:", words)
print("Number of available characters:", characters)