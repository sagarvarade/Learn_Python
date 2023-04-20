age=8

def test():
    age=10
    print(age)
    
    def MyPrintFunc(varx):
        print("Inside Func :",varx)

    MyPrintFunc(age)


print(age)
test()

def talk(phrase):
    def say(word):
        print(word)

    words=phrase.split(" ")
    for word in words:
        say(word)

talk("This is my pharase word")

# >>>>>>>>>>>

def count():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(count)
    return increment

count()
increment=count()
print(increment())
print(increment())
print(increment())
