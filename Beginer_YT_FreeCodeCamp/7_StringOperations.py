
print("String object")
str1="String one"
str2='String two'+' String append here'

# Multi Line String
print("Multi Line Strings")
MultiLineString="""
This is multi Line MultiString \n
Here new line
"""
print(MultiLineString)

# String operations
print("String operations")
strx="sagar VARADE"
print(strx.upper())
print(strx.lower())
print(strx.title())
print(strx.capitalize())
print(strx.isdigit())
print(len(strx))
print("ag" in strx)
print("xx" in strx)
str_spcl="\" The title  \""
print(str_spcl)
# Operators
print(strx[1])
print(strx[0:7])
print(strx[:7])
print(strx[-1:-5])

print(type(strx))

book_1_read=False
book_2_read=False
read_any_book=any([book_1_read,book_2_read])
print(read_any_book)

