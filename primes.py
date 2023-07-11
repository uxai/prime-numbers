import time
start_time = time.time()

def check_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return print(r, end="\t")

keys = (1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
        47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89)

for n in range(0, 100):
    for i in range(0, 24):
        r = 90 * n + keys[i]
        if r == 1:
                print("2\t3\t5", end="\t")
        else:
            check_prime(r)

print("\n--- %s seconds ---" % (time.time() - start_time))
