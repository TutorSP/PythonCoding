#WAP in Python to convert given number of days into years and weeks

days = int(input("Enter number of days: "))

no_of_years = days // 365
no_of_weeks = days // 7

print("Number of years  = {}\nNumber of weeks = {}".format(no_of_years, no_of_weeks))