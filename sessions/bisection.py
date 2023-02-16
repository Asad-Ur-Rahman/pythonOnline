x = int(input("Enter any integer to find square root: "))

epsilon = 0.01
num_guesses = 0
low = 0
high = max(1,x)

guess = (high + low)/2.0

while abs(guess**2 - x) >= epsilon:
   
   print('low =', low, 'high = ', high, 'guess = ', guess)

   if guess**2 < x:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the square root of', x)
