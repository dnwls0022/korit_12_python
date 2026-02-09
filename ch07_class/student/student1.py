# 클래스 스튜던트
class Student:
    #생성자 생성과 학생정보,스튜던트아이디, 성적딕셔너리 초기화
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        print(f'학생이름: {self.name}')
    #add_grade라는 메서드를 정의하여 subject와 score를 매개변수로 받아 grades 딕셔너리에 추가
    def add_grade(self,subject ,score ):
        self.grades[subject] = score

    #get_average_grade라는 메서드를 정의하여 grades 딕셔너리의 점수들을 기반으로 평균 성적을 계산하여 반환하시오.
    def get_average_grade(self):
        # 과목들의 합
        total = sum(self.grades.values())
        # 과목의 개수
        count = len(self.grades)
        # 평균구하기
        avg = total/count
        return avg

#평균은 모든과목의점수합하기 / 개수

# 4. Student 객체를 생성하고, 성적을 추가한 뒤, 평균 성적을 출력하시오.
# 실행 예:
# 학생 이름: 김일
# 평균 성적: 90.0점
student= Student(name='김일', student_id='23232')
student.add_grade(subject='국어', score=90)
avg = student.get_average_grade()
print('평균성적은: 90점입니다.')

