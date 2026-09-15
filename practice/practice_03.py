"""
    실습용 사이트에서
        종목 메뉴 페이지(SSR)의 섹터를 "IT 서비스"로 검색한 결과 데이터를 추출

    - 요청주소 : ??
    TODO :오늘 0915 18시까지 이메일제출
"""

"""
    목록 파싱
"""
import requests

from bs4 import BeautifulSoup

from config import BASE, TIMEOUT, HEADERS
from parsers import get_text, parse_stocks

resp = requests.get(f"{BASE}/stocks?sector=S08&market=&q=", headers=HEADERS, timeout=TIMEOUT)
resp.raise_for_status()

html = resp.text

soup = BeautifulSoup(html, 'lxml')

stocks = parse_stocks(html)

print(f"{'코드':<8}{'종목명':14}{'섹터':<10}{'현재가':>12}{'등락률':>9}")

for s in stocks:
    print(f"{s['code']:<8}{s['name']:<14}{s['sector']:<10}{s['price']:>12}{s['rate']:>9}")

print("=" * 60)