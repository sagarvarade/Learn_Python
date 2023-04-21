
def logTime(func):
    def wrapper():
        print("Before")
        val=func()
        print("After")
        return val
    return wrapper

@logTime
def hello():
    print("Hello Word")


print(hello())
