def get_input():
    try:
        a = int(input("Enter the value:"))
        b = int(input("Enter the value:"))
        return a,b
    except ValueError as e:
        print(e)
        return get_input()
    finally:
        print("finally of get input()")

def div(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally of div()")
def main():
    try:
        a,b = get_input()
        c = div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except Exception as e
        print(e)
        main()
    except:
        print("Exception is arrised")
    finally:
        print("process completed")
if __name__ == "__main__":
    main()