def check(n1,n2):
    if (n1^n2)!=0:
        print("The numbers are not equal.")
    else:
        print("The numbers are equal.")

n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))

check(n1,n2)