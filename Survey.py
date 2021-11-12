import tkinter as tk
import tkinter.font
from tkinter import ttk
import tkinter.messagebox as msg
import time
import pandas as pd

import Solution

"""
사용되는 설문 스크립트 각 화면에 맞게 dictionary형태로 구성함 
"""
SCRIPT = {
    'Survey1_Title' : ["다음은 본인 생각하는 본인의 특성을 측정하는 항목입니다.",
                       "측정항목은 6점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다."],
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
    'Survey2_Title' : ["다음은 본인 생각하는 우리 회사의 특성을 측정하는 항목입니다.",
                       "측정항목은 6점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다."],
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
    'Survey3_Title' : ["다음은 본인 생각하는 우리 회사의 정보보안 수준을 측정하는 항목입니다.",
                       "측정항목은 5점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다."],
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

class Survey(ttk.Frame):
    """
    모든 Survey Frame에 뼈대가 되는 Super class
    """
    def __init__(self, app):
        ttk.Frame.__init__(self, app)
        self.app = app

class Survey1(Survey):
    """
    화면 2-1을 구성하는 Frame class
    개인 특성 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        Survey.__init__(self, app)
        # self.app = app

        title = ttk.Label(self, text="개인 특성 측정", font=self.app.font["title"])
        desc1 = ttk.Label(self, text=SCRIPT['Survey1_Title'][0], font=self.app.font["sub_title"])
        desc2 = ttk.Label(self, text=SCRIPT['Survey1_Title'][1], font=self.app.font["sub_title"])

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()

        ttk.Label(self, text='--- ' * 50, font=self.app.font["etc"]).pack(pady=3)
        ttk.Label(self, text="1 : 매우 그렇지 않다.\t~\t6 : 매우 그렇다.\t       ", font=self.app.font["etc"]).pack(anchor='e')
        ttk.Label(self, text="1       2       3       4       5       6\t     ").pack(anchor='e', pady=1, ipady=2.4)

        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey1']                     # 스크립트에서 설문1에 대한 내용을 받아옴
        temp_frame = ttk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = ttk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = ttk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame

        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###
        for i in range(len(scr)):
            temp = []
            for k in range(len(scr[i])):
                ttk.Label(surv_frame, text="\tQ{}-{}. ".format(i+1, k+1)+scr[i][k],
                          font=self.app.font["contents1"]).pack(anchor='w')

                inner_frame = ttk.Frame(check_frame)
                temp.append([tk.IntVar() for _ in range(6)])
                for j in range(6):
                    ttk.Checkbutton(inner_frame, variable=temp[k][j]).pack(padx=5, side='left') # checkBox 생성
                inner_frame.pack()
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 30, font=self.app.font["contents1"]).pack(pady=3, anchor='e')
            ttk.Label(check_frame, text='--- ' * 15, font=self.app.font["contents1"]).pack(pady=3, anchor='w')
        surv_frame.pack(side='left', expand=True, fill="both")
        check_frame.pack(side='right', expand=True, fill="both")
        temp_frame.pack(expand=True, fill="both")

        ttk.Button(self, text='다음', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("individual_attribute.csv") # 파일을 읽어옴
        data = {"g_id" : self.app.groupID, "u_id" : self.app.userID,
               "date":time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
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
        self.app.switch_frame(Survey2) # 이후 다음 설문문항으로 넘김(switch_frame)

class Survey2(Survey):
    """
    화면 2-2을 구성하는 Frame class
    기업 특성 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        Survey.__init__(self, app)

        title = ttk.Label(self, text="조직 특성 측정", font=self.app.font["title"])
        desc1 = ttk.Label(self, text=SCRIPT['Survey2_Title'][0], font=self.app.font["sub_title"])
        desc2 = ttk.Label(self, text=SCRIPT['Survey2_Title'][1], font=self.app.font["sub_title"])

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()

        ttk.Label(self, text='--- ' * 50, font=self.app.font["etc"]).pack(pady=3)
        ttk.Label(self, text="1 : 매우 그렇지 않다.\t~\t6 : 매우 그렇다.\t       ", font=self.app.font["etc"]).pack(anchor='e')
        ttk.Label(self, text="1       2       3       4       5       6\t     ").pack(anchor='e', pady=1, ipady=2.4)

        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey2']                     # 스크립트에서 설문2에 대한 내용을 받아옴
        temp_frame = tk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = tk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = tk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame

        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###
        for i in range(len(scr)):
            temp = []
            for k in range(len(scr[i])):
                ttk.Label(surv_frame, text="\tQ{}-{}. ".format(i+1, k+1)+scr[i][k],
                          font=self.app.font["contents1"]).pack(anchor='w')

                inner_frame = ttk.Frame(check_frame)
                temp.append([tk.IntVar() for _ in range(6)])
                for j in range(6):
                    ttk.Checkbutton(inner_frame, variable=temp[k][j]).pack(padx=5, side='left') # checkBox 생성
                inner_frame.pack()
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 30, font=self.app.font["contents1"]).pack(pady=3, anchor='e')
            ttk.Label(check_frame, text='--- ' * 15, font=self.app.font["contents1"]).pack(pady=3, anchor='w')
        surv_frame.pack(side='left', expand=True, fill="both")
        check_frame.pack(side='right', expand=True, fill="both")
        temp_frame.pack(expand=True, fill="both")

        ttk.Button(self, text='다음', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("cultural_attribute.csv") # 파일을 읽어옴
        data = {"g_id": self.app.groupID, "u_id": self.app.userID,
                "date": time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
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
        self.app.switch_frame(Survey3) # 이후 다음 설문문항으로 넘김(switch_frame)

class Survey3(Survey):
    """
    화면 2-3을 구성하는 Frame class
    정보보안 수준 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        Survey.__init__(self, app)
        # self.app = app

        title = ttk.Label(self, text="정보보안 수준 측정", font=self.app.font["title"])
        desc1 = ttk.Label(self, text=SCRIPT["Survey3_Title"][0], font=self.app.font["sub_title"])
        desc2 = ttk.Label(self, text=SCRIPT["Survey3_Title"][1], font=self.app.font["sub_title"])

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()

        ttk.Label(self, text='--- ' * 50, font=self.app.font["etc"]).pack(pady=3)
        ttk.Label(self, text="만족도                                     중요도              ").pack(anchor='e')
        ttk.Label(self, text="매우 불만족  ~  매우 만족                            매우 사소  ~  매우 중요        ",
                  font=self.app.font["etc"]).pack(anchor="e")
        ttk.Label(self, text="1     2     3     4     5     \t     1     2     3     4     5   ").pack(anchor='e', ipady=2.4)

        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        scr = SCRIPT['Survey3']                     # 스크립트에서 설문3에 대한 내용을 받아옴
        temp_frame = tk.Frame(self)                 # 각 설문요인을 담는 frame
        surv_frame = tk.Frame(temp_frame)           # 각각의 설문 내용을 담는 frame
        check_frame = tk.Frame(temp_frame)          # 각 설문에 대한 checkbox를 담는 frame

        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###
        for i in range(len(scr)):
            temp = []
            ttk.Label(surv_frame, text=scr[i], font=self.app.font["contents1"]).pack(anchor='e')

            inner_frame = tk.Frame(check_frame)
            temp.append([tk.IntVar() for _ in range(5)])
            for j in range(5):
                ttk.Checkbutton(inner_frame, variable=temp[0][j]).pack(side='left', padx=1.5) # 만족도 checkBox 생성

            ttk.Label(inner_frame, text="            ").pack(side='left')

            temp.append([tk.IntVar() for _ in range(5)])
            for j in range(5):
                ttk.Checkbutton(inner_frame, variable=temp[1][j]).pack(side='left', padx=1.5) # 중요도 checkBox 생성
            inner_frame.pack(anchor='e')
            self.checkvar.append(temp)  # checkvar 갱신
            ttk.Label(surv_frame, text='--- ' * 15, font=self.app.font["contents1"]).pack(anchor='e')
            ttk.Label(check_frame, text='--- ' * 25, font=self.app.font["contents1"]).pack(anchor='w')
        surv_frame.pack(side='left', expand=True, fill="both")
        check_frame.pack(side='right', expand=True, fill="both")
        temp_frame.pack(expand=True, fill="both")

        ttk.Button(self, text='설문종료', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        f = pd.read_csv("Information_Security_Level.csv") # 파일을 읽어옴
        data = {"g_id": self.app.groupID, "u_id": self.app.userID,
                "date": time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
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
        self.app.switch_frame(Solution.Main_Frame) # 이후 다음 설문문항으로 넘김(switch_frame)

if __name__ == "__main__":
    window = tk.Tk()
    window.font = {
        "title": tkinter.font.Font(family="Malgun Gothic", size=32, weight="bold"),
        "sub_title": tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold"),
        "contents1": tkinter.font.Font(family="Malgun Gothic", size=10, weight="bold"),
        "contents2": tkinter.font.Font(family="Malgun Gothic", size=12),
        "contents3": tkinter.font.Font(family="Malgun Gothic", size=12, weight="bold"),
        "widget": tkinter.font.Font(family="Malgun Gothic", size=10),
        "etc": tkinter.font.Font(family="Malgun Gothic", size=7)
    }
    window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))  # 크기 (가로x세로)
    s3 = Survey3(window)
    s3.pack()

    window.mainloop()