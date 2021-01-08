
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class MyFrama03(ttk.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # グリッドを使ってレイアウト
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # 下地のframe: frBoxを作る
        self.frBox1 = tk.Frame(self)
        # ラベルを作る
        label1 = ttk.Label(self.frBox1,text="日付 ",width=8)
        # 日付ピッカーを作る
        self.calendar = DateEntry(self.frBox1, locale='ja_JP.UTF-8', date_pattern='y/mm/dd', width=14)

        # 下地のframeにcalendarを載せる
        label1.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        self.calendar.pack(side=tk.LEFT, fill=tk.BOTH)

        # 下地のframe: frBoxを作る
        self.frBox2 = tk.Frame(self)

        # TimePickerを作る (スピンボックス×２)
        # ラベルを作る
        label2 = ttk.Label(self.frBox2,text="時刻 ",width=8)
        # スピンボックス (時)
        self.hour = tk.StringVar()
        self.hour.set('12')
        self.hour_spinEntry = ttk.Spinbox(
            self.frBox2,
            format='%02.0f',
            state='readonly',
            textvariable=self.hour,
            from_=0,
            to=23,
            increment=1.0,
            width=6,
            command=lambda: print(self.hour.get()))

        # スピンボックス (分)
        self.minute = tk.StringVar()
        self.minute.set('00')
        self.minute_spinEntry = ttk.Spinbox(
            self.frBox2,
            format='%02.0f',
            state='readonly',
            textvariable=self.minute,
            from_=0,
            to=59,
            increment=1.0,
            width=6,
            command=lambda: print(self.minute.get()))

        # 下地のframeにTimePickerを載せる
        label2.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        self.hour_spinEntry.pack(anchor=tk.W,side=tk.LEFT, fill=tk.BOTH)
        self.minute_spinEntry.pack(anchor=tk.W,side=tk.LEFT, fill=tk.BOTH)

        # ラベルとテキスト入力を作る
        # ボタンを作る
        submit_button = ttk.Button(self,text="送信", width=20)
        exit_button = ttk.Button(self, text="アプリ終了", width=20)

        # ボタンを押された時は onSubmit()を実行
        submit_button["command"] = lambda: self.onSubmit()
        # 任意の名前の仮想イベントを作成しておく
        exit_button["command"] = lambda: self.event_generate("<<Page_Exit>>")

        # ボタンを配置
        self.frBox1.grid(row=0,column=0, padx=5, pady=5)
        self.frBox2.grid(row=1,column=0, padx=5, pady=5)
        submit_button.grid(row=1, column=1, padx=5, pady=5)
        exit_button.grid(row=2, column=1, padx=5, pady=5)


    def onSubmit(self):
        dt=self.calendar.get_date()
        tstr = dt.strftime('%Y/%m/%d')
        hh = self.hour.get()
        mm = self.minute.get()
        str = tstr + ' ' + hh + ':' + mm
        # メッセージボックス表示
        messagebox.showinfo("確認", str)
