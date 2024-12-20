import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from math import pi
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

## 데이터 준비
df = pd.DataFrame({
    'Character': ['ind-cul'],
    '가나': [4.867**2],
    '다라': [3.933**2],
    '마바': [3.934**2],
    '사아': [3.8**2],
})
print(df)
plt.rcParams['font.family'] = 'Malgun Gothic'
## 하나로 합치기
labels = df.columns[1:]
num_labels = len(labels)

angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]  ## 각 등분점
angles += angles[:1]  ## 시작점으로 다시 돌아와야하므로 시작점 추가

my_palette = plt.cm.get_cmap("Set2", len(df.index))

fig = plt.figure(figsize=(8, 8))
fig.set_facecolor('white')
ax = fig.add_subplot(polar=True)
for i, row in df.iterrows():
    color = my_palette(i)
    data = df.iloc[i].drop('Character').tolist()
    data += data[:1]

    ax.set_theta_offset(pi / 2)  ## 시작점
    ax.set_theta_direction(-1)  ## 그려지는 방향 시계방향

    plt.xticks(angles[:-1], labels, fontsize=13)  ## 각도 축 눈금 라벨
    ax.tick_params(axis='x', which='major', pad=15)  ## 각 축과 눈금 사이에 여백을 준다.

    ax.set_rlabel_position(0)  ## 반지름 축 눈금 라벨 각도 설정(degree 단위)
    plt.yticks([0, 5, 10, 15, 20, 25], ['0', '5', '10', '15', '20', '25'], fontsize=10)  ## 반지름 축 눈금 설정
    plt.ylim(0, 25)

    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=row.Character)  ## 레이더 차트 출력
    ax.fill(angles, data, color=color, alpha=0.4)  ## 도형 안쪽에 색을 채워준다.

plt.legend(loc=(0.9, 0.9))
plt.show()

# ## 따로 그리기
# labels = df.columns[1:]
# num_labels = len(labels)
#
# angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]  ## 각 등분점
# angles += angles[:1]  ## 시작점으로 다시 돌아와야하므로 시작점 추가
#
# my_palette = plt.cm.get_cmap("Set2", len(df.index))
#
# fig = plt.figure(figsize=(15, 20))
# fig.set_facecolor('white')
#
# for i, row in df.iterrows():
#     color = my_palette(i)
#     data = df.iloc[i].drop('Character').tolist()
#     data += data[:1]
#
#     ax = plt.subplot(3, 2, i + 1, polar=True)
#     ax.set_theta_offset(pi / 2)  ## 시작점
#     ax.set_theta_direction(-1)  ## 그려지는 방향 시계방향
#
#     plt.xticks(angles[:-1], labels, fontsize=13)  ## x축 눈금 라벨
#     ax.tick_params(axis='x', which='major', pad=15)  ## x축과 눈금 사이에 여백을 준다.
#
#     ax.set_rlabel_position(0)  ## y축 각도 설정(degree 단위)
#     plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2', '4', '6', '8', '10'], fontsize=10)  ## y축 눈금 설정
#     plt.ylim(0, 10)
#
#     ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')  ## 레이더 차트 출력
#     ax.fill(angles, data, color=color, alpha=0.4)  ## 도형 안쪽에 색을 채워준다.
#
#     plt.title(row.Character, size=20, color=color, x=-0.2, y=1.2, ha='left')  ## 타이틀은 캐릭터 클래스로 한다.
#
# plt.tight_layout(pad=5)  ## subplot간 패딩 조절
# plt.show()