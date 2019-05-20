# WAP in Python to calculate the sum of all prime numbers between 1 and 100
def isPrime(n):
	flag = True
	for i in range(2, n//2+1):
		if n%i == 0:
			flag = False
			break
	return flag
sum = 0
for i in range(2, 101):
	if isPrime(i):
		sum += i
print("The sum of Prime numbers from 1 to 100 is {}".format(sum))