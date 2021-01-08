
import tkinter as tk
from tkinter import ttk


class MyFrama01(ttk.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # グリッドを使ってレイアウト
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.grid_columnconfigure(0, weight=1)

        # ボタンを4つ作る
        button01 = ttk.Button(self, text="テキスト入力", width=30)
        button02 = ttk.Button(self, text="日付と時刻",    width=30)
        button03 = ttk.Button(self, text="予約一覧",    width=30)
        exit_button = ttk.Button(self, text="アプリ終了", width=30)

        # 任意の名前の仮想イベントを作成しておく
        button01["command"] = lambda: self.event_generate("<<Page_Menu>>")
        button02["command"] = lambda: self.event_generate("<<Page_Customer>>")
        button03["command"] = lambda: self.event_generate("<<Page_Reservation>>")
        exit_button["command"] = lambda: self.event_generate("<<Page_Exit>>")

        # Labelを作成して 0行目、0列目 (2列分の大きさ)
        tk.Label(self, text="メニューのページ", font=("", 20)).grid(row=0, column=0, sticky=tk.N)
        # ボタンを配置 1行目、0列目、1列目、2列目
        button01.grid(row=1, column=0, pady=5)
        button02.grid(row=2, column=0, pady=5)
        button03.grid(row=3, column=0, pady=5)
        exit_button.grid(row=4, column=0, pady=5)