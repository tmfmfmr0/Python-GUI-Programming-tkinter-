from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")    # 스크롤 바 높이만큼 채우기

listbox = Listbox(frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)    # 리스트박스에 스크롤바 연결. yscrollcommand 필수. set 없으면 스크롤을 내려도 다시 올라옴
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)    # 스크롤바에 리스트박스 연결

root.mainloop()