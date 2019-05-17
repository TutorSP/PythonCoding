#WAP in Python to input a temperature in Fahrenheit, convert it to Centigrade and print after rounding off to 3 places 

fahr = float(input("Enter temperature in Fahrenheit: "))	#default input is string, need to convert to float 
celsius = 5/9*fahr - 160/9
celsius = round(celsius, 3)     #rounding off to 3 places of decimal
print("The equivalent temperature in Centigrade is {}".format(celsius))  