import tkinter as tk
import tkinter.font
from tkinter import ttk
import webbrowser
import time
import threading
import pandas as pd
import pygsheets

def Thread_job(app):
    gc = pygsheets.authorize(outh_file='client_secret.json')
    print(gc)
    file_name = '정보보안솔루션(응답)'
    sh = gc.open(file_name)
    sheet1 = sh.sheet1
    data = sheet1.get_all_records()
    data_len = len(data)
    update = len(data)

    while data_len == update:
        print("진행중")
        sh = gc.open(file_name)
        sheet1 = sh.sheet1
        data = sheet1.get_all_records()
        update = len(data)
    print(data)

    app.data = data

class Main_Frame(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app
        font = tkinter.font.Font(family="메이플스토리", size=18, weight="bold")
        tk.Label(self, text="인간요인 강화 정보보안 대처 솔루션", font=font).pack()
        ttk.Button(self, text="시작하기", command=self.start_app).pack()

    def start_app(self):
        webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScqQN8bbUgk7appqGLvme7Dtk9f4lHp0B89glgDdw6i0zBstw/viewform')
        self.app.switch_frame(Progressing_Survey)

class Progressing_Survey(tk.Frame):
    def __init__(self, app):
        tk.Frame.__init__(self, app)
        self.app = app

        self.txt = ttk.Label(self, text="설문을 진행해주세요.", font=('메이플스토리',12))
        self.txt.pack()
        self.progress_var = tk.DoubleVar() #here you have ints but when calc. %'s usually floats
        self.progressbar = ttk.Progressbar(self, variable=self.progress_var, maximum=50)
        self.progressbar.pack(fill='x', expand=1)

    def progress(self):
        thr = threading.Thread(target=Thread_job, args=(self.app,))
        thr.start()

        for i in range(50):
            time.sleep(1)
            if not thr.is_alive():
                self.progress_var.set(50)
                self.progressbar.update()
                break
            self.progress_var.set(i)
            self.progressbar.update()
        thr.join()
        self.txt.config(text="완료!")
        tk.Label(self, text=str(self.app.data), font=('메이플스토리', 10)).pack()

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
        if type(self._frame) == Progressing_Survey:
            self._frame.progress()