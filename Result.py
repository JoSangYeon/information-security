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

import Solution

SCRIPT = {
    "result1" : ["\'상\'은 조직과 조직원 간의 목표, 가치 등이 우수한 수준으로 일치한다는 의미입니다."+
                 "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동을 유지함으로써,"+
                 "\n조직원들이 조직의 방향을 이해하도록 돕는 것이 필요합니다.",
                 "\'중\'은 조직과 조직원 간의 목표, 가치 등이 양호한 수준에서 일치한다는 의미입니다."+
                 "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동에서 구성원의 가치를 이해하고"+
                 "\n지속적인 변화활동을 추진함으로써, 적합성을 추가 보완하는 것이 필요합니다.",
                 "\'하\'는 조직과 개인간의 목표, 가치 등의 일치성이 미흡한 수준임을 의미합니다."+
                 "\n따라서, 우리 조직은 구성원 들이 추구하는 가치, 목표 등을 검토하여,"+
                 "\n혁신적으로 조직문화를 개편함으로써, 일치성을 확보할 수 있도록 지원하는 것이 필요합니다. "
                 ],
    "result2": {"s1" : ["1. 최고경영층지원", "2. 보안규정(보상, 처벌 등)", "3. 정보보안 목표 및 가치", "4. 정보보안 시스템",
                        "5. 교육/훈련", "6. 홍보/캠페인", "7. 커뮤니케이션", "8. 보안문화", "9. 위기관리", "10. 기술지원(헬프데스크 등)"],
                "s2" : ["우리 회사 직원들이 고려하는 정보보안 활동은 다음과 같습니다.",
                        "첫째, 현수준 유지영역(A). 해당 영역은 정보보안 활동의 중요드는 낮으나, 만족도는 높은 영역으로서, "
                        +"\n{} 요인들의 \n지원을 유지하는 것이 필요합니다.",
                        "둘째, 유지/관리 지속영역(B). 해당 영역은 정보보안 활동의 중요도와 만족도를 높게 판단하는 영역으로서, "
                        +"\n{} 요인들의 \n높은 수준의 지원을 지속적으로 유지시키는 것이 필요합니다.",
                        "셋째, 만족도 제공영역(C). 해당 영역은 정보보안 활동의 중요돠 만족도 모두 낮은 영역으로서, "
                        +"\n{} 요인들의 \n지원에 대한 만족도를 개선할 수 있는 활동이 필요합니다.",
                        "넷째, 중점 개선영역(D). 해당 영역은 정보보안 활동의 중요도는 높으나, 만족도는 낮은 영역으로서,"
                        +"\n{} 요인들의 \n지원을 중점적으로 향상시키는 것이 필요합니다."]}
}
POINT = [(0.25,3.15, "A. 현수준 유지영역"), (3.9,4.5, "B. 유지/관리 지속영역"),
         (0.25,0.5, "C. 만족도 제공영역"), (4,0.5, "D. 중점 개선영역")]
AREA = [([0, 0, 2.5, 2.5], [2.5, 5, 5, 2.5]), ([2.5, 2.5, 5, 5], [2.5, 5, 5, 2.5]),
        ([0, 0, 2.5, 2.5], [0, 2.5, 2.5, 0]), ([2.5, 2.5, 5, 5], [0, 2.5, 2.5, 0])]

