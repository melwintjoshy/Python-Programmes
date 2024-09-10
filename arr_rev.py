import array as arr

n = int(input("Enter the size of the array: "))
a = arr.array('i', [ ])
 
for i in range(0, n):
	element = int(input("Enter the element : ",))
	a.append(element)	

print("Array before reversing is:", end=" ")
for i in range(0, n):
    print(a[i], end=" ") 

print()

start = 0
end = n - 1

while start<end:
	
	temp = a[start]
	a[start] = a[end]
	a[end] = temp
	
	start+=1
	end-=1

print("Array after reversing is:", end=" ")
for i in range(0, n):
    print(a[i], end=" ") 
		
		
		
