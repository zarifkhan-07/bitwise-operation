def convert(n):
    r=bin(n)[2:]
    b=r[::-1]
    j=int(b,2)
    return j

n=int(input("Enter the number:"))
print("The number is:",convert(n))