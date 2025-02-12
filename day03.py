import math



def my_pow(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """

    if e < 0:
        b = 1 / b
        e = e * -1
    result = 1

    # 정수부분 실수부분 나누기
    i = int(e)
    f = e - 1


    for _ in range(i):  # for_ in range(e):
        result = result * b

    if f > 0:
        result = result * math.exp(f * math.log(b))

    return result

print(my_pow(10, -2))
print(my_pow(2,9)) # 512
print(my_pow(16, 0.5))  #4
print(my_pow(4, 2)) #16
# print(math.exp(1))
# print(math.e)
print(math.log(3))