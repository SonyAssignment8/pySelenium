#max of number
max_num=max([i for i in [23,21,10,5,50]])
print(max_num)

#max of string
s=['hi','hello','python']
max_word=max([s1 for s1 in s])
print(max_word,len(max_word))

#another way
lis = ['hi', 'hello', 'hey','ohman', 'yoloo', 'hello']
def length_str(lists):
    a = 0
    answer = ""


    for item in lists:
        x = len(item)
        if x > a:
            a = x
            answer = item
        elif x == a:
            if item not in answer:
                answer = answer + " " + item
    return answer
print(length_str(lis))