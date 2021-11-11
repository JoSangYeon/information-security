import tkinter as tk
import tkinter.font
from tkinter import ttk
import tkinter.messagebox as msg

import Survey
import Result

class Project(tk.Tk):
    """
    전체 소스코드를 관장하는 Project class
    tkinter 패키지의 TK() 객체를 상속하여 만든 클래스
    """
    def __init__(self):
        tk.Tk.__init__(self)

        self.groupID = ""   # 집단명을 저장하는 변수
        self.userID = ""   # 개인ID을 저장하는 변수
        self.myWidth = self.winfo_screenwidth()     # 모니터별 너비 픽셀
        self.myHeight = self.winfo_screenheight()   # 모니터별 높이 픽셀
        self.font = {
            "title" : tkinter.font.Font(family="Malgun Gothic", size=32, weight="bold"),
            "sub_title" : tkinter.font.Font(family="Malgun Gothic", size=16),
            "contents" : tkinter.font.Font(family="Malgun Gothic", size=10, weight="bold"),
            "widget" : tkinter.font.Font(family="Malgun Gothic", size=10),
            "etc" : tkinter.font.Font(family="Malgun Gothic", size=7)
            }

        self.title("정보보안 솔루션") # 제목 설정
        self.geometry("{}x{}".format(self.myWidth, self.myHeight))  # 크기 (가로x세로)
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

class Main_Frame(ttk.Frame):
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
        ttk.Frame.__init__(self, app)
        self.app = app

        """각종 Widget 선언 부분"""
        ttk.Label(self, text="인간요인 강화 정보보안 대처 솔루션", font=self.app.font["title"]).pack()

        userInfo_Frame = ttk.Frame(self)

        group_Frame = ttk.Frame(userInfo_Frame)
        groupID_L = ttk.Label(group_Frame, text="Group ID : ",font=self.app.font["widget"])
        self.groupID_E = ttk.Entry(group_Frame, width=15)

        user_Frame = ttk.Frame(userInfo_Frame)
        userID_L = ttk.Label(user_Frame, text="User ID : ",font=self.app.font["widget"])
        self.userID_E = ttk.Entry(user_Frame, width=15)

        groupID_L.pack(side="left", anchor = "w")
        self.groupID_E.pack(side="right", anchor = "e")
        userID_L.pack(side="left", anchor = "w")
        self.userID_E.pack(side="right", anchor = "e")

        group_Frame.pack(fill="both")
        user_Frame.pack(fill="both")

        userInfo_Frame.pack()
        ttk.Button(self, text="시작하기", command=self.start_app).pack()
        ttk.Button(self, text="결과보기", command=self.start_result).pack()
        ttk.Button(self, text="종료하기", command=self.app.quit).pack()

    def start_app(self):
        """
        버튼을 클릭하면, 다음화면(Frame(화면 2-1))으로 switching하는 메소드
        :return:
        """
        self.app.groupID = self.groupID_E.get()
        self.app.userID = self.userID_E.get()

        if self.app.groupID == "":
            msg.showwarning("Message", "Group ID를 입력해주세요")
            return
        elif self.app.userID == "":
            msg.showwarning("Message", "User ID를 입력해주세요")
            return
        else:
            # print("group ID : {}\nuser ID : {}".format(self.app.groupID, self.app.userID))
            self.app.switch_frame(Survey.Survey1)

    def start_result(self):
        """
        버튼을 클릭하면, 결과화면(Frame(화면 3-1))으로 switching하는 메소드
        :return:
        """
        self.app.groupID = self.groupID_E.get()
        self.app.userID = self.userID_E.get()

        if self.app.groupID == "":
            msg.showwarning("Message", "Group ID를 입력해주세요")
            return
        elif self.app.userID == "":
            msg.showwarning("Message", "User ID를 입력해주세요")
            return
        else:
            print("group ID : {}\nuser ID : {}".format(self.app.groupID, self.app.userID))
            self.app.switch_frame(Result.Result1)