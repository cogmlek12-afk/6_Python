"""
   문자열 다루기
"""

print("=" * 60)
print("인덱싱, 슬라이싱")
print("=" * 60)

# 인덱스는 0부터 시작

message = "Love grows in little moments"
print(f"메세지 : {message}")
print()
print(f"첫글자 : {message[0]}")
print(f"마지막글자 : {message[-1]}")

# 슬라이싱 : 변수[시작:끝:간격]
print(f"{message[0:7:1]} / {message[0:7]} / {message[:15]}")
print(f"{message[7:]}")
print(f"{message[::2]}") # 2칸 간격
print(f"{message[::-1]}") # -1. 역순

# 대문자 변환 : upper()
print(f"대문자 변환: {message.upper()}")
# 소문자 변환 : lower()
print(f"소문자 변환: {message.lower()}")

message = "    Eat again, big pink pig           "
print(f"[{message}]")
# 좌우 공백 제거 : strip()
print(f":좌우 공백 제거 : [{message.strip()}]")

# 문자열을 구분자로 분할: split(구분자)
print(f"split : [{message.split(',')}]")

# 특정 문자 개수 반환 : count(문자)
print(f"1의 개수: {message.count('p')}")

# 특정 문자의 인덱스 반환 : find(문자)
print(f"Eat의 위치 : {message.find('pink')}")
print(f"JAVA의 위치 : {message.find('JAVA')}")

# 리스트 --> 문자열 (문자열 결합)
today = '-'.join(['2026', '09', '07'])
print(f"today : {today} ({type(today)})")

print("=" * 60)

# 여러 줄 문자열 => 따옴표 3개
end_message = """
    문자열 다루기
    - 인덱싱, 슬라이싱
    - 자주 사용하는 메소드 (split, join, strip, ...)
"""

print(end_message)
