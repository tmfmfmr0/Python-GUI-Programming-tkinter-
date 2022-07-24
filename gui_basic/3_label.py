from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


# 라벨은 그냥 글자나 이미지만 보여줌 (동작 없음)
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()


# 버튼 
def change():
    label1.config(text="또 만나요")    # config(속성=) 으로 속성값 변경

    global photo2    # 전역변수로 안만들면 garbage collection이 진행돼서 지움
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)    # config(속성=) 으로 속성값 변경

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()