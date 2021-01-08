
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MyFrama02(ttk.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # グリッドを使ってレイアウト
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # ラベルとテキスト入力を作る
        label1 = ttk.Label(self,text="ユーザ名")
        # 入力した値を受け取る変数
        self.username = tk.StringVar()
        self.username_entry = ttk.Entry(
            self,
            textvariable=self.username,
            width=30)

        # ラベルとテキスト入力を作る
        label2 = ttk.Label(self,text="パスワード")
        # 入力した値を受け取る変数
        self.password = tk.StringVar()
        self.password_entry = ttk.Entry(
            self,
            textvariable=self.password,
            width=30)

        # ボタンを作る
        submit_button = ttk.Button(self,text="送信", width=20)
        exit_button = ttk.Button(self, text="アプリ終了", width=20)

        # ボタンを押された時は onSubmit()を実行
        submit_button["command"] = lambda: self.onSubmit()
        # 任意の名前の仮想イベントを作成しておく
        exit_button["command"] = lambda: self.event_generate("<<Page_Exit>>")

        # ラベルとテキスト入力を配置
        label1.grid(row=0, column=0, sticky=tk.E)
        self.username_entry.grid(row=0,column=1)
        label2.grid(row=1, column=0, sticky=tk.E)
        self.password_entry.grid(row=1,column=1)
        # ボタンを配置
        submit_button.grid(row=1, column=2, padx=5, pady=5)
        exit_button.grid(row=2, column=1, padx=5, pady=5)


    def onSubmit(self):
        # メッセージボックス表示
        messagebox.showinfo("確認",
            self.username.get()+' / '+self.password.get())
