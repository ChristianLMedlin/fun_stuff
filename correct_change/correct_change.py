number_of_tens = 0
number_of_fives = 0
number_of_ones = 0
number_of_quarters = 0
number_of_dimes = 0
numbers_of_nickels = 0
number_of_pennies = 0

amount_due = float(input("What is your total bill? $"))

while amount_due >= 10:
    number_of_tens += 1
    amount_due -=10
while amount_due >= 5:
    number_of_fives += 1
    amount_due -= 5
while amount_due >= 1:
    number_of_ones += 1
    amount_due -= 1
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

message = f"You were given {number_of_tens} tens, {number_of_fives} fives, {number_of_ones}, {number_of_quarters} quarters," \
    f" {number_of_dimes} dimes, {numbers_of_nickels} nickels, and {number_of_pennies} pennies."

print(message)