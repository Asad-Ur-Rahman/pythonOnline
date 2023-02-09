epsilon = 0.01
step = epsilon ** 2
num_guess = 0
ans = 0.0

x = int(input("Enter any integer to find square root: "))

while abs(ans **2 - x) >= epsilon and ans <= x:
    ans += step
    num_guess += 1

print('number of guesses =', num_guess)

if abs(ans**2 - x) >= epsilon:
    print('failed on suqare root of', x)
else:
    print(ans, 'is close to suqare root of', x)