import array as arr

n = int(input("Enter the size of the array: "))
a = arr.array('i', [ ])
 
for i in range(0, n):
		element = int(input("Enter the element : ",))
		a.append(element)	

key = int(input("Enter the element to search: "))


for i in range(0, n):
		if (a[i] == key):
				print(f"The element {a[i]} found at the index {i}.")
				break;
	
else:
		print("The element not found.")



""" print("Array is:", end=" ")
for i in range(0, n):
    print(a[i], end=" ") """
