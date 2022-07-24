from tkinter import *

root = Tk()
root.title("Nado GUI")

# 기본 버튼
btn1 = Button(root, text="버튼1")   # root 윈도우에 '버튼1'
btn1.pack()                         # 버튼 생성

# 버튼 패딩 비교
btn2 = Button(root, padx=0, pady=20, text="버튼2")
btn2.pack()
btn3 = Button(root, padx=20, pady=0, text="버튼3")
btn3.pack()

# 버튼 크기 (width, height) 딱 정하기
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# foreground 글자색, background 배경색
btn5 = Button(root, fg="purple", bg="skyblue", text="버튼5")
btn5.pack()

# 이미지 버튼
photo = PhotoImage(file="gui_basic/img.png")    # 이미지 불러와서 객체로 저장
btn6 = Button(root, image=photo)    
btn6.pack()

# 이미지 버튼
btn6 = Button(root, image=photo, text="버튼6")    
btn6.pack()

# 버튼 동작 함수
def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)    # 버튼 클릭 시 커맨드에 해당하는 함수 실행
btn7.pack()

root.mainloop()