"""
    BeautifulSoup
        : HTML 및 XML 문서에서 원하는 데이터를 쉽게 추출 할 수 있도록 해주는 스크래핑 라이브러리

        1. requests로 요청 후 문자열 (html, xml)을 응답받음
        2. bs4의 find, select 를 활용해서 특정 텍스트 추출
"""
import requests
# ModuleNotFoundError: No module named 'requests'
# 위처럼 오류나면 모듈을 설치해야됨, pip install requests
from bs4 import BeautifulSoup

from config import BASE, TIMEOUT, HEAERS

resp = requests.get(f"{BASE}/stocks", headers=HEAERS, timeout=TIMEOUT)
resp.raise_for_status()

html = resp.text
print(f"{BASE}/stocks   [{resp.status_code}] {len(html):,}자")

print('-' * 60)

# 문자열 --> 태그 구조

# bs4 은 문자열을 DOM 트리처럼 다룰 수 있게 만들어줌
soup = BeautifulSoup(html, 'lxml')

print(f"title --> {soup.title.text if soup.title else '없음'}")

rows_select = soup.select("tr.stock-row")
print(f"tr.stock-row 개수 : {len(rows_select)}")

first = soup.select_one("tr.stock-row")
price_tag = first.select_one("td.col-price")
print(f"td.col-price text  : {price_tag.text}")
print(f"td.col-price text  : {price_tag.text!r}")

print(f"td.col-price text   : {price_tag.get_text()!r}")
print(f"td.col-price text   : {price_tag.get_text(strip=True)!r}")

name_link = first.select_one("td.col-name a")

print(f"name_link['href] : {name_link['href']}")
print(f"name_link.get('href') : {name_link.get('href')}")
print(f"name_link.get('href') : {name_link.get('href','없음')}")

for sel in ["td.col-code", "td.col-name a", "td.col-sector",
            "td.col-price", "td.col-change", "td.col-volume",
            "td.col-market span"]: 
   tag = first.select_one(sel)
   value = tag.get_text(strip=True) if tag else "없음"
   print(f"{sel:<20} {value}")