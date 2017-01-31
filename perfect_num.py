# input number and get a perfect number from 1 to number
def perfect(num) :
	sum = 0
	for i in range(1,num+1):
		for j in range(1,i):
			if i%j==0 :
				sum+=j
		if sum == i : 
			print sum,     #print("%d "%sum, end= ' ') python 3.0
		sum = 0			

num = int(input("input the number: "))
perfect(num)		 
