# Factorial digit sum

# Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

start = 100
fact = start

for i in range(1,fact):
    fact *= i

sm = 0
for c in str(fact):
    sm += int(c)

print(f"The sum of the digits in the number {start}! is {sm}")
    