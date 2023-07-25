n=int(input("Enter the value for N: "))
k=int(input("Enter the value for K: "))
a=pow(2,k)
b=n/a
c=n-b 
print("Eliminated: "+str(c))
print("Remaining: "+str(b))