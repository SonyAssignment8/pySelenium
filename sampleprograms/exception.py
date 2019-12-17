def get_inpuy():
    try:
        a=int(input("enter the value:"))
        b=int(input("enter the value:"))
        return a,b
    except ValueError as v:
        print(v)
        return get_inpuy
    finally:
        print("finally of get_input()")

def div(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally is running")
def main():
    try:
        a,b=get_inpuy()
        c=div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e:
        print(e)
        main()
    except:
        print("exception is araised")
        main()
    finally:
        print("process completed")

if __name__=="__main__":
    main()