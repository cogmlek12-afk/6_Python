"""
    목록 파싱
"""

import requests, json, csv

from bs4 import BeautifulSoup

from config import BASE, TIMEOUT, HEADERS
from parsers import get_text, parse_stocks

resp = requests.get(f"{BASE}/stocks", headers=HEADERS, timeout=TIMEOUT)
resp.raise_for_status

html = resp.text

soup = BeautifulSoup(html, 'lxml')

row = soup.select_one("tr.stock-row")
try:
    row.select_one("td.test").text
except Exception as e:
    print(f"오류:: {e}")

print(f" {get_text(row, 'td.test')}")
print("=" * 60)

stocks = parse_stocks(html)

print(f"{'코드':<8}{'종목명':14}{'섹터':<10}{'현재가':>12}{'등락률':>9}")

for s in stocks:
    print(f"{s['code']:<8}{s['name']:<14}{s['sector']:<10}{s['price']:>12}{s['rate']:>9}")

print("=" * 60)

# json 저장하기
def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json(stocks, "stocks.json")

# cvs 저장하기
def save_csv(data, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())

        writer.writeheader()
        writer.writerows(data)

save_csv(stocks, "stocks.csv")