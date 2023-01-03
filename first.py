primes = []
n = 2

while len(primes) < 200:
    primo = True
    if len(primes) == 0:
        print(n)
        primes.append(n)
        n += 1
        continue
    for i in primes:
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n)
        primes.append(n)
    n += 1