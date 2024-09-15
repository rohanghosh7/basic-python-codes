n=int(input("Enter a number="))
sum=0
while(n>0):
    d=int(n%10)
    sum+=d
    n//=10
print("Sum=",sum)
