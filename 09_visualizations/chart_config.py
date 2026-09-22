"""
    차트 관련 설정
"""
import platform 
from pathlib import Path

from matplotlib  import font_manager
"""
==========================
    한글 폰트 설정
==========================
운영체제별로 기본한글폰트 (기본으로 설치된 항목)
"""
_DEFAULT_FONT = {
    "Windows": ["Malgun Gothic"], 
    "Darwin" : ["AppleGothic"],
}
_FALLBACK = ["NanumGothic", "Noto Sans CJK KR", "Noto Sans CJK JP", "IPAGothic"]

def find_korean_font():

    installed = {r.name for r in font_manager.fontManager.ttflist}

    for name in _DEFAULT_FONT.get(platform.system(), [])+ _FALLBACK:
        if name in installed:
            return name

    return None

OUTPUT_DIR = Path(__file__).with_name("output") 

def out(name): 
    OUTPUT_DIR.mkdir(exist_ok=True)

    return OUTPUT_DIR / name

def saved_files():
    OUTPUT_DIR.mkdir(exist_ok=True)

    return sorted(p.name for p in OUTPUT_DIR.iterdir() if p.is_file())
    



def setup(theme=True):

    pass
