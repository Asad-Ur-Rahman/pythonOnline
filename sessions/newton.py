x = int(input("Enter any integer to find square root: "))

epsilon = 0.01
guess = x/2

while abs(guess**2 - x) >= epsilon:
    guess = guess -(((guess**2) - x)/(2*guess))

