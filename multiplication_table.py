# Print the multiplication table for numbers from 1 up to 10.

product = 0
multiplier = 1

for row in range(1, 11):
    for prod in range(1, 11):
        product = row * multiplier
        print(f'{row} x {multiplier} = {product}')
        multiplier += 1
    multiplier = 1

