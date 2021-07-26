import tkinter as tk
import tkinter.font
from tkinter import ttk
import tkinter.messagebox as msg
import time
import threading
import pandas as pd
import Survey

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
        self.app.switch_frame(Survey.Survey1)

class Project(tk.Tk):
    def __init__(self):
        self.data = None
        tk.Tk.__init__(self)
        self.title("정보보안 솔루션") # 제목 설정
        self.geometry("640x560+640+200") # 크기/위치 설정 (가로*세로+x좌표+y좌료)
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