class Result1(tk.Frame):
    def __init__(self, app):
        """설문 데이터 import"""
        ind_att = pd.read_csv('individual_attribute.csv')
        cul_att = pd.read_csv('cultural_attribute.csv')

        self.ind_r = self.calc_mean(ind_att)
        self.cul_r = self.calc_mean(cul_att)
        print("개인 요인별 평균 :", self.ind_r)
        print("기업 요인별 평균 :", self.cul_r)

        self.result = self.calc_PO_fit(self.ind_r, self.cul_r)
        print("적합도 제곱근 :",pd.DataFrame(self.result[0], index=["과업중심","관계중심","손해회피","이익추구"]))
        print("적합도 산출 결과 :", pd.Series(self.result[1]))
        print("적합도 Score :", self.result[2])

        """데이터 시각화"""
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("1150x500+420+200")

        self.container = tk.Frame(self)
        self.canvas_frame = tk.Frame(self.container) # 설문 결과를 보여주는 Frame
        self.script_frame = tk.Frame(self.container) # 설문 결과에 대한 설명을 보여주는 Frame
        font = tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold")

        title = ttk.Label(self, text="적합도 산출 결과", font=font)
        title.pack()

        fig = self.draw(self.result)
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)  #
        canvas.get_tk_widget().pack()

        bins = [0, 100/3, 100/3*2, 100]
        labels = ["하", "중", "상"]
        cut_off = str(pd.cut([self.result[-1]], bins, right=False, labels=labels))[2:3]
        desc1 = ttk.Label(self.script_frame, text="우리 회사와 직원간에는 총 '{}%'의 특성 적합도를 "
                                     "가지며 적합도 수준은 '{}'입니다.".format(self.result[-1], cut_off),
                          font=tkinter.font.Font(family="Malgun Gothic", size=12, weight="bold"))
        desc1.pack()

        if cut_off == "상":
            script = ttk.Label(self.script_frame, text=SCRIPT["result1"][0],
                                font=tkinter.font.Font(family="Malgun Gothic", size=11))
        elif cut_off == "중":
            script = ttk.Label(self.script_frame, text=SCRIPT["result1"][0],
                                font=tkinter.font.Font(family="Malgun Gothic", size=11, weight="bold"))
        else:
            script = ttk.Label(self.script_frame, text=SCRIPT["result1"][0],
                                font=tkinter.font.Font(family="Malgun Gothic", size=11, weight="bold"))
        script.pack()

        self.canvas_frame.pack(side="left")
        self.script_frame.pack(side="right")
        self.container.pack()

        next_btn = ttk.Button(self, text="다음", command=self.next)
        next_btn.pack()

    def calc_mean(self, data):
        """
        12개 문항을 3개씩 4개의 요인으로 나누고
        각 요인에 대한 설문 값의 평균을 구하는 함수
        :param data: pandas를 통해 추출한 설문 데이터 값
        :return: 각 요인에 대한 설문데이터 값의 평균(list)
        """
        means = np.array(list(dict(data.mean().round(2)).values()))
        result = []
        for i in range(0, len(means), 3):
            tmp = np.mean([means[i], means[i + 1], means[i + 2]]).round(2)
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
        my_palette = plt.cm.get_cmap("Set2", len(df))

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

        fig.legend(loc="lower left")

        return fig

    def next(self):
        self.app.switch_frame(Result2)

