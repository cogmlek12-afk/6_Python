"""
차트 관련 설정
"""

import platform
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

# ==========================================
# 한글 폰트 설정
# ==========================================

_DEFAULT_FONT = {
    "Windows": ["Malgun Gothic"],
    "Darwin": ["AppleGothic"],
}


def setup():
    """
    운영체제에 맞는 한글 폰트 설정
    """
    system = platform.system()
    fonts = _DEFAULT_FONT.get(system, [])

    for font in fonts:
        if any(font == f.name for f in font_manager.fontManager.ttflist):
            plt.rcParams["font.family"] = font
            break

    # 마이너스 기호 깨짐 방지
    plt.rcParams["axes.unicode_minus"] = False


# ==========================================
# 그래프 저장 폴더
# ==========================================

OUTPUT_DIR = Path(__file__).parent / "output"


def out(filename):
    """
    그래프 저장 경로를 만들어주는 함수
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR / filename