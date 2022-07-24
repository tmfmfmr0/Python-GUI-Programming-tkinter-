from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+500+200") # 가로 * 세로 + x좌표 + y좌표

root.resizable(True, True) # 창 크기 x, y 값 변경 여부

root.mainloop()