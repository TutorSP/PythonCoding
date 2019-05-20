# WAP in Python to check whether a number is negative, zero or positive

number = int(input("Enter a number: "))
if number < 0:
   print("{} is a negative number".format(number))
elif number == 0:
   print("{} is zero".format(number))
else:
   print("{} is a positive number".format(number))   
