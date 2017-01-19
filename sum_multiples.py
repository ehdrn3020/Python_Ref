n=int(input("input the number "))
k=0
Sum=0
if n<1 and n>100:
	print("input only 1 to 100 number")
elif n>=1 and n<=100:
	while k<100:
		k=k+n
		Sum=Sum+k
		print(k)
	print(Sum)
else: 
	print("wrong number")
			
	
	
	


