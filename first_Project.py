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

print("Hello World")

def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


n = int(input("Enter the number of Fibonacci terms: "))
print(fibonacci(n))

