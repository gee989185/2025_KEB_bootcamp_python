# SOLID
#Open Clossed Princinple: 개방 폐쇄 원칙 (확장에는 열려 있고 수정에는 닫혀있는 원칙)

import time

# !(factorial)
def factorial_repetition(n) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

number = int(input())
start_time = time.time()
print(f"{number}! = {factorial_repetition(number)}")
end_time =  time.time()
print(end_time - start_time)