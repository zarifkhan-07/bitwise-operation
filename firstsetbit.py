def nofb(n):
    while(n):
        if (n&1==1):
            print("There is a number")
        else:
            print("Ther is no number")
        n>>=1

n=int(input("Enter the num:"))
nofb(n)