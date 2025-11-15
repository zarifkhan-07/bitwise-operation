def is_power_of_8(n):
    if n <= 0:
        return False
    
    while n % 8 == 0:
        n = n // 8
    
    return n == 1

# Input
num = int(input("Enter a number: "))

# Output
if is_power_of_8(num):
    print(num, "is a power of 8")
else:
    print(num, "is NOT a power of 8")
