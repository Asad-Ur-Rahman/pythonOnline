x = int(input("Enter an integaer greater than 2: "))



for guess in range(2,x):

    if x%guess == 0:
        smallest_divisor = guess
        continue
    else:
        print(guess, end=" ")
