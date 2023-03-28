# Sum square difference
# Show HTML problem content 
# Problem 6
# The sum of the squares of the first ten natural numbers is, 385

# The square of the sum of the first ten natural numbers is,3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# .3025-385=2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

top = 100
sum_squares = []
square_sums = []
for i in range(1,top +1):
    sum_squares.append(i**2)
    square_sums.append(i)

sm_sq = sum(sum_squares)
sq_sum = sum(square_sums)**2
Diff = abs(sm_sq - sq_sum)
print(f"For the numbers 1 to {top} the sum of squares is {sm_sq} and the square of sums is {sq_sum}. The difference is {Diff})")
