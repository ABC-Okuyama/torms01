from MyDB import MyDB
import tkinter as tk
from tkinter import ttk


class OrderMenuList(ttk.Frame):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        # Load Data from Database
        self.results = self.load_Kind()

        # Buttonを作る
        back_button = ttk.Button(self, text="メニューに戻る")
        # 任意の名前の仮想イベントを作成しておく
        back_button["command"] = lambda: self.event_generate("<<Page_Back>>")

        # 下地のframe: frBoxを作る
        self.frBox = tk.Frame(self)

        # 下地のfrBoxにcomboBoxをセットアップする
        self.setup_kindComboBox()

        # Frameを配置
        self.frBox.pack()
        # Buttonを配置
        back_button.pack(side="bottom")


    # TreeViewのセットアップ
    def setup_kindComboBox(self):

        self.kindVal = tk.StringVar()

        v=()
        # 表にデータを入れる
        for i in range(len(self.results)):
            rec = self.results[i]
            v = v + (rec[0]+rec[1])

        # ComboBox
        self.comboBox = ttk.Combobox(self.frBox, width=10, values=v, textvariable=self.kindVal, state='readonly')


        # ComboBox bind
        # 項目を選択したら、on_comboBox_select()が呼ばれるようにする
        self.comboBox.bind("<<ComboboxSelected>>", self.on_comboBox_select)

        # TreeViewとScrollView配置
        self.comboBox.pack(side=tk.LEFT, fill=tk.Y)


    # ComboBox 項目選択された時の処理
    def on_comboBox_select(self,event):
        k=self.kindVal.get() # for Debug
        print("selected items:"+k)



    # データベースからデータをロード
    def load_Kind(self):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB()

        # DB Query Execute
        results = myDB.kind_query()

        # Close DataBase
        myDB.close()

        return results  # 検索結果を返す

    # データベースからデータをロード
    def load_Data(self):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB()

        # DB Query Execute
        results = myDB.customer_query()

        # Close DataBase
        myDB.close()

        return results  # 検索結果を返す
