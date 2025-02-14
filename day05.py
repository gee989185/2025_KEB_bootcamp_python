# def factorial_repetition(n) -> int:
#     '''
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: 팩토리얼 값, int
#     '''
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#     '''
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, int
#     '''
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursion(n-1)
#
# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())
#1 2 3 4 5 6 7 8  9
#0 1 1 2 3 5 8 13 21
def fibonacci_recursion(n):
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

a, b, c, d  = map(int,input().split())
for i in range(a):
    print(f"{i+1}번째 항: {fibonacci_recursion(i)}")



def fibonacci_loop(n):
    n_list = [0, 1]
    for i in range(n + 1):
        n_list.append(n_list[i] + n_list[i + 1])
    return n_list[n]

for j in range(b):
    print(f"{j+1}번째 항: {fibonacci_loop(j)}")

def recrusion(n):
    if n == 0:
        return 0
    else:
        return recrusion(n-1)

for k in range(c, -1, -1):
    if k == 0:
        print("펑")
    else:
        print(f" recrusion {k}")

def loop(n):
    for k in range(n, -1, -1):
        if k == 0:
            print("펑")
        else:
            print(f" loop {k}")

loop(d)