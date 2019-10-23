# Find the Highest Common Factor (HCF) of a and b.
# define a function
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf
a = int(input("a: "))
b = int(input("b: "))

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", b,"and", a,"is", computeHCF(a, b))
a = int(input("a: "))
b = int(input("b: "))

