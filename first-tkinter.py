import tkinter


root = tkinter.Tk()
root.title("タイトル")
root.geometry("400x300")
text = tkinter.Label(text='テキストを表示')
text.pack()

root.mainloop()