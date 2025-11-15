def power(x, y):
    result=1
    for i in range(y):
        result=result*x
    return result

x=int(input("Enter the x for x^y:"))
y=int(input("Enter the y for x^y:"))
print("Total:",power(x,y))