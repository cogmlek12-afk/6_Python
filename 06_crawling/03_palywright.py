import requests
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks

# ssr : server side rendering. 서버에서 완성된 화면을 응답.
# csr : client side rendering. 

ssr = requests.get(f"{BASE}/stocks", headers=HEADERS, timeout=TIMEOUT)
csr = requests.get(f"{BASE}/csr/stocks", headers=HEADERS, timeout=TIMEOUT)

print(f"{'경로':<20}{'상태':<8}{'본문 길이':>12}")
print(f"{'/stocks (SSR)':<20}{ssr.status_code:<8}{len(ssr.text):>12}")
print(f"{'/csr/stocks (CSR)':<20}{csr.status_code:<8}{len(csr.text):>12}")

# csr 본문확인
for line in csr.text.strip().strip("\n"):
    print(f"{line}")

KEYWORD = '가온전자'
print(f"ssr --> {KEYWORD in ssr.text}")
print(f"csr --> {KEYWORD in csr.text}")
print("=" * 60)

# Playwright 동기 방식 API
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context(locale="ko-KR",
                                  viewport={"width": 1280, "height": 720})

    page = context.new_page()

    # page.route(패턴, 처리함수) : 특정패턴의 요청을 가로채서 직접 처리하는 함수
    # route.abort() : 요청을 취소
    # route.continue_() : 요청을 그대로 진행
    page.route(
        "**/*", 
        lambda route: route.abort() if route.request.resource_type in {"image", "font", "media"}
                                    else route.continue_()
    )

    page.goto(f"{BASE}/csr/stocks", wait_until='domcontentloaded')
    # wait_until
    #     - domcontentloaded : HTML을 다읽고 DOM트리가 만들어진 시점 (JS 실행 전)

    page.wait_for_selector("tr.stock-row")
    # 해당 선택자가 DOM에 그려질때까지 대기

    count = page.locator("tr.stock-row").count
    print(f" 렌더링 후 가져온 행의 개수: {count}")

    html = page.content()
    # print(f" page.content : {html}")

    items = parse_stocks(html)

    browser.close()

for data in items[:5]:
    print(f"{data['code']} : {data['name']} : {data['price']}")

    """
        * headless=False, slow_mo=1000
        화면을 직접 보면서 확인할 수 있음

        * 스크린샷, HTML 저장
            page.screenshot(path=".../screenshot.png", full_page=True)
            open("capture.html", "w", encoding="utf-8").write(page.content())
    """


