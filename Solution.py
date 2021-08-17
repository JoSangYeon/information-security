import tkinter as tk
import tkinter.font
from tkinter import ttk

import Survey
import Result

class Project(tk.Tk):
    """
    전체 소스코드를 관장하는 Project class
    tkinter 패키지의 TK() 객체를 상속하여 만든 클래스
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("정보보안 솔루션") # 제목 설정
        self.resizable(False, False) #창 크기 변경 (너비, 높이)
        self._frame = None
        self.switch_frame(Main_Frame)

    def switch_frame(self, frame_class):
        """
        frame간 전환을 구현한 메소드
        :param frame_class: 스위치할 frame class명을 입력
        """
        new_frame = frame_class(self)   # 매개변수로 받은 frame 객체를 생성
        if self._frame is not None:     # 기존에 있던 frame 삭제
            self._frame.destroy()
        self._frame = new_frame         # 새로운 프레임 적용
        self._frame.pack()              # pack()을 통한 배치

class Main_Frame(tk.Frame):
    """
    화면 1-1를 구성하는 Frame class
    버튼은 총 3개로
    시작하기
    결과확인
    종료하기 이다.
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("400x200+640+150")  # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        font = tkinter.font.Font(family="Malgun Gothic", size=16, weight="bold")
        ttk.Label(self, text="인간요인 강화 정보보안 대처 솔루션", font=font).pack()
        ttk.Button(self, text="시작하기", command=self.start_app).pack()
        ttk.Button(self, text="결과보기", command=self.start_result).pack()
        ttk.Button(self, text="종료하기", command=self.app.quit).pack()

    def start_app(self):
        """
        버튼을 클릭하면, 다음화면(Frame(화면 2-1))으로 switching하는 메소드
        :return:
        """
        self.app.switch_frame(Survey.Survey1)

    def start_result(self):
        """
        버튼을 클릭하면, 결과화면(Frame(화면 3-1))으로 switching하는 메소드
        :return:
        """
        self.app.switch_frame(Result.Result1)