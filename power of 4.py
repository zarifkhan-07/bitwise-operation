n=int(input("Enter the number:"))

if n>0 and (n & (n-1))==0 and (n%3==1):
    print("\n The number is a power of 4")
else:
    print("\n The number is not a power of 4")