from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 프레임
frame_burger = Frame(root, relief="solid", bd=1)    # 외곽선, 굵기
frame_burger.pack(side="left", fill="both", expand=True)    # 패키징 할 때 위치 설정 가능
# 프레임 안에 버튼
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 제목 있는 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)    # 패키징 할 때 위치 설정 가능
# 프레임 안에 버튼
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()