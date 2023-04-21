# Exception Handling

"""
try:
    count=count+1
except <ERROR_1>:
    # Handle error 1
except <ERROR_2>:
    # Handle error 2
except:
    #Handle Except part
else:
    #If no error found they this else will be executed
finally:
    #This will always gone be run, no matter exception caught or not
"""


#result=2/0
#print(result)

try:
 result=2/1
 print(result)
except ZeroDivisionError:
    print("Can Not Divide by ZERO") # If exceptions occured
else:
    print("In else Part") # If no exceptions occured
finally:
    print("Here in Finally Block of try catch") # Always
   

try:
    raise Exception('An Error !')
except Exception as error:
    print("Exception ",error) # If exceptions occured
else:
    print("In else Part") # If no exceptions occured
finally:
    print("Finaly")



class DogNotFoundException(Exception):
    print("Inside dog not found Exception.")
    pass

try:
    raise DogNotFoundException('An Error DogNotFoundException')
except DogNotFoundException as error:
    print(error)