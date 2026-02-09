# 1. 몇 개의 숫자를 입력할지 사용자로부터 입력 받음
count = int(input("몇 개의 숫자를 입력하시겠습니까? >>> "))

# 2. 입력받은 숫자들을 저장할 빈 리스트(numbers) 생성
numbers = []

# 3. 양수, 음수, 0의 개수를 저장할 변수 3개를 0으로 초기화
pos_count = 0
neg_count = 0
zero_count = 0

# 4. for 반복문을 사용하여 입력 받은 횟수만큼 숫자 입력 및 판별
for i in range(1, count + 1):
    num = int(input(f"{i}번째 숫자를 입력하시오 >>> "))
    numbers.append(num)  # 리스트에 추가

    # 숫자 판별
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1

# 최종 결과 출력
print(f"양수: {pos_count}개")
print(f"음수: {neg_count}개")
print(f"0: {zero_count}개")
