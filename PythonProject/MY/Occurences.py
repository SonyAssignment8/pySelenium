# # One way
# s = input("Enter a string to count occurrences:")
# dict = {}
# count = 1
# s = s.replace(' ', '')
# for char in s:
#     dict[char] = dict.get(char, 0) + 1
# print("Character dict for '{}' is :\n {}".format(s, str(dict)))

# Second way
input_string = "Data Science"
input_string = input_string.replace(" ","")
frequencies = {}

for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Show Output
print("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))

# adding numbers in between the string
s1 = input("Enter a alphanumeric string:")

addition = 0
for chr in s1:
    if chr.isdigit():
        z = int(chr)
        addition = addition + z
print(addition)





