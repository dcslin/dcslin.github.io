import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # blocking
        # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        #     print('%d is prime: %s' % (number, prime))

        # unblocking
        futures = dict()
        for p in PRIMES:
            f:concurrent.futures.Future = executor.submit(is_prime, p)
            futures[p] = f
        done = dict()
        while len(done)<len(futures): # event loop
            print("check loop")
            for p in futures.keys():
                if p in done:
                    continue
                if futures[p].done:
                    done[p] = True
                    print(p, futures[p].result())

if __name__ == '__main__':
    main()