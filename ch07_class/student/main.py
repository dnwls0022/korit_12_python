class Student:
    # 생성자 정의
    def __init__(self, name, student_id):
        # 💡 주의: @property를 쓰려면 내부 저장 변수 이름은 self._name처럼 언더바를 붙이는 게 관례예요.
        self._name = name
        self.student_id = student_id
        # 성적을 저장하기 위한 빈 딕셔너리 -> 과목명을 key / 점수를 value로 예정
        self._grade = {}

    # python 버전의 getter에 해당하는 메서드 정의 방식
    @property
    def name(self):
        return self._name

    # python 버전의 setter의 예시
    @name.setter
    def name(self, value):
        self._name = value

# --- 여기서부터는 벽에 딱 붙여주세요! (클래스 밖) ---
# 객체 생성
student1 = Student('김일', 2026001)

# 게터 호출 (소괄호 없이 변수처럼!)
print(f'학생이름: {student1.name}')

# 세터 호출 (대입 연산자 = 사용)
student1.name = '김영'

# 게터 재호출
print(f'변경된 학생이름: {student1.name}')
print(student1._name)

'''
java기준으로 python코드를 해석할때 의문....
1. name이라는 속성이있지만 객체명.name을 통해서 '김일','김이'라는 속성값이 출력된다: 근데 객체명 ._name도 작동한다.

2. 객체명._name = '김영'이 아닌 객체명.name = '김영' 으로 재대입한것처럼 보이지 setter의; 호출로 보이지않는다는 점 당연히 객체명.set

그런데 이건 Java 기준으로 본거고, python으로 풀었을 때는, _name / name이 서로 다른 개념으로 보이지만 '_'가 붙으면 파이썬 언어 내부적으로 동일한 속성으로 처리해줍니다.

객체명.속성명 뒤에 ()가 없음에도 불구하고 파이썬은 이걸 그냥 메서드처럼 처리해준다는 점입니다. 그래서 그냥 객체명.속성명이면 getter로 처리해주고 '객체명.속성명 = 데이터'면 알아서 setter로 처리해줍니다.

그런데 그  '알아서'처리하기 위한 필수작업이 '@property'와 '속성명.setter'라는 데코레이터 떄문이다.

원래는 자동생성되기 때문에 일일이 @달고 _속성명인지/그냥 속성명인지 따질필요가없다..
파이썬으로
'''