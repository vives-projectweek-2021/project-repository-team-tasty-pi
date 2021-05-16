import sys
import time
import math

#Don't need to iterarite even numbers after 2
#Don't need to go higier than sqare root of n
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primeToFind = 60000
primeFounded = 0
found = False

num = 1

startTime = time.perf_counter()
print(f"\nStarting looking for {primeToFind} primes\n")

num = 1
while found == False:
    num += 1
    
    if(is_prime(num)):
        print(f"{num}, ", end="")
        primeFounded +=1

        if primeToFind == primeFounded:
            found = True
    
    


endTime = time.perf_counter()
calculateTime = endTime - startTime

print(f"\nFounded primes: {primeFounded}\nTime: {format(calculateTime, '.5f')}s")



