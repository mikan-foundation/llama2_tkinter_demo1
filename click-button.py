import tkinter

def on_button_click():
    text.config(text="ボタンが押されました")

root = tkinter.Tk()
root.title("タイトル")
root.geometry("400x300")

text = tkinter.Label(text='テキストを表示')
text.pack()

textbox = tkinter.Entry(width=20)
textbox.pack()

button = tkinter.Button(text="ボタン",command=on_button_click)
button.pack()

root.mainloop()