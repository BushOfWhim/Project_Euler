# Self powers
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

tot = 0
top = 1000
for i in range(1,top+1):
    num = str(i**i)
    tot += int(num[-11:])

print(str(tot)[-10:])

#9110846700

