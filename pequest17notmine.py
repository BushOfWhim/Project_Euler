def count_letters(n):
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
               16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
               40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    count = 0
    for i in range(n, n+1):
        if i in numbers:
            count += len(numbers[i])
        else:
            count += len(numbers[i//10*10]) + len(numbers[i%10])
    return count

print(count_letters(100))