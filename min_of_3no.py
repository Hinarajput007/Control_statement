A = int(input("Enter first number (A): "))
B = int(input("Enter second number (B): "))
C = int(input("Enter third number (C): "))

if A <= B and A <= C:
    print("Minimum is:", A)
elif B <= A and B <= C:
    print("Minimum is:", B)
else:
    print("Minimum is:", C)