# Python Practical 18 : To write a python program to print first n Prime Numbers.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    prime_count = 0
    num = 2
    
    while prime_count < n:
        if is_prime(num):
            print(num, end=" ")
            prime_count += 1
        num += 1

n = 12
print(f"The first {n} prime numbers are:")
print_n_primes(n)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
