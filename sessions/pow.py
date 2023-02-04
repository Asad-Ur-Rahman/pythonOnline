x = int(input("Enter an integer: "))
pwr = 1 
while pwr < 6 :
    if x < 0:
        root = x
    else:
        root = 0 
    while root ** pwr <= x:
        if root ** pwr == x:
            print(root, " ** ", pwr, "=", x)
        else:
            if x ** 1 == x:
                print(x, "No such integer pair exists.")
        root += 1
    pwr += 1