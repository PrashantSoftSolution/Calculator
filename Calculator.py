def add(x, y):    
   return x + y   
def subtract(x, y):   
   return x - y   
def multiply(x, y):   
   return x * y   
def divide(x, y):   
   return x / y   
print ("Please select the operation whatever you want to perform ")    
print ("1. Add")    
print ("2. Subtract")    
print ("3. Multiply")    
print ("4. Divide")    
    
choice = int(input("Please enter your choice (1/ 2/ 3/ 4):- "))    
    
first_num = int(input ("Please enter the first number:- "))    
second_num = int(input ("Please enter the second number:- "))    
    
if choice == '1':    
   print (first_num, " + ", second_num, " = ", add(first_num, second_num))    
    
elif choice == '2':    
   print (first_num, " - ", second_num, " = ", subtract(first_num, second_num))    
    
elif choice == '3':    
   print (first_num, " * ", second_num, " = ", multiply(first_num, second_num))    
elif choice == '4':    
   print (first_num, " / ", second_num, " = ", divide(first_num, second_num))    
else:    
   print ("invalid choice")    
