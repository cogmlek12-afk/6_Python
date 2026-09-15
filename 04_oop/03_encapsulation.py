"""
    캡슐화   
"""

# 네이밍 규칠 (_필드명 / _필드명) -> 파이썬에서는 private 없음
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._bank_code = "005"
        self.__balance = balance 

acc = Account("김누룽지", 8000)
print(f"owner : {acc.owner}")
print(f"_bank_code : {acc._bank_code}") # 오류x. 접근가능하지만, 직접접근하지말것
# print(f"__balance : {acc.__balance}") # 오류o. 접근불가

print(f" 실제 이름 : {[k for k in vars(acc)]}")
print(f" _Account__balance : {acc._Account__balance}")

# 네임 맹글링 (name mangling)

print("=" * 60)

# @property : 메소드를 속성(필드)처럼 사용하게 해주는 데코레이터
class SafeAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    #getter 
    @property
    def balance(self):
        """ getter """
        return self.__balance

    #setter
    @balance.setter
    def balance(self, value):
        """ setter """
        if value < 0:
            if value < 0:
                self.__balance = 0
                return
        self.__balance = value

    @property
    def info(self):
        return f"{self.owner} : {self.__balance:,}원"

sa = SafeAccount("박기태", 500000)

print(f"sa.balance : {sa.balance}")
sa.balance = 1000000
print(f"sa.balance : {sa.balance}")
#sa.balance = -99999

print(f"sa.info : {sa.info}")


