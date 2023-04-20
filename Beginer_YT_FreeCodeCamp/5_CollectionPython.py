dogs=["rogs",23.2,"max",12,"sds","sss","zzz"]
print("rogs" in dogs)
print("rogsss" in dogs)
print(dogs[0])
print(list(dogs))
dogs[2]="jjjjjjjj"
print(list(dogs))
print(len(dogs))
print(dogs[-2])
print(dogs[2:5])
print(dogs[0:])
dogs.append("sssssss")
dogs.extend(["xx",5])
print(dogs)
print(dogs.pop())
dogs.insert(1,"sxx")
print(dogs)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
IntItems=[1,4,5,22,43,53,21]
StringItems=["abc","msj","wsg","pol"]
IntItems.sort()
print(IntItems)
StringItems.sort(key=str.lower)
print(StringItems)

itemsCopy=StringItems[:]
print(itemsCopy)


#Tuples, unmodifiable collections 
name=("Roger","Syd")
print(name[0])
print(name.index("Roger"))
print(len(name))
print("Roger" in name)
print(sorted(name))
newTuple=name+("tina","Mina")


# Dictionary , Map like DS 
print(">>>>> Tuples")
dog={"name":"Roger","age":8,"color":"green"}

print(dog["age"])
print(dog.get("age"),"  ",dog.get("coler","browm"))
print(dog)
# print(dog.popitem())
print("color" in dog)
print(dog.keys())
print(dog.values())
print(len(dog))

# Sets Immutable data  sets 
print(">>>>>>>>>>>>>>>>Sets")
Sets_name={"Roger","sgar","sdd"}
set2={"maz"}
Sets_name.add("varade")
intersect=Sets_name & set2
union=Sets_name | set2
minus=Sets_name - set2
print(list(Sets_name))
print(intersect)
print(union)

