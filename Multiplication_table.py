#multiplication table

def mul_table(n) :
  for i in range(1,9) : 
    print("%d * %d = %d" % (n,i,n*i))
    
n = input("Give me the Number ")
mul_talbe(n)
