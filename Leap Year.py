for i in range(int(input("How many times you want to check"))):
    year = int(input("Enter the Year"))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    
    else:
        print("No")
