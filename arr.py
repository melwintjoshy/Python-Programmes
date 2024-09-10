import array as arr

n = int(input("Enter the size of the array: "))
a = arr.array('i', [ ])
 
print("Enter the elements: ")
for i in range(0, n):
		element = int(input())
		a.append(element)	

key = int(input("Enter the element to search: "))
found = 0

for i in range(0, n):
		if (a[i] == key):
				found = 1;
	
if found == 1:
		print(f"The element {a[i]} found at the index {i}.")
else:
		print("The element not found.")



""" print("Array is:", end=" ")
for i in range(0, n):
    print(a[i], end=" ") """
