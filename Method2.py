"""
"""
import tkinter as tk
import tkinter.font
from tkinter import ttk
import time
import threading
import pandas as pd

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
                '보안 문화',
                '위기 관리',
                '기술 지원(헬프데스크 등)'],
}

class Main_Frame(tk.Frame):
    """
    화면 1-1를 구성하는 Frame class
    2021.07.19 - 추후에 화면구성에 조금더 신경을 쓸 예정 당장은 기능 구현에 힘을 쓰겠다.
    """
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        font = tkinter.font.Font(family="나눔고딕", size=18, weight="bold")
        tk.Label(self, text="인간요인 강화 정보보안 대처 솔루션", font=font).pack()
        ttk.Button(self, text="시작하기", command=self.start_app).pack()

    def start_app(self):
        """
        버튼을 클릭하면, 다음화면(Frame(화면 2-1))으로 switching하는 메소드
        :return:
        """
        self.app.switch_frame(Survey1)

class Survey1(tk.Frame):
    """
    화면 2-1을 구성하는 Frame class
    개인 특성 측정을 구현
    2021.07.19 - 현재 뼈대 정도만 구현 세부 기능은 추후에 설계
    """
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        font = tkinter.font.Font(family="나눔고딕", size=14, weight="bold")

        title = ttk.Label(self, text="개인 특성 측정", font=font)
        desc1 = ttk.Label(self, text="다음은 본인 생각하는 본인의 특성을 측정하는 항목입니다.", font=('나눔고딕', 10))
        desc2 = ttk.Label(self, text="측정항목은 6점 척도로 구성되어 있으며, 해당되는 부분에 체크해주시기 바랍니다.", font=('나눔고딕', 10))

        title.pack(pady=5)
        desc1.pack()
        desc2.pack()

        self.checkvar = []                          # checkBox의 check여부를 저장하는 변수를 담는 list
        ttk.Label(self, text='--- '*25, font=('나눔고딕', 10)).pack(pady=3)
        scr = SCRIPT['Survey1']                     # 스크립트에서 설문1에 대한 내용을 받아옴
        for i in range(len(scr)):
            temp = []
            for k in range(len(scr[i])):
                temp_frame = tk.Frame(self)         # 각 설문요인을 담는 frame

                surv_frame = tk.Frame(temp_frame)   # 각각의 설문 내용을 담는 frame
                ttk.Label(surv_frame, text=scr[i][k], font=('나눔고딕', 10)).pack()
                surv_frame.pack(side='left', expand=True)

                check_frame = tk.Frame(temp_frame)  # 각 설문에 대한 checkbox를 담는 frame
                temp.append([tk.IntVar() for _ in range(6)])
                for j in range(6):
                    ttk.Checkbutton(check_frame, variable=temp[k][j]).pack(side='left') # checkBox 생성
                check_frame.pack(side='right', expand=True)

                temp_frame.pack(anchor='e')
            self.checkvar.append(temp)              # checkvar 갱신
            ttk.Label(self, text='--- '*25,font=('나눔고딕', 10)).pack(pady=3)

        ttk.Button(self, text='check', command=self.check).pack()

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        2021.07.19 - 현재는 중복기능 없이 구현 추후에 구현할 예정 
        """
        for i in range(len(self.checkvar)):
            for k in range(len(self.checkvar[i])):
                for j in range(len(self.checkvar[i][k])):
                    print(self.checkvar[i][k][j].get(), end=" ")
                print()
            print("--- - - - ---")

class Project(tk.Tk):
    def __init__(self):
        self.data = None
        tk.Tk.__init__(self)
        self.title("정보보안 솔루션") # 제목 설정
        self.geometry("640x480+640+300") # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        self.resizable(False, False) #창 크기 변경 (너비, 높이)
        self._frame = None
        self.switch_frame(Main_Frame)

    def switch_frame(self, frame_class):
        """
        frame간 전환
        :param frame_class: 스위치할 frame class명을 입력
        """
        new_frame = frame_class(self)   #매개변수로 받은 frame을 생성
        if self._frame is not None:     #기존에 있던 frame 삭제
            self._frame.destroy()
        self._frame = new_frame         # 새로운 프레임 적용
        self._frame.pack()              # pack()을 통한 배치