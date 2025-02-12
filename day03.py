# Assignment
# 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정

import random

# 리스트로 변경
drinks_foods_sul = ["위스키", "와인","소주","고량주"]
drinks_foods_anzu = ["초콜릿","치즈", "삼겹살", "양꼬치" ]

# 리스트로 변경
# japan_drinks_foods_sul1 = "사케"
# japan_drinks_foods_sul2 = "위스키"
# drinks_foods_sul.append(japan_drinks_foods_sul1)
# drinks_foods_sul.append(japan_drinks_foods_sul2)
# japan_drinks_foods_anzu1 = "광어회"
# japan_drinks_foods_anzu2 = "낙곱새"
# drinks_foods_anzu.append(japan_drinks_foods_anzu1)
# drinks_foods_anzu.append(japan_drinks_foods_anzu2)

drinks_foods_sul.extend(["사케", "막걸리"])
drinks_foods_anzu.extend(["광어회", "낙곱새"])

menu_list = '다음  술 중에 고르세요\n'
for i in range(len(drinks_foods_sul)):
    menu_list = menu_list +f'{i+1}) {drinks_foods_sul[i]}\t\t'
menu_list = menu_list + f'{len(drinks_foods_sul) +1}) 아무거나\t\t {len(drinks_foods_anzu)+2} 종료 :'
# print(menu_list)

while True:
    menu = input(menu_list)
#   menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_sul[0]}   2) {drinks_foods_sul[1]}   3) {drinks_foods_sul[2]}   4) {drinks_foods_sul[3]}   5) {drinks_foods_sul[4]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods_sul[0]}에 어울리는 안주는 {drinks_foods_anzu[0]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods_sul[1]}에 어울리는 안주는 {drinks_foods_anzu[1]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods_sul[2]}에 어울리는 안주는 {drinks_foods_anzu[2]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods_sul[3]}에 어울리는 안주는 {drinks_foods_anzu[3]} 입니다')
    elif menu == '5':
        print(f'{drinks_foods_sul[4]}에 어울리는 안주는 {drinks_foods_anzu[4]} 입니다')
    elif menu == '6':
        random_index = random.randint(0,len(drinks_foods_anzu)-1)
        print(f'{drinks_foods_sul[random_index]}에 어울리는 안주는 {drinks_foods_anzu[random_index]}입니다.')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break