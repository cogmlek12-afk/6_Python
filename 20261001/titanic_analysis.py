import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------
# 1. train.csv 파일 불러오기
# ----------------------------------------------------
df = pd.read_csv('train.csv')

# ----------------------------------------------------
# 2. 상위 5개 행 출력
# ----------------------------------------------------
print("=== 2번: 상위 5개 행 ===")
print(df.head())

# ----------------------------------------------------
# 3. 데이터 정보 확인
# ----------------------------------------------------
print("\n=== 3번: df.info() ===")
df.info()

# ----------------------------------------------------
# 4. Age, Fare의 평균값, 최솟값, 최댓값 (소수점 2자리 반올림)
# ----------------------------------------------------
print("\n=== 4번: Age, Fare 기술통계 ===")
print(f"Age - 평균: {df['Age'].mean():.2f}, 최솟값: {df['Age'].min():.2f}, 최댓값: {df['Age'].max():.2f}")
print(f"Fare - 평균: {df['Fare'].mean():.2f}, 최솟값: {df['Fare'].min():.2f}, 최댓값: {df['Fare'].max():.2f}")

# ----------------------------------------------------
# 5. 생존자와 사망자 수 계산
# ----------------------------------------------------
survived_counts = df['Survived'].value_counts()
print("\n=== 5번: 생존자 및 사망자 수 ===")
print(f"생존자(1): {survived_counts.get(1, 0)}명, 사망자(0): {survived_counts.get(0, 0)}명")

# ----------------------------------------------------
# 6. 객실 등급(Pclass)별 탑승객 수
# ----------------------------------------------------
print("\n=== 6번: Pclass별 탑승객 수 ===")
print(df['Pclass'].value_counts().sort_index())

# ----------------------------------------------------
# 7. 50세 이상 탑승객 추출
# ----------------------------------------------------
df_over_50 = df[df['Age'] >= 50]
print(f"\n=== 7번: 50세 이상 탑승객 수: {len(df_over_50)}명 ===")

# ----------------------------------------------------
# 8. AgeGroup 열 추가
# ----------------------------------------------------
def get_age_group(age):
    if pd.isna(age):
        return '미확인'
    elif age < 10:
        return '아동'
    elif age < 20:
        return '10대'
    elif age < 30:
        return '20대'
    elif age < 40:
        return '30대'
    elif age < 50:
        return '40대'
    elif age < 60:
        return '50대'
    else:
        return '60대 이상'

df['AgeGroup'] = df['Age'].apply(get_age_group)
print("\n=== 8번: AgeGroup 추가 후 상위 5개 행 ===")
print(df[['Age', 'AgeGroup']].head())

# ----------------------------------------------------
# 9. 성별(Sex) 및 객실 등급(Pclass)별 평균 생존율
# ----------------------------------------------------
print("\n=== 9번: 성별 및 Pclass별 평균 생존율 ===")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean().round(2))

# ----------------------------------------------------
# 10. 나이대별(AgeGroup) 평균 생존율
# ----------------------------------------------------
print("\n=== 10번: AgeGroup별 평균 생존율 ===")
print(df.groupby('AgeGroup')['Survived'].mean().round(2))

# ----------------------------------------------------
# 11. 결측치 총 개수 및 비율 (내림차순)
# ----------------------------------------------------
null_counts = df.isnull().sum()
null_ratios = (df.isnull().sum() / len(df) * 100).round(2)
missing_df = pd.DataFrame({'결측치 개수': null_counts, '비율(%)': null_ratios}).sort_values(by='결측치 개수', ascending=False)
print("\n=== 11번: 결측치 현황 ===")
print(missing_df)

# ----------------------------------------------------
# 12. Sex 인코딩 (Gender_Encoded 추가)
# ----------------------------------------------------
df['Gender_Encoded'] = df['Sex'].map({'male': 0, 'female': 1})
print("\n=== 12번: Gender_Encoded 확인 ===")
print(df[['Sex', 'Gender_Encoded']].head())

# ----------------------------------------------------
# 13. 탑승지(Embarked)별 평균 Fare
# ----------------------------------------------------
print("\n=== 13번: Embarked별 평균 Fare ===")
print(df.groupby('Embarked')['Fare'].mean().round(2))

# ----------------------------------------------------
# 14. Pclass x Sex 피벗 테이블 (Fare 평균)
# ----------------------------------------------------
pivot_fare = df.pivot_table(index='Pclass', columns='Sex', values='Fare', aggfunc='mean').round(2)
print("\n=== 14번: Pclass x Sex Fare 피벗 테이블 ===")
print(pivot_fare)

# ----------------------------------------------------
# 15. FamilySize 생성 및 요약 통계
# ----------------------------------------------------
df['FamilySize'] = df['SibSp'] + df['Parch']
print("\n=== 15번: FamilySize 요약 통계 ===")
print(df['FamilySize'].describe().round(2))

# ----------------------------------------------------
# 16. Title 추출 및 가장 흔한 5개 호칭
# ----------------------------------------------------
df['Title'] = df['Name'].str.extract(r', ([A-Za-z]+)\.', expand=False)
print("\n=== 16번: 상위 5개 Title ===")
print(df['Title'].value_counts().head(5))

# ----------------------------------------------------
# 17. Title별 승객 수, 평균 나이, 평균 생존율
# ----------------------------------------------------
title_agg = df.groupby('Title').agg(
    승객수=('PassengerId', 'count'),
    평균나이=('Age', 'mean'),
    평균생존율=('Survived', 'mean')
).round(2)
print("\n=== 17번: Title별 집계 ===")
print(title_agg)

# ----------------------------------------------------
# 18. 생존/사망별 Age 분포 시각화 및 이미지 저장
# ----------------------------------------------------
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='Age', hue='Survived', common_norm=False, fill=True)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(labels=['Survived (1)', 'Dead (0)'])
plt.tight_layout()
plt.savefig('survival_age_distribution.png')
plt.close()
print("\n=== 18번: 'survival_age_distribution.png' 저장 완료 ===")

# ----------------------------------------------------
# 19. Title과 Pclass 기준 Age 결측치 대치
# ----------------------------------------------------
group_medians = df.groupby(['Title', 'Pclass'])['Age'].transform('median')
df['Age'] = df['Age'].fillna(group_medians)
df['Age'] = df['Age'].fillna(df['Age'].median())  # 예외적 전체 결측 처리
print(f"\n=== 19번: 대치 후 Age 결측치 개수: {df['Age'].isnull().sum()}개 ===")

# ----------------------------------------------------
# 20. 상관관계 행렬 계산 및 히트맵 저장
# ----------------------------------------------------
plt.figure(figsize=(8, 6))
numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
corr_matrix = df[numeric_cols].corr().round(2)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()
print("=== 20번: 'correlation_heatmap.png' 저장 완료 ===")