def sample():
    try:
        a=1,b=2
        return 10
    except:
        return 20
    finally:
        return 30

print(sample())
