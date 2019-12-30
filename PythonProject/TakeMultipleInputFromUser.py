import sys
print("Enter multi line input:") # When input is done press (ctrl+D)
msg = sys.stdin.readlines()
print(msg)
for item in msg:
    # manipulate user input data
    print(item)
