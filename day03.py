# Assignment
# 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정
# while문 안 쪽의 하드 코딩된 코드를 함수화하시오
# while문 안 쪽의 조건문을 줄이세요 hint. int로 하기
import random

# 술(sul), 안주(anzu) 설정: 리스트로 설정
drinks_foods_sul = ["위스키", "와인","소주","고량주"]
drinks_foods_anzu = ["초콜릿","치즈", "삼겹살", "양꼬치" ]

# 술, 안주 추가
drinks_foods_sul.extend(["사케", "막걸리"])
drinks_foods_anzu.extend(["광어회", "낙곱새"])


def print_menu(n):
    print(f'{drinks_foods_sul[n]}에 어울리는 안주는 {drinks_foods_anzu[n]} 입니다')



menu_list = '다음  술 중에 고르세요\n'
for i in range(len(drinks_foods_sul)):
    menu_list = menu_list +f'{i+1}) {drinks_foods_sul[i]}\t\t'
menu_list = menu_list + f'{len(drinks_foods_sul) +1}) 아무거나\t\t {len(drinks_foods_anzu)+2} 종료 :'


while True:
    menu = int(input(menu_list))
    if 1 <= menu <= len(drinks_foods_anzu):
        print_menu(menu - 1)
    elif menu == len(drinks_foods_anzu) +1:
        random_index = random.randint(0, len(drinks_foods_anzu) - 1)
        print(f'{drinks_foods_sul[random_index]}에 어울리는 안주는 {drinks_foods_anzu[random_index]}입니다.')
    # elif menu == len(drinks_foods_anzu) +2:
    else:
        print(f'다음에 또 오세요')
        break
