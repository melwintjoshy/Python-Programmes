n = int(input("Enter the number of elements: "))
x = 0
y = 1
print("Fibonacci series : ")
if n == 1:
	print(x)
else:
	print(x, end = " ")
	for i in range(0,n - 1):
		sum = x + y
		x = y
		y = sum
		print(sum, end = " ")
