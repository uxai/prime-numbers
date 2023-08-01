import math

def check_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return print(r, end="\t")

prime_limit = int(input("To what range would you like to check the primes?"))
prime_limit = math.floor(prime_limit / 90)

keys = (1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89)

for n in range(0, prime_limit):
    for i in range(0, len(keys)):
        r = 90 * n + keys[i]
        if r == 1:
            print("2\t3\t5", end="\t")
        else:
            check_prime(r)
