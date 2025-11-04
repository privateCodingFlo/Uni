def isPrime(num):
    if num <= 1:
        return False

    # num / 2 because at half of numb there can none divider exists
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    return primes


start = 0
end = int(input("Enter the end of the range: "))

print(primes_in_range(start, end))