class Result2(tk.Frame):
    def __init__(self, app):
        """데이터 import"""
        df = pd.read_csv("Information_Security_Level.csv")
        self.data, self.result = self.calc_mean_and_zip(df)
        self.factors = self.quaternary(self.data)
        print(self.result)

        self.idx = -1
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("1150x500+380+200")
        font = tkinter.font.Font(family="Malgun Gothic", size=14, weight="bold")

        title = ttk.Label(self, text="정보보안 수준 결과", font=font)
        title.pack(pady=5)

        self.container = tk.Frame(self)
        self.canvas_frame = tk.Frame(self.container) # 설문 결과를 보여주는 Frame
        self.script_frame = tk.Frame(self.container) # 설문 결과에 대한 설명을 보여주는 Frame

        fig = self.draw(self.data)
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)

        self.display_script()

        self.btn_frame = tk.Frame(self.script_frame)
        previous_btn = ttk.Button(self.btn_frame, text="◀◀◀이전", command=self.on_previous)
        next_btn = ttk.Button(self.btn_frame, text="다음▶▶▶", command=self.on_next)
        previous_btn.pack(side="left")
        next_btn.pack(side="top")
        self.btn_frame.pack()

        return_btn = ttk.Button(self.script_frame, text="메인화면으로", command=self.on_return)
        return_btn.pack(side="bottom")

        self.canvas_frame.pack(side="left")
        self.script_frame.pack(side="right")

        self.container.pack()

    def calc_mean_and_zip(self, data):
        means = np.array(list(dict(data.mean().round(2)).values()))
        data = {"중요도" : means[range(1,len(means),2)], "만족도" : means[range(0,len(means),2)]}

        result = pd.DataFrame(data, index=SCRIPT["result2"]["s1"])
        return data, result

    def quaternary(self, data):
        factors = {"A": {"중요도":[],"만족도":[], "요인":[]}, "B": {"중요도":[],"만족도":[], "요인":[]},
                   "C": {"중요도":[],"만족도":[], "요인":[]}, "D": {"중요도":[],"만족도":[], "요인":[]}}
        temp = zip(data["중요도"],data["만족도"])
        for i,(x,y) in zip(range(10),temp):
            if x <= 2.5 and y > 2.5:
                factors["A"]["요인"].append(SCRIPT["result2"]["s1"][i].split(". ")[-1])
                factors["A"]["중요도"].append(x)
                factors["A"]["만족도"].append(y)
            elif x > 2.5 and y > 2.5:
                factors["B"]["요인"].append(SCRIPT["result2"]["s1"][i].split(". ")[-1])
                factors["B"]["중요도"].append(x)
                factors["B"]["만족도"].append(y)
            elif x <= 2.5 and y <= 2.5:
                factors["C"]["요인"].append(SCRIPT["result2"]["s1"][i].split(". ")[-1])
                factors["C"]["중요도"].append(x)
                factors["C"]["만족도"].append(y)
            else:
                factors["D"]["요인"].append(SCRIPT["result2"]["s1"][i].split(". ")[-1])
                factors["D"]["중요도"].append(x)
                factors["D"]["만족도"].append(y)
        return factors

    def draw(self, data):
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rc('legend', fontsize=6)

        fig = plt.figure(figsize=(5, 4.5))
        fig.set_facecolor('#F0F0F0')
        ax = fig.add_subplot()

        if self.idx <= -1:
            for i in range(10):
                ax.scatter(data["중요도"][i], data["만족도"][i], s=60,
                           label=SCRIPT["result2"]["s1"][i], marker='o')
                ax.text(data["중요도"][i], data["만족도"][i], str(i+1), fontsize=8)
        else:
            factor = self.factors[list(self.factors.keys())[self.idx]]
            for i in range(len(factor["요인"])):
                ax.scatter(factor["중요도"][i], factor["만족도"][i], s=75,
                           label=str(i+1)+". "+factor["요인"][i], marker='o')
                ax.text(factor["중요도"][i], factor["만족도"][i], str(i+1), fontsize=8)
            ax.fill(AREA[self.idx][0],AREA[self.idx][1], color="skyblue", alpha=0.5)

        for x,y,txt in POINT:
            ax.text(x,y,txt,fontsize=9)
        # plt.xlim(np.min(data["중요도"])-0.5,np.max(data["중요도"])+0.5)
        # plt.ylim(np.min(data["만족도"])-0.5,np.max(data["만족도"])+0.5)
        ax.plot([0,5],[0,5], "r-", alpha=0.75)
        ax.hlines(y=2.5, xmin=0, xmax=5, color="black", linewidth=1.5, linestyles="--", alpha=0.75)
        ax.vlines(x=2.5, ymin=0, ymax=5, color="black", linewidth=1.5, linestyles="--", alpha=0.75)

        ax.set_xlabel("중요도")
        ax.set_ylabel("만족도")
        ax.set_xlim(0,5)
        ax.set_ylim(0,5)
        fig.legend(loc="upper left")
        ax.grid(True)

        return fig

    def display_script(self):
        desc = ttk.Label(self.script_frame, text=SCRIPT["result2"]["s2"][0],
                               font=tkinter.font.Font(family="Malgun Gothic", size=12, weight="bold"))
        desc.pack(pady=5)
        self.descs = []
        for key,i in zip(self.factors.keys(), range(1,5)):
            self.descs.append(ttk.Label(self.script_frame,
                                   text=SCRIPT["result2"]["s2"][i].format(", ".join(self.factors[key]["요인"])),
                                   font=tkinter.font.Font(family="Malgun Gothic", size=9)))
            self.descs[-1].pack(pady=3, ipadx=1.5, ipady=1.5, ancho='w')

    def on_next(self):
        self.descs[self.idx].configure(font=tkinter.font.Font(family="Malgun Gothic", size=9, weight="normal"))
        self.idx = (self.idx+1)%4
        self.descs[self.idx].configure(font=tkinter.font.Font(family="Malgun Gothic", size=10, weight="bold"))
        fig = self.draw(self.data)
        self.canvas.get_tk_widget().grid_remove()
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        pass

    def on_previous(self):
        self.descs[self.idx].configure(font=tkinter.font.Font(family="Malgun Gothic", weight="normal"))
        self.idx = (self.idx-1)%4
        self.descs[self.idx].configure(font=tkinter.font.Font(family="Malgun Gothic", weight="bold"))
        fig = self.draw(self.data)
        self.canvas.get_tk_widget().grid_remove()
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def on_return(self):
        self.app.switch_frame(Solution.Main_Frame)