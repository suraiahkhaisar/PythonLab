n=int(input("Enter a value:"))
reverse=0
while n>0:
    r=n%10
    reverse=reverse*10+r
    n//=10
print("Reverseof a number:",reverse)
