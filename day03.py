# Assignment
# 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정
# while문 안 쪽의 하드 코딩된 코드를 함수화하시오
# while문 안 쪽의 조건문을 줄이세요 hint. int로 하기
import random


# d_s_p = {"위스키": [ '초콜릿', 50_000]}
# print(d_s_p["위스키"][1])      # output = 초콜릿

# 술(sul), 안주(anzu) 설정: 리스트로 설정
drinks_foods_sul = ["위스키", "와인","소주","고량주"]
drinks_foods_anzu = ["초콜릿","치즈", "삼겹살", "양꼬치" ]
prices_sul = [50_000, 30_000, 5_000, 7_500]
amounts = [0 for i in range(len(drinks_foods_sul))]
# amounts = list()
# for i in range(len(drinks_foods_sul)):
#     amounts.append(0)



# # 술, 안주 추가(extend)
# drinks_foods_sul.extend(["사케", "막걸리"])
# drinks_foods_anzu.extend(["광어회", "낙곱새"])
# prices_sul.extend([20_000, 3_000])


# 술, 안주 추가(append)
drinks_foods_sul.append("사케")
drinks_foods_anzu.append("광어회")
prices_sul.append(20_000)
prices_sul.append(3_000)
amounts.append(0)
drinks_foods_anzu[0] = "낙곱새"




 total_price = 0

def print_menu_total_price(n):
    global total_price
    print(f'{drinks_foods_sul[n]}에 어울리는 안주는 {drinks_foods_anzu[n]} 입니다')
    print(f'가격은  {prices_sul[n]} 입니다')
    amounts[n] = amounts[n] + 1
    total_price = total_price + prices_sul[n]




menu_list = '다음  술 중에 고르세요\n'
for i in range(len(drinks_foods_sul)):
    menu_list = menu_list +f'{i+1}) {drinks_foods_sul[i]}\t\t'
menu_list = menu_list + f'{len(drinks_foods_sul) +1}) 아무거나\t\t {len(drinks_foods_anzu)+2} 종료 :'


while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks_foods_anzu):
        print_menu_total_price(menu - 1)
    elif menu == len(drinks_foods_anzu) +1:
        random_index = random.randint(0, len(drinks_foods_anzu) - 1)
        print(f'{drinks_foods_sul[random_index]}에 어울리는 안주는 {drinks_foods_anzu[random_index]}입니다.')
    # elif menu == len(drinks_foods_anzu) +2:
    else:
        print(f'다음에 또 오세요')
        break

# for k in range(len(drinks_foods_sul)):
#     if amounts[k] != 0:
#         print(f"주류명: {drinks_foods_sul[k]} 수량: {amounts[k]} 단가:{prices_sul[k]} 소계: {prices_sul[k] * amounts[k]}")
# print(f"총 금액: {total_price}원")


print("\n=== 주문 내역 ===")
for i in range(len(drinks_foods_sul)):
    if amounts[i] > 0:
        print(f'주류명: {drinks_foods_sul[i]}\n | 수량: {amounts[i]:>2} | 단가: {prices_sul[i]:>6} | 소계: {prices_sul[i] * amounts[i]:>5}')
print(f'총 금액: {total_price}원')