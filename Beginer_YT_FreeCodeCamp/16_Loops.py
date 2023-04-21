
# Only two type of loops while and for loop

# Loops
condition=True
while condition== True:
    print("The condition is True")
    condition=False

# Loops
count=0
while count<10:
    print("The condition is True",count)
    count=count+1

print("After the loop",count)

# For loops
items=[1,2,3,4,5,6]
for item in items:
    print(item)

for item in range(6):
    print("ss ",item)

items2=["beau","ss","xx","wer"]
for index,item in enumerate(items2):
    print("> ",index,item)

items3=[1,2,34,2,3,4]
for item in items3:
    if item==2:
        continue
    print(item)

items3=[1,2,34,2,3,4]
for item in items3:
    if item==34:
        break
    print(item)
