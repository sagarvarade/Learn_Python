from functools import reduce

# Maps
doubleLambda=lambda a:a*3

numbers=[1,2,3,4,5,6,7,8,9]
def double(a):
    return a*2

result=map(double,numbers)

print(list(result))

result2=map(doubleLambda,numbers)
print(list(result2))


result3=map(lambda a:a*4, numbers)
print(list(result3))

# Filter
def isEven(n):
    return n%2==0

isOddLambda= lambda a:a%2!=0

res_1=filter(isEven,numbers)
print(list(res_1))

res_2=filter(isOddLambda,numbers)
print(list(res_2))

# Reduce , get val greater than 5

expenses=[
    ('Dinner',80),
    ('car repair',120)
]

sum=0

for expense in expenses:
    sum+=expense[1]

print("Reduce ",sum)

sum2=reduce(lambda a,b:a[1]+b[1],expenses)
print("Lambda reduce vlaue ",sum2)