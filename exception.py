def getinput():
    try:
        a=int(input("Enter a value"))
        b=int(input("Enter a value"))
        return a,b
    except ValueError as e:
        print(e)
        return getinput()
    finally:
        print("finally of getinput()")

def div(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally of div()")

def main():
    try:
        a,b=getinput()
        c=div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e:
        print(e)
        main()
    except:
        print("Exception is araised")
    finally:
        print("finally process completed")

if __name__=="__main__":
    main()