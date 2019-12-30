# num = int(input("Enter a number t generate next palindrome:"))
# rev, rem = 0


# temp = num
# for i in range(0, 10):
#     num += 1
#     while num > 0:
#         rem = num % 10
#         sum = (sum * 10) + rem
#         num = num // 10
#     if temp == sum:
#         print("palindrome number ")
#     else:
#         print("not palindrome")
def next_Palindrome(num):
    for x in range(num, num + 10):
        if str(x) == str(x)[::-1]:
            return x


def previous_Palindrome(num):
    for x in range(num - 1, 0, -1):
        if str(x) == str(x)[::-1]:
            return x


print("Next palindrome is:", next_Palindrome(140))
print("Previous palindrome is :", previous_Palindrome(120))
