def hello():
    print('hello')

def hello2(age,name="My Frield"):
    print(name,age)

hello()
hello2("sagar")
hello2(2,"sagar")
hello2(1) # Conside My Frild as default value

# >>>>>>>>>>>>>>>>>>>>>>..

def  change(value):
    value=2

def  changeDict(dict):
    dict["name"]="Syd"


val=1
change(val)
print(val)  #Value did not changed pass by value

dictvar={"name":"sagar"}
print(dictvar)
changeDict(dictvar)
print(dictvar)


# >>>>>>>>>>...
def hello(name):
    if not name:
        return
    else:
        print("Hello "+name+" .")
        return name,"2 return values"

hello(False)
hello("sagarr")
print(hello("sgar"))
