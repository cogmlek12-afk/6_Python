"""
    예외처리
    try / except / else / finally
"""

# 함수 정의 : divide
#   데이터를 하나 전달받아 정수로 변환
#   변환된 값으로 100을 나누느 겨로가 출력
def divide(text):
    try:
        num = int(text)
        result = 100 / num
        print(f"결과: {result}")
    except ValueError:
        print(f"{text} : 숫자가 아닙니다.")
    except ZeroDivisionError:
        print(f"{text} : 0으로 나눌 수 없습니다.")
    except Exception as e:
        print(f"{text} : {e}")
    else:
        print(f"결과: {result}")
    finally:
        pass 

for t in ["100", "-5", "abc", "0"]:
    divide(t)

print("=" * 60)

# 사용자 정의 예외 / 예외 발생 (raise)
class NoBalanceError(Exception):
    """ 잔액 부족 예외 """
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"잔액 부족: 현재 {balance}, 요청: {amount}")

class InvalidAmountError(ValueError):
    """ 금액 잘못된 경우 예외 """

class Account:
    """ 은행 계좌를 나타내는 클래스 """
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        """
            계좌에서 출금하는 메소드
            
            Args:
                amount (int): 출금할 금액
        """
        if amount <= 0:
                    raise InvalidAmountError("출금액 0보다 커야됨")
        
        if amount > self.balance:
            raise NoBalanceError(self.balance, amount)

        self.balance -= amount
        return amount

    def __str__(self):
         return f"[{self.owner}] 잔액 : {self.balance:,}원"

acc = Account("이웅진", 30000)
print(acc)

for amount in[5000, 50000, -1000]:
    try:
        acc.withdraw(amount)
    except NoBalanceError as e:
        print(f"출금 실패 : {e}")
    except InvalidAmountError as e:
        print(f"출금 실패 : {e}")
    else:
        print(f"출금 성공 : {amount}원")