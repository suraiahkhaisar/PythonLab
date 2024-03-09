n=int(input("Enter a value:"))
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum+r*r*r
    n//=10
if(sum==temp):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
