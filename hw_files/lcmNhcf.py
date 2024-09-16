x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
	
#hcf function
def HCF(x,y) :
	if (x < y):
		s = x
	else:
		s = y
		
	for i in range(2, s+1):
		if (x % i ==0) and (y % i == 0):
			hcf  = i
	return hcf
	
#lcm function
def LCM(x,y):
	lcm = abs(x * y)/ HCF(x,y)
	return int(lcm)


print(f"The HCF is {HCF(x,y)}")
print(f"The LCM is {LCM(x,y)}")

		
