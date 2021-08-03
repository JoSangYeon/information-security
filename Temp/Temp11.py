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
                        +"\n{} 요인들의 지원을 유지하는 것이 필요합니다.",
                        "둘째, 유지/관리 지속영역(B). 해당 영역은 정보보안 활동의 중요도와 만족도를 높게 판단하는 영역으로서, "
                        +"\n{} 요인들의 높은 수준의 지원을 지속적으로 유지시키는 것이 필요합니다.",
                        "셋째, 만족도 제공영역(C). 해당 영역은 정보보안 활동의 중요돠 만족도 모두 낮은 영역으로서, "
                        +"\n{} 요인들의 지원에 대한 만족도를 개선할 수 있는 활동이 필요합니다.",
                        "넷째, 중점 개선영역(D). 해당 영역은 정보보안 활동의 중요도는 높으나, 만족도는 낮은 영역으로서,"
                        +"\n{} 요인들의 지원을 중점적으로 향상시키는 것이 필요합니다."]}
}
POINT = [(0.25,3.15, "A. 현수준 유지영역"), (3.9,4.5, "B. 유지/관리 지속영역"),
         (0.25,0.5, "C. 만족도 제공영역"), (4,0.5, "D. 중점 개선영역")]
AREA = [([0, 0, 2.5, 2.5], [2.5, 5, 5, 2.5]), ([2.5, 2.5, 5, 5], [2.5, 5, 5, 2.5]),
        ([0, 0, 2.5, 2.5], [0, 2.5, 2.5, 0]), ([2.5, 2.5, 5, 5], [0, 2.5, 2.5, 0])]

class Result2(tk.Frame):
    def __init__(self, app):
        """데이터 import"""
        df = pd.read_csv("../Information_Security_Level.csv")
        self.data, self.result = self.calc_mean_and_zip(df)
        self.factors = self.quaternary(self.data)
        print(self.result)

        self.idx = -1
        tk.Frame.__init__(self, app)
        self.app = app
        font = tkinter.font.Font(family="나눔고딕", size=14, weight="bold")

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
        previous_btn = tk.Button(self.btn_frame, text="◀◀◀이전", command=self.on_previous)
        next_btn = tk.Button(self.btn_frame, text="다음▶▶▶", command=self.on_next)
        previous_btn.pack(side="left")
        next_btn.pack(side="top")
        self.btn_frame.pack()

        return_btn = tk.Button(self.script_frame, text="메인화면으로", command=self.on_return)
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
                               font=tkinter.font.Font(family="나눔고딕", size=12, weight="bold"))
        desc.pack(pady=5)
        self.descs = []
        for key,i in zip(self.factors.keys(), range(1,5)):
            self.descs.append(ttk.Label(self.script_frame,
                                   text=SCRIPT["result2"]["s2"][i].format(", ".join(self.factors[key]["요인"])),
                                   font=tkinter.font.Font(family="나눔고딕", size=10)))
            self.descs[-1].pack(pady=3, ipadx=1.5, ipady=1.5)

    def on_next(self):
        self.descs[self.idx].configure(font=tkinter.font.Font(size=10, weight="normal"))
        self.idx = (self.idx+1)%4
        self.descs[self.idx].configure(font=tkinter.font.Font(size=11, weight="bold"))
        fig = self.draw(self.data)
        self.canvas.get_tk_widget().grid_remove()
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        pass

    def on_previous(self):
        self.descs[self.idx].configure(font=tkinter.font.Font(size=10, weight="normal"))
        self.idx = (self.idx-1)%4
        self.descs[self.idx].configure(font=tkinter.font.Font(size=12, weight="bold"))
        fig = self.draw(self.data)
        self.canvas.get_tk_widget().grid_remove()
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def on_return(self):
        self.app.switch_frame(Solution.Main_Frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x480+380+200")

    r = Result2(root)
    r.pack()

    root.mainloop()
