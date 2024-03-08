print("Hello world")
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

num = int(input("Enter your Number:"))
print(f"The binary representation of {num} is {decimal_to_binary(num)}")

n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    print(i, end=' ')
    
    n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    print(i, end=' ')