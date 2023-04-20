from enum import Enum

stringVar="Sagar"
intVar=30
floatVar=23.0
print(f"Values {stringVar} , {intVar}")
# Type of 

print(type(stringVar)," : type of String var")
print(isinstance(stringVar,str)," : Instance of String var")

print(type(intVar)," : type of int var")
print(isinstance(intVar,int)," : Instance of int var")

# Casting
strAge="20"
age=int(strAge)
print(isinstance(age,int)," ",isinstance(age,str))
print(">>>>>>>>>>>>>")

# Arithmatic operators
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Comparison operators
print(a==b,"Equal to")
print(a!=b, "Not equal to")
print(a>=b ,"Greater than")
print(a<=b ,"Less than equal to ")

#Conditinal Operators
con1=True
con2=False
print("Conditional Not, ",not(con1)," ",not(con2))
print("Conditional And, ",con1 and con2)
print("Conditional Or, ",con1 or con2)

# Condoioanls with variables
print(0 or 1)
print(False or 'Hey')
print('hi' or 'hey')
print([] or False)
print(False or [])
print(">>>>>>>")
print(0 and 1)
print(False and 'Hey')
print('hi' and 'hey')
print([] and False)
print(False and [])


# bit wise opertors
# & | ^ ~ << >>

# Ternaory operator
print("Ternory opertor : ",a if a==b else b)

# String in python
String_Var1="SAgar"
String_var2='varade'
String_var3=String_Var1+" "+String_var2
print(String_Var1+" "+String_var2)

String_MultiLiene="""sodf;asijjoyweour;\naewjljlfka
\"
lksdlfkjsl
"""
print(String_MultiLiene)
print(String_var3.lower())
print(String_var3.upper())
print(String_var3.title())
print(String_var3.islower())
print(String_var3.isupper())
print(len(String_var3))
print("gar" in String_var3)

print(">>>>>>>>..")

print(String_var3[1])
print(String_var3[-2])
print(String_var3[1:4])
print(String_var3[4:])
print(String_MultiLiene.splitlines())

print(">>>>>>>>..")

book_1_read=True
book_2_read=False
# Any return true if any value is true
res=any([book_1_read,book_2_read])
print(res)
# all return true if all values are true
res2=all([book_1_read,book_2_read])
print(res2)


# Complex Numbers
num1=2+3j
num2=complex(2,3)
print(num1.real, num1.imag)
print(num2.real, num2.imag)
# Absolute Value
print(round(5.5))
print(abs(5.5))


#Enums in pythonn
class State(Enum):
    INACTIVE=0
    ACTIVE=1
print(">>>>>>>>>>>>> Enums")
print(State.ACTIVE, "  ",State.INACTIVE)
print(State.ACTIVE.value, "  ",State.INACTIVE.value)
print(list(State))
print(len(State))