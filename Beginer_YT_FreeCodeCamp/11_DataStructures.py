dogs=['Roger','Syd',1,True]
print('Syd' in dogs)
print(1 in dogs)
print(False in dogs)
print(True in dogs)

print(dogs[1])
print(dogs[0:])
dogs.append("Step 1")
dogs.append(False)
dogs.extend(["New Item"])
dogs.extend("aa")
print(len(dogs))
print(dogs[0:])
dogs.remove("a")
print(dogs[0:])
dogs.pop()
print(dogs[0:])

#### >>>>>>>...

items=["aaa","bbb","ccc","ddd","eee"]

items.insert(2,"test")
items[1:1]=["csc","dese"]
print(items[0:])
items.sort(key=str.lower)
items.sort()
print(items[0:])

itemsCopy=items[:]
print(itemsCopy)
print(sorted(items,key=str.lower))

#Tuples, As List
tpl=("Roger","Syd","AAA")
print(tpl[0])
print(tpl[:])
print(len(tpl))
print(sorted(tpl))



## Dictionaries , As map of Key Value pairs
mMaps={"name":"Roger","sur":"Mike","age":334}
print(len(mMaps))
print(mMaps.get("age"))
print(mMaps)
#print(mMaps.pop("name"))
#print(mMaps.popitem())
print("name" in mMaps)
print(mMaps.keys())

print(list(mMaps.values()))
print(list(mMaps.items()))
mMaps["loc"]="ade"
print(list(mMaps.items()))
del mMaps["loc"]
mCopy=mMaps.copy()
print(list(mMaps.items()))


# Sets 
nameSet={"roger","roger","ssd","xfd"}
print(nameSet)
settwo={"xree","sert","ssd"}
intersect=nameSet & settwo
print(intersect)

union=nameSet | settwo
print(union)

mod=nameSet - settwo
#mod=nameSet < settwo
#mod=nameSet > settwo
print(mod)
print(list(mod))

