def is_prime(num) -> bool:
    """
     A function that returns True if it is a prime number and False if it is not a prime number
    :param num:
    :return:
    """
    if n >= 2:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    else:
        return False
    return True
# main
help(is_prime)
n = int(input("Input number : "))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")