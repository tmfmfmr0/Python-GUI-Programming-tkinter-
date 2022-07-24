from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


# 텍스트 입력 창 (여러 줄 입력)
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")    # 기본값

# 엔트리 입력 창 (한 줄 입력)
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")    # 기본값


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))    # 텍스트 가져오기 (1번째 라인, 0번째 column 위치부터) (끝까지) 모든 내용 가져오기
    print(e.get())    # 엔트리 가져오기 (그냥 기본이 한줄 전체 가져옴)

    # 내용 삭제
    txt.delete("1.0", END)    # 1,0부터 끝까지 삭제
    e.delete(0, END)    # 0부터 끝까지 삭제

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()