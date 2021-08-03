import tkinter as tk
import tkinter.font
from tkinter import ttk
import tkinter.messagebox as msg
import time
import threading
import pandas as pd

import Solution
import Result

"""
Test에 사용될 설문 스크립트 각 설문에 맞게 dictionary형태로 구성함 
"""
SCRIPT = {
    'Survey1': [['나는 성과중심의 가치를 추구한다.',
                  '나는 일을 할 때, 성취 결과를 중요시한다.',
                  '나는 높은 성과를 이루는 것을 선호한다.'],
                 ['나는 인간관계중심의 가치를 추구한다.',
                  '나는 일을 할 때, 대인관계를 중요시한다.',
                  '나는 좋은 인간관계를 이루는 것을 선호한다.'],
                 ['나는 위험이 발생할 경우 안전한 선택을 우선시하는 편이다.',
                  '나는 손해가 발생하는 것을 경계한다.',
                  '나는 피해가 발생하지 않도록 우선적으로 노력한다.'],
                 ['나는 위험이 발생하더라도 이익을 높일 수 있는 선택을 우선시 하는 편이다.',
                  '나는 이익을 발생하는 것을 추구한다.',
                  '나는 성과가 발생하도록 우선적으로 노력한다.']],
    'Survey2': [['우리 조직은 성과중심의 가치를 추구한다.',
                 '우리 조직은 일을 할 때, 성취 결과를 중요시한다.',
                 '우리 조직은 높은 성과를 이루는 것을 선호한다.'],
                ['우리 조직은 인간관계중심의 가치를 추구한다.',
                 '우리 조직은 일을 할 때, 대인관계를 중요시한다.',
                 '우리 조직은 좋은 인간관계를 이루는 것을 선호한다.'],
                ['우리 조직은 위험이 발생할 경우 안전한 선택을 우선시하는 편이다.',
                 '우리 조직은 손해가 발생하는 것을 경계한다.',
                 '우리 조직은 피해가 발생하지 않도록 우선적으로 노력한다.'],
                ['우리 조직은 위험이 발생하더라도 이익을 높일 수 있는 선택을 우선시 하는 편이다.',
                 '우리 조직은 이익을 발생하는 것을 추구한다.',
                 '우리 조직은 성과가 발생하도록 우선적으로 노력한다.']],
    'Survey3': ['최고경영층 지원',
                '보안 규정(보상, 처벌 등)',
                '정보보안 목표 및 가치',
                '정보보안 시스템',
                '교육/훈련',
                '홍보 캠페인',
                '커뮤니케이션',
                '보안 문화',
                '위기 관리',
                '기술 지원(헬프데스크 등)'],
}

