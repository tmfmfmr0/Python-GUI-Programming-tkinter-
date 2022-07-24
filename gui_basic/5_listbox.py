from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


# 리스트박스
listbox = Listbox(root, selectmode="extended", height=0)    # selectmode (single extended여러 개 선택 가능), height (한번에 보여줄 목록 수)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    #listbox.delete(END) # 맨 뒤 항목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (인덱스 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()