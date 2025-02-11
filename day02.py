n = int(input("Input number : "))
is_prime = True
if n >= 2:
    i = 2
    while i < n:
        if n % i == 0:
            is_prime = False  #count = count + 1
            break
        i += 1

else:
    is_prime = False

#if count == 0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")