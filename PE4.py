#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



#calc product
#check if palindrome
#reduce b by 1 until 99
#reduce a by 1

def calc_product(a,b):
    print(a*b)
    return(a*b)


def palindrome(product):
    #convert int to string
    pro_str = str(product)
    rev = pro_str[::-1]
    #check if string forwards = string bakwards    
    if pro_str == rev:
        return True
    else:
        return False

largest = 0
for first in range(999,99,-1):
    for second in range(999,99,-1):
        prod = calc_product(first,second)
        if palindrome(prod) == True and prod > largest:
            largest = prod
        
    
    
print(largest)
#906609

#not mine
print(max(x * y for x in range(100, 1000) for y in range(100, 1000)
          if str(x * y) == str(x * y)[::-1]))

#Second Try
largest = []
for first in range(999,99,-1):
    for second in range(999,99,-1):
        prod = first*second
        if str(prod) ==str(prod)[::-1]:
            largest.append(prod)
        
print(max(largest))