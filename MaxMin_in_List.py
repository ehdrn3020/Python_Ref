def mm(list):
	mx = max(list)
	mn = min(list)
	return (mx, mn)
list=[]
for i in range(0,3):
	list.append(int(input()))	
print(mm(list))