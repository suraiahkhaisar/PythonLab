n=int(input("Enter a value:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("Perfect Number")
else:
    prin("Not a Perfect Number")
