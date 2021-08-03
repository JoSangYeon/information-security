import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

SCRIPT = ["1. 최고경영층지원", "2. 보안규정(보상, 처벌 등)", "3. 정보보안 목표 및 가치", "4.정보보안 시스템",
          "5. 교육/훈련", "6. 홍보/캠페인", "7. 커뮤니케이션", "8. 보안문화", "9. 위기관리", "10.기술지원(헬프데스크 등)"]
POINT = [(0.5,3.5, "A. 현수준 유지 영역"), (4.5,4.5, "B. 유지/관리 지속 영역"),
         (0.5,0.5, "C. 만족도 제공영역"), (4.5,0.5, "D. 중점 개선 영역")]
AREA = [([0, 0, 2.5, 2.5], [2.5, 5, 5, 2.5]), ([2.5, 2.5, 5, 5], [2.5, 5, 5, 2.5]),
        ([0, 0, 2.5, 2.5], [0, 2.5, 2.5, 0]), ([2.5, 2.5, 5, 5], [0, 2.5, 2.5, 0])]

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(x, y)

def calc_mean_and_zip(data):
    means = np.array(list(dict(data.mean().round(2)).values()))
    result = {"만족도" : means[range(0,len(means),2)], "중요도" : means[range(1,len(means),2)]}
    return result

def on_click():
    global x, y
    p=1
    updated_y = np.cos(x - 0.05 * p)

    line1.set_xdata(x)
    line1.set_ydata(updated_y)

    figure.canvas.draw()

    figure.canvas.flush_events()
    time.sleep(0.1)

if __name__ == "__main__":
    df = pd.read_csv("../Information_Security_Level.csv")
    data = calc_mean_and_zip(df)
    print(data)

    root = Tk()
    canvas = FigureCanvasTkAgg(figure, master=root)  #
    canvas.get_tk_widget().pack()
    btn = Button(root, text = "다음", command=on_click)
    btn.pack()
    root.mainloop()