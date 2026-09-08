
print("=" * 60)
print("if / elif / else")
print("=" * 60)



value = 10

if value > 5:
     print("조건문 내부입니다")
     print("조건문 내에서 실행하고자 한다면 들여쓰기 필수")

print("조건문 외부")
print()

score = int(input("점수입력 : "))

if score >= 90:
     grade = "A"
elif score >= 80:
     grade = "B"
elif score >= 70:
     grade = "C"
else:
     grade = "F"

print(f"{score}점 => {grade}")
# 블록은 들여쓰기로 구분, 조건식 옆에는 콜론(:) 지정
# else if 대신 elif 사용

print()

print("=" * 60)
print("삼항 연산")
print("=" * 60)

# 참일 때 결과값 if 조건식 else 거짓일 때 결과값 
age = int (input("나이 입력 : "))
"""
if age >= 20:
     result = "성인"
else:
     result = "미성년자"
"""

result = "성인" if age >= 20 else "미성년자"
print(f"{age}세 -> {result}")

print("=" * 60)
print("match-case (java의 switch)")
print("=" * 60)

status = int(input("상태 코드 입력: "))

match status:
     case 200:
          result = "정상"
     case 404:
          result = "페이지 찾을 수 없음"
     case 500:
          result = "서버 오류"
     case _: 
          result = "알 수 없음"
print(f"{status} -> {result}")

print("=" * 60)
print(" pass ")
print("=" * 60)

# 빈 블록 작성할때사용 (오류방지)

score = 90

if score > 90:
     pass
else:
     print("--- else영역 ---")

n = 1

while True:
     if n > 3:
          break # 반복문 종료
     print(f"n : {n}")
     n += 1

