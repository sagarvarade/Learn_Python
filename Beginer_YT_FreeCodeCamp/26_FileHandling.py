fileName="d:/fileText.txt"

try:
    file=open(fileName,'r')
    content=file.read()
    print(content)
except FileNotFoundError as er:
    print(er)
finally:
    print("File Read Complete")



with(open(fileName,'r')) as file:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    content=file.read()
    print(content)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