class Survey1(tk.Frame):
    """
    화면 2-1을 구성하는 Frame class
    개인 특성 측정을 구현
    """
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("640x580+640+150")  # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        font = tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold")

        title = ttk.Label(self, text="개인 특성 측정", font=font)
        desc1 = ttk.Label(self, text="다음은 본인 생각하는 본인의 특성을 측정하는 항목입니다.", font=('Malgun Gothic', 10))
        desc2 = ttk.Label(self, text="측정항목은 6점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다.", font=('Malgun Gothic', 10))
        desc3 = ttk.Label(self, text="1 : 매우 그렇지 않다.\n6 : 매우 그렇다.", font=('Malgun Gothic', 7))

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()
        desc3.pack(anchor="w")

        ttk.Label(self, text='--- ' * 35, font=('Malgun Gothic', 10)).pack(pady=3)
        ttk.Label(self, text="1     2     3     4     5    6").pack(anchor='e', pady=1, ipady=2.4)
        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey1']                     # 스크립트에서 설문1에 대한 내용을 받아옴
        temp_frame = tk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = tk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = tk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame
        for i in range(len(scr)):
            temp = []
            for k in range(len(scr[i])):
                ttk.Label(surv_frame, text=scr[i][k], font=('Malgun Gothic', 10)).pack(anchor='w')

                inner_frame = tk.Frame(check_frame)
                temp.append([tk.IntVar() for _ in range(6)])
                for j in range(6):
                    ttk.Checkbutton(inner_frame, variable=temp[k][j]).pack(side='left') # checkBox 생성
                inner_frame.pack(anchor='e')
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 25, font=('Malgun Gothic', 10)).pack(pady=3, anchor='w')
            ttk.Label(check_frame, text='--- ' * 10, font=('Malgun Gothic', 10)).pack(pady=3, anchor='e')
        surv_frame.pack(side='left', expand=True)
        check_frame.pack(side='right', expand=True)
        temp_frame.pack(expand=True)

        ttk.Button(self, text='check', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("individual_attribute.csv")
        data = {"date":time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        for i in range(len(self.checkvar)):
            for k in range(len(self.checkvar[i])):
                key = "Q"+str(i+1)+"-"+str(k+1)
                check = False
                for j in range(len(self.checkvar[i][k])):
                    if not check and self.checkvar[i][k][j].get() == 1:
                        check = True
                        data[key] = j+1
                    elif check and self.checkvar[i][k][j].get() == 1:
                        msg.showwarning("Message","Q%i-%i항목이 중복체크 되어있습니다."%(i+1, k+1))
                        return
                if not check:
                    msg.showwarning("Message","Q%i-%i항목을 체크해주세요."%(i+1, k+1))
                    return
        f = f.append(pd.DataFrame([data]))
        f.to_csv('individual_attribute.csv', sep=",", index=False)
        msg.showinfo("Message", "설문 내용이 정상적으로 입력되었습니다.")
        self.app.switch_frame(Survey2)

class Survey2(tk.Frame):
    """
    화면 2-2을 구성하는 Frame class
    기업 특성 측정을 구현
    """
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("640x580+640+150")  # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        font = tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold")

        title = ttk.Label(self, text="조직 특성 측정", font=font)
        desc1 = ttk.Label(self, text="다음은 본인 생각하는 우리 회사의 특성을 측정하는 항목입니다.", font=('Malgun Gothic', 10))
        desc2 = ttk.Label(self, text="측정항목은 6점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다.", font=('Malgun Gothic', 10))
        desc3 = ttk.Label(self, text="1 : 매우 그렇지 않다.\n6 : 매우 그렇다.", font=('Malgun Gothic', 7))

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()
        desc3.pack(anchor="w")

        ttk.Label(self, text='--- ' * 35, font=('Malgun Gothic', 10)).pack(pady=3)
        ttk.Label(self, text="1     2     3     4     5    6").pack(anchor='e', pady=1, ipady=2.4)
        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey2']                     # 스크립트에서 설문1에 대한 내용을 받아옴
        temp_frame = tk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = tk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = tk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame
        for i in range(len(scr)):
            temp = []
            for k in range(len(scr[i])):
                ttk.Label(surv_frame, text=scr[i][k], font=('Malgun Gothic', 10)).pack(anchor='w')

                inner_frame = tk.Frame(check_frame)
                temp.append([tk.IntVar() for _ in range(6)])
                for j in range(6):
                    ttk.Checkbutton(inner_frame, variable=temp[k][j]).pack(side='left') # checkBox 생성
                inner_frame.pack(anchor='e')
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 25, font=('Malgun Gothic', 10)).pack(pady=3, anchor='w')
            ttk.Label(check_frame, text='--- ' * 10, font=('Malgun Gothic', 10)).pack(pady=3, anchor='e')
        surv_frame.pack(side='left', expand=True)
        check_frame.pack(side='right', expand=True)
        temp_frame.pack(expand=True)

        ttk.Button(self, text='check', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("cultural_attribute.csv")
        data = {"date":time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        for i in range(len(self.checkvar)):
            for k in range(len(self.checkvar[i])):
                key = "Q"+str(i+1)+"-"+str(k+1)
                check = False
                for j in range(len(self.checkvar[i][k])):
                    if not check and self.checkvar[i][k][j].get() == 1:
                        check = True
                        data[key] = j+1
                    elif check and self.checkvar[i][k][j].get() == 1:
                        msg.showwarning("Message","Q%i-%i항목이 중복체크 되어있습니다."%(i+1, k+1))
                        return
                if not check:
                    msg.showwarning("Message","Q%i-%i항목을 체크해주세요."%(i+1, k+1))
                    return
        f = f.append(pd.DataFrame([data]))
        f.to_csv("cultural_attribute.csv", sep=",", index=False)
        msg.showinfo("Message", "설문 내용이 정상적으로 입력되었습니다.")
        self.app.switch_frame(Survey3)

class Survey3(tk.Frame):
    """
    화면 2-3을 구성하는 Frame class
    정보보안 수준 측정을 구현
    """
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("640x640+640+150")  # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        font = tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold")

        title = ttk.Label(self, text="정보보안 수준 측정", font=font)
        desc1 = ttk.Label(self, text="다음은 본인 생각하는 우리 회사의 정보보안 수준을 측정하는 항목입니다.", font=('Malgun Gothic', 10))
        desc2 = ttk.Label(self, text="측정항목은 5점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다.", font=('Malgun Gothic', 10))
        desc3 = ttk.Label(self, text="1 : 매우 불만족/매우 사소.\n5 : 매우 만족/매우 중요.", font=('Malgun Gothic', 7))

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()
        desc3.pack(anchor="w")

        ttk.Label(self, text='--- ' * 35, font=('Malgun Gothic', 10)).pack(pady=3)
        ttk.Label(self, text="만족도\t\t\t중요도           ").pack(anchor='e')
        ttk.Label(self, text="1     2     3     4     5\t1     2     3     4     5").pack(anchor='e', ipady=2.4)
        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey3']                     # 스크립트에서 설문1에 대한 내용을 받아옴
        temp_frame = tk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = tk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = tk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame
        for i in range(len(scr)):
            temp = []
            ttk.Label(surv_frame, text=scr[i], font=('Malgun Gothic', 10)).pack(anchor='e')

            inner_frame = tk.Frame(check_frame)
            temp.append([tk.IntVar() for _ in range(5)])
            for j in range(5):
                ttk.Checkbutton(inner_frame, variable=temp[0][j]).pack(side='left') # 만족도 checkBox 생성

            ttk.Label(inner_frame, text="            ").pack(side='left')

            temp.append([tk.IntVar() for _ in range(5)])
            for j in range(5):
                ttk.Checkbutton(inner_frame, variable=temp[1][j]).pack(side='left') # 중요도 checkBox 생성
            inner_frame.pack(anchor='e')
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 15, font=('Malgun Gothic', 9)).pack(anchor='w')
            ttk.Label(check_frame, text='--- ' * 25, font=('Malgun Gothic', 9)).pack(anchor='e')
        surv_frame.pack(side='left', expand=True)
        check_frame.pack(side='right', expand=True)
        temp_frame.pack(expand=True)

        ttk.Button(self, text='check', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("Information_Security_Level.csv")
        data = {"date":time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        for i in range(len(self.checkvar)):
            for k in range(len(self.checkvar[i])):
                key = "Q"+str(i+1)+"-"+str(k+1)
                check = False
                for j in range(len(self.checkvar[i][k])):
                    if not check and self.checkvar[i][k][j].get() == 1:
                        check = True
                        data[key] = j+1
                    elif check and self.checkvar[i][k][j].get() == 1:
                        msg.showwarning("Message","Q%i-%i항목이 중복체크 되어있습니다."%(i+1, k+1))
                        return
                if not check:
                    msg.showwarning("Message","Q%i-%i항목을 체크해주세요."%(i+1, k+1))
                    return
        f = f.append(pd.DataFrame([data]))
        f.to_csv("Information_Security_Level.csv", sep=",", index=False)
        msg.showinfo("Message", "설문 내용이 정상적으로 입력되었습니다.")
        self.app.switch_frame(Result.Result1)