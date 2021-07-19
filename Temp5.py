from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""체크 박스"""
# variable: 체크박스의 상태를 저장할 변수를 설정해야함
checkvar = IntVar() #checkvar에 int형으로 값을 저장한다.
checkBox = Checkbutton(root, text="오늘 하루 보지 않기", variable=checkvar)

# checkBox.select() # 선택처리
# checkBox.deselect() # 선택해제 처리
checkBox.pack()

checkvar2 = IntVar()
checkBox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable=checkvar2)
checkBox2.pack()


"""체크 박스 응용"""
def btncmd():
    print(checkvar.get()) # 0: 체크해제, 1:체크됨
    print(checkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 하는 명령어



"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

"""
스크롤 바
"""
frame = Frame(root)
frame.pack()

# 스크롤바를 생성하고 frame의 왼쪽에 채움
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 리스트 박스에 yscrollcommand=scrollbar.set속성을 선언함으로 리스트박스에 스크롤바가 매핑됨
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32): # 1~31일
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

# 스크롤바에도 리스트박스를 매핑함
scrollbar.config(command=listbox.yview)

"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어


"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

#햄버거 frame#
frame_burger = Frame(root, relief="groove", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈햄버거").pack()
Button(frame_burger, text="치킨햄버거").pack()

#음료 frame#
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이드").pack()

"""화면 출력"""
root.mainloop() #창이 닫히지 않도록 하는 명령어