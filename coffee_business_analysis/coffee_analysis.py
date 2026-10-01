"""
연령 & 고객 데이터 산점도(Scatter Plot) 시각화 분석
"""

# 화면 출력이 필요한 경우 아래 줄을 주석 처리(#) 하세요.
import matplotlib
matplotlib.use("Agg")

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# chart_config 설정 불러오기
from chart_config import setup, OUTPUT_DIR

# 1. 폰트 및 스타일 초기화
setup()
sns.set_theme(style="whitegrid", font=plt.rcParams["font.family"])

# 2. 전용 저장 폴더 설정 (output/coffee_charts)
COFFEE_OUTPUT_DIR = OUTPUT_DIR / "coffee_charts"


def coffee_out(filename: str) -> Path:
    """커피 차트 전용 출력 경로 생성 함수"""
    COFFEE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return COFFEE_OUTPUT_DIR / filename


# 3. 수치형 데이터 준비 (샘플 데이터 생성)
np.random.seed(42)
n_samples = 300

# 나이, 결제 금액, 월 방문 횟수, 선호 커피
ages = np.random.randint(18, 65, size=n_samples)
visit_counts = np.random.poisson(lam=8, size=n_samples) + 1
base_amount = 3000 + (visit_counts * 500) + np.random.normal(0, 1500, n_samples)
total_spend = np.clip(base_amount, 2000, 30000)

coffee_choices = ["아메리카노", "카페라떼", "바닐라라떼", "콜드브루"]
preferred_coffee = np.random.choice(coffee_choices, size=n_samples)

df = pd.DataFrame({
    "age": ages,
    "visit_count": visit_counts,
    "total_spend": total_spend,
    "preferred_coffee": preferred_coffee
})


# ==========================================
# 차트 1. 기본 산점도 (나이 vs 결제 금액) + 커피 종류별 구분 (Hue)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="age",
    y="total_spend",
    hue="preferred_coffee",
    style="preferred_coffee",
    s=70,             # 점 크기
    alpha=0.8,        # 투명도
    palette="Set1",
    ax=ax
)

ax.set_title("연령과 결제 금액의 관계 (커피 선호도별)", fontsize=14, pad=12)
ax.set_xlabel("나이 (세)")
ax.set_ylabel("평균 결제 금액 (원)")
ax.legend(title="선호 커피", bbox_to_anchor=(1.02, 1), loc="upper left")

fig.tight_layout()
fig.savefig(coffee_out("01_age_vs_spend_scatter.png"), dpi=120)
plt.close(fig)


# ==========================================
# 차트 2. 버블 차트 (나이 vs 결제 금액 + 점 크기에 방문 횟수 반영)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

scatter = sns.scatterplot(
    data=df,
    x="age",
    y="total_spend",
    size="visit_count",        # 버블 크기
    sizes=(30, 300),           # 최소/최대 점 크기
    hue="visit_count",         # 방문 횟수에 따른 색상 명암
    palette="viridis",
    alpha=0.7,
    ax=ax
)

ax.set_title("연령 vs 결제 금액 (점 크기 및 색상 = 월 방문 횟수)", fontsize=14, pad=12)
ax.set_xlabel("나이 (세)")
ax.set_ylabel("평균 결제 금액 (원)")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", title="월 방문 횟수")

fig.tight_layout()
fig.savefig(coffee_out("02_bubble_chart_scatter.png"), dpi=120)
plt.close(fig)


# ==========================================
# 차트 3. 추세선이 포함된 산점도 (회귀선 추세 파악)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

sns.regplot(
    data=df,
    x="visit_count",
    y="total_spend",
    scatter_kws={"s": 50, "alpha": 0.6, "color": "darkbrown"},
    line_kws={"color": "red", "linewidth": 2},
    ax=ax
)

ax.set_title("월 방문 횟수와 결제 금액 간 추세 분석 (Regplot)", fontsize=14, pad=12)
ax.set_xlabel("월 방문 횟수 (회)")
ax.set_ylabel("평균 결제 금액 (원)")

fig.tight_layout()
fig.savefig(coffee_out("03_trend_regplot_scatter.png"), dpi=120)
plt.close(fig)

print("✅ 산점도 생성 성공! output/coffee_charts 폴더에 그래프가 저장되었습니다.")