# Will need to loop through every value in primes_found (nested for loops?)


number_input = int(input("Enter an integer: "))
def searchForPrimes(num):
    found_primes = [2] # It's safe to assume 2 is a prime number. Because it is.
    for integer in range(3, num):
        square_root = integer ** 0.5 # Multiplying an int by 0.5 is equivalent to taking its square root
        for factor in found_primes:
            if integer % factor == 0:
                break
            if factor > square_root:
                found_primes.append(integer)
                break
    return found_primes

print(searchForPrimes(number_input))