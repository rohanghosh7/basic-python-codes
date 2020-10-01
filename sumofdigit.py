n=int(input("Enter a number="))
copy=n
summ=0
while n>0:
    d=n%10;
    summ+=d
    n//=10
print("sum = ", summ)

