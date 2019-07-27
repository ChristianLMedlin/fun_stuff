amount_due = float(input("What is your total bill? $"))

number_of_quarters, number_of_dimes, numbers_of_nickels, number_of_pennies = 0, 0, 0, 0


while amount_due >= .25:
    number_of_quarters += 1
    amount_due -= .25
while amount_due >= .10:
    number_of_dimes += 1
    amount_due -= .10
while amount_due >= .05:
    numbers_of_nickels += 1
    amount_due -= .05
while amount_due >= .01:
    number_of_pennies += 1
    amount_due -= .01


print(f'You were given {number_of_quarters} quarters, {number_of_dimes} dimes, {numbers_of_nickels} nickels, and {number_of_pennies} pennies!')