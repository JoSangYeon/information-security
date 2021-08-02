"""
메뉴얼

① 각 해당 문항의 집단(개인차 변인, 집단차 변인으로 구성) 평균 점수
② 3개로 구성된 해당문항의 평균값 산출, 수식 = 각 3개 문항 평균
③ P-O fit sub-score: 각 요인별 점수 차이, 수식 = (5-abs(개인요인평균 – 집단요인평균))^2 : 범위 0~25
④ P-O fit total score : P-O fit sub-score 값들의 총합의 제곱근
⑤ P-O fit total score × 10 = 100 분위 점수 변경
⑥ 상중하 집단 구분: 1/3 씩 동일한 급간으로 구분

1. individual 속성에서 각 요인(총 4개)마다의 평균을 구함
1-1. 4개의 요인중 각각의 질문에 대한 평균 == 그냥 해당 요인의 모든 값의 평균
1-2. 개인은 설문을 한 당사자의 값으로만 판단
```
np.mean([aa,bb,cc])
Out[29]: 4.333333333333333
np.mean([2,5,4,1,6,6,3,5,6,6,5,5,3,5,2,6,4,4])
Out[30]: 4.333333333333333
```
2. 1과 같이 cultural 속성에서도 같이 값을 구함
2-1. 기업요인은 전체의 설문 데이터의 평균을 구함
3. 1(a)과 2(b)의 차이의 절대값(abs(a-b))를 5에서 뺌 즉, 5-abs(a-b)
4. 3에서 얻은 값을 => P-O fit total score
5. sum(P-O fit total score) * 5
5-1. sum(P-O fit total score) / 2 * 10
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import tkinter as tk
import tkinter.font
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Result1(tk.Frame):
    def __init__(self, app):
        """설문 데이터 import"""
        ind_att = pd.read_csv('individual_attribute.csv')
        cul_att = pd.read_csv('cultural_attribute.csv')

        ind_data = np.array(ind_att.iloc[:, 1:].values.tolist())  # 개인 특성 전체
        cul_data = np.array(cul_att.iloc[:, 1:].values.tolist())  # 조직 특성 전체
        self.ind_r = self.calc_mean(ind_data)
        self.cul_r = self.calc_mean(cul_data)
        print("개인 요인별 평균 :", self.ind_r)
        print("기업 요인별 평균 :", self.cul_r)

        self.result = self.calc_PO_fit(self.ind_r, self.cul_r)
        print("적합도 산출 결과 :",self.result)

        """데이터 시각화"""
        tk.Frame.__init__(self, app)
        self.app = app
        font = tkinter.font.Font(family="나눔고딕", size=16, weight="bold")

        title = ttk.Label(self, text="적합도 산출 결과", font=font)
        title.grid(row=0, column=10, pady=5)

        fig = self.draw(self.result)
        canvas = FigureCanvasTkAgg(fig, master=self)  #
        canvas.get_tk_widget().grid(row=1, column=10, pady=3)  #

        bins = [0, 100/3, 100/3*2, 100]
        labels = ["하", "중", "상"]
        cut_off = str(pd.cut([self.result[-1]], bins, right=False, labels=labels))[2:3]
        desc1 = ttk.Label(self, text="우리 회사와 직원간에는 총 '{}%'의 특성 적합도를 "
                                     "가지며 적합도 수준은 '{}'입니다.".format(self.result[-1], cut_off),
                          font=tkinter.font.Font(family="나눔고딕", size=12))
        desc1.grid(row=2, column=10)

        if cut_off == "상":
            script = ttk.Label(self, text="\'상\'은 조직과 조직원 간의 목표, 가치 등이 우수한 수준으로 일치한다는 의미입니다."
                                           "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동을 유지함으로써, "
                                          "\n조직원들이 조직의 방향을 이해하도록 돕는 것이 필요합니다. ",
                                font=tkinter.font.Font(family="나눔고딕", size=10))
        elif cut_off == "중":
            script = ttk.Label(self, text="\'중\'은 조직과 조직원 간의 목표, 가치 등이 양호한 수준에서 일치한다는 의미입니다. "
                                           "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동에서 구성원의 가치를 이해하고 "
                                          "\n지속적인 변화활동을 추진함으로써, 적합성을 추가 보완하는 것이 필요합니다.",
                                font=tkinter.font.Font(family="나눔고딕", size=10))
        else:
            script = ttk.Label(self, text="\'하\'는 조직과 개인간의 목표, 가치 등의 일치성이 미흡한 수준임을 의미합니다. "
                                           "\n따라서, 우리 조직은 구성원 들이 추구하는 가치, 목표 등을 검토하여,"
                                          "\n혁신적으로 조직문화를 개편함으로써, 일치성을 확보할 수 있도록 지원하는 것이 필요합니다. ",
                                font=tkinter.font.Font(family="나눔고딕", size=10))
        script.grid(row=3, column=10)

        next_btn = ttk.Button(self, text="다음", command=self.next)
        next_btn.grid(row=4, column=10)

    def calc_mean(self, data):
        """
        12개 문항을 3개씩 4개의 요인으로 나누고
        각 요인에 대한 설문 값의 평균을 구하는 함수
        :param data: pandas를 통해 추출한 설문 데이터 값
        :return: 각 요인에 대한 설문데이터 값의 평균(list)
        """
        T_data = data.T
        result = []
        for i in range(0, len(T_data), 3):
            tmp = np.mean([T_data[i], T_data[i + 1], T_data[i + 2]]).round(3)
            # print(T_data[i], end=", ")
            # print(T_data[i + 1], end=", ")
            # print(T_data[i + 2], "=>", tmp)
            result.append(tmp)
        return result

    def calc_PO_fit(self, ind, cul):
        ind = np.array(ind)
        cul = np.array(cul)

        PO_sub = 5-np.abs(ind-cul)
        score = (np.sum(5-np.abs(ind-cul))/2*10).round(3)

        keys = ["과업중심", "관계중심", "손해회피", " 이익추구"]
        dict_r = {key : round(value**2,2) for key, value in zip(keys, PO_sub)}
        return PO_sub, dict_r ,score

    def draw(self, data):
        df = pd.DataFrame(data[1], index=["개인-조직특성 적합도"])

        labels = df.columns[:]
        num_labels = len(labels)

        angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]  ## 각 등분점
        angles += angles[:1]  ## 시작점으로 다시 돌아와야하므로 시작점 추가

        plt.rcParams['font.family'] = 'Malgun Gothic'
        my_palette = plt.cm.get_cmap("Set2", 1)

        fig = plt.figure(figsize=(5, 4))
        fig.set_facecolor('#F0F0F0')
        ax = fig.add_subplot(polar=True)
        for i,(idx, row) in zip(range(len(df)), df.iterrows()):
            color = my_palette(i)
            data = df.iloc[i].tolist()
            data += data[:1]

            ax.set_theta_offset(pi / 2)  ## 시작점
            ax.set_theta_direction(-1)  ## 그려지는 방향 시계방향

            plt.xticks(angles[:-1], labels, fontsize=13)  ## 각도 축 눈금 라벨
            ax.tick_params(axis='x', which='major', pad=15)  ## 각 축과 눈금 사이에 여백을 준다.

            ax.set_rlabel_position(0)  ## 반지름 축 눈금 라벨 각도 설정(degree 단위)
            plt.yticks([0, 5, 10, 15, 20, 25], ['0', '5', '10', '15', '20', '25'], fontsize=12)  ## 반지름 축 눈금 설정
            plt.ylim(0, 25)

            ax.plot(angles, data, color=color, marker='o',linewidth=2, linestyle='solid', label=idx)  ## 레이더 차트 출력
            ax.fill(angles, data, color=color, alpha=0.4)  ## 도형 안쪽에 색을 채워준다.
        for i in range(len(data)-1):
            ax.text(angles[i], data[i], data[i], fontsize=9)

        fig.legend(loc="upper right")

        return fig

    def next(self):
        self.app.switch_frame(Result2)

class Result2(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        font1 = tkinter.font.Font(family="나눔고딕", size=14, weight="bold")

        title = ttk.Label(self, text="정보보안 수준 결과", font=font1)
        title.pack(pady=5)