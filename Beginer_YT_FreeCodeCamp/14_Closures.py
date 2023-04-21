
# Closures basically means returning functions and using it

def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        return count,"He"
    
    return increment

incr=counter()
print(incr()) #(1, 'He')
print(incr()) #(2, 'He')
print(incr()) #(3, 'He')