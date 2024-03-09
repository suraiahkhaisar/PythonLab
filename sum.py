n=int(input("Enter a value:"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n//=10
print("Sum of individual digits is:",sum)
