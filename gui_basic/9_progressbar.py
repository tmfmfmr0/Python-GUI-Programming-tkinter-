import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")    # 언제 끝날지 결정되지 않음
progressbar.start(10)    # 10 ms 마다 움직임
progressbar.pack()

progressbar1 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar1.start(10)
progressbar1.pack()

def btncmd():
    progressbar1.stop() # 작동 중지
btn = Button(root, text="중지", command=btncmd)
btn.pack()


p_var2 = DoubleVar()    # 실수도 반영
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()