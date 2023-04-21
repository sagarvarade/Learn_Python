numbers=[1,2,3,4,5,6,7,8]

numbers_power_2=[n**2 for n in numbers]
print(list(numbers_power_2))

numbers_power_2=[]

for n in numbers:
    numbers_power_2.append(n**2)

print(numbers_power_2)




