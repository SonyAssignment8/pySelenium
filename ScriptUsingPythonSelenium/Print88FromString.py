def main(s):
    sum=""
    for i in s:
        if i.isdigit():
            if int(i)>0:
                sum=sum+i
    print(sum)

str="sd80daeeedjskl@$$$s8"
main(str)