
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MyFrama04(ttk.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # グリッドを使ってレイアウト
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # 下地のframe: frBoxを作る
        self.frBox1 = tk.Frame(self)
        # ラベルを作る
        label1 = ttk.Label(self.frBox1,text="日付 ",width=8)
        # ListBoxを作る
        currencies1 = ['Japan', 'Jamaica','Korea','India','England' ]
        v1 = tk.StringVar(value=currencies1)
        listBox1 = tk.Listbox(self.frBox1,
                             listvariable=v1,
                             selectmode='single',
                             height=4)

        # 下地のframeにcalendarを載せる
        label1.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        listBox1.pack(side=tk.LEFT, fill=tk.BOTH)


        # 下地のframe: frBoxを作る
        self.frBox2 = tk.Frame(self)

        # TimePickerを作る (スピンボックス×２)
        # ラベルを作る
        label2 = ttk.Label(self.frBox2,text="時刻 ",width=8)
        # ListBoxを作る
        currencies2 = ['日本', 'ジャマイカ','韓国','インド','イングランド' ]
        v2 = tk.StringVar(value=currencies2)
        listBox2 = tk.Listbox(self.frBox2,
                             listvariable=v2,
                             selectmode='single',
                             height=4)

        # 下地のframeにTimePickerを載せる
        label2.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        listBox2.pack(side=tk.LEFT, fill=tk.BOTH)

        # ラベルとテキスト入力を作る
        # ボタンを作る
        submit_button = ttk.Button(self,text="送信", width=20)
        back_button = ttk.Button(self,text="戻る", width=20)
        exit_button = ttk.Button(self, text="アプリ終了", width=20)

        # ボタンを押された時は onSubmit()を実行
        submit_button["command"] = lambda: self.onSubmit()
        # 任意の名前の仮想イベントを作成しておく
        back_button["command"] = lambda: self.event_generate("<<Page_Back>>")
        exit_button["command"] = lambda: self.event_generate("<<Page_Exit>>")

        # ボタンを配置
        self.frBox1.grid(row=0,column=0, padx=5, pady=5)
        self.frBox2.grid(row=1,column=0, padx=5, pady=5)
        submit_button.grid(row=1, column=1, padx=5, pady=5)
        back_button.grid(row=2, column=1, padx=5, pady=5)
        exit_button.grid(row=3, column=1, padx=5, pady=5)


    def onSubmit(self):
        str = 'Confirm'
        # メッセージボックス表示
        messagebox.showinfo("確認", str)
