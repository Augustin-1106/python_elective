import math

num = float(input('Enter a positive number:'))
guess = 1.0
tolerance=0.00001

while True:
        new_guess = 0.5 * (guess + num / guess)
        if abs(new_guess - guess) < tolerance:
                print('Programs Estimate:',new_guess)
                print('Pythons Estimate:',math.sqrt(num))
                break
        guess = new_guess