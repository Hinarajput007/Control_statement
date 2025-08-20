A = int(input())
original = A
reverse = 0
while A > 0:
    reverse = reverse * 10 + A % 10
    A //= 10
print("Yes" if original == reverse else "No")