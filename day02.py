n = int(input("Input number : "))
is_prime = True
if n >= 2:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False  #count = count + 1
            break
        print(i, end=' ')

else:
    is_prime = False

#if count == 0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")