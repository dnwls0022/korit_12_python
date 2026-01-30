year= int(input('연도입력>>'))
if year % 400 == 0:
    print("윤년입니다.")
elif year % 100 == 0:
    print('윤년이아닙니다')
elif year % 4 == 0:
    print('윤년입니다.')
else:
    print('운년아닙니다.')


#논리연산자 사용한 풀이방식

#if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
 #   print(f'{year} 년은 윤년아님')
