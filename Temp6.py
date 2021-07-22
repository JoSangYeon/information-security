from tkinter import * #티킨터 모듈에 있는 함수를 사용

"""기본 프레임 설정"""
root = Tk() # tk창 생성
root.title("JSY GUI") # 제목 설정
root.geometry("640x480")

f1 = Frame(root)
f2 = Frame(root)

btn1 = Button(f1, text="Left1")
btn1.pack(anchor='w')
btn2 = Button(f1, text="Left2")
btn2.pack(anchor='w')
btn5 = Button(f1, text="qqqqqqqqqqqqqqqqqqqqqqq\n1")
btn5.pack(anchor='w')

btn3 = Button(f2, text="Right1")
btn3.pack(anchor='e')
btn4 = Button(f2, text="Right2")
btn4.pack(anchor='e')
btn6 = Button(f2, text="Right2")
btn6.pack(anchor='e')

f1.pack(side='left')
f2.pack(side='right')

root.mainloop()
