from MyDB import MyDB
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox


class OrderMenuList(ttk.Frame):
    def __init__(self,  *args, **kw):
        super().__init__(*args, **kw)

        # Load Data from Database
        self.kind_results = self.load_Kind()

        # Buttonを作る
        back_button = tk.Button(self, text="メニューに戻る")
        # 任意の名前の仮想イベントを作成しておく
        back_button["command"] = lambda: self.event_generate("<<Page_Back>>")

        # 下地のframe1: frBoxを作る
        self.frBox1 = tk.Frame(self)

        # ラベルを作る
        label1 = ttk.Label(self.frBox1,text="日付 ",width=8)
        # 日付ピッカーを作る
        self.calendar = DateEntry(self.frBox1, locale='ja_JP.UTF-8', date_pattern='y/mm/dd', width=14)

        # 下地のframeにcalendarを載せる
        label1.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        self.calendar.pack(side=tk.LEFT, fill=tk.BOTH)

        # 下地のfrBoxにcomboBoxをセットアップする
        label2 = ttk.Label(self.frBox1,text="種別 ",width=8)
        label2.pack(anchor=tk.W,side=tk.LEFT, fill=tk.NONE)
        self.setup_kindComboBox()

        # 下地のframe2: frBoxを作る
        self.frBox2 = tk.Frame(self)
        self.setup_originalMenuTreeView()

        # 下地のframe3: frBoxを作る
        self.frBoxBtn = tk.Frame(self)
        self.setup_BoxBtn()

        # 下地のframe3: frBoxを作る
        self.frBox3 = tk.Frame(self)
        self.setup_orderMenuTreeView()

        # Frameを配置
        self.frBox1.pack()
        self.frBox2.pack()
        self.frBoxBtn.pack()
        self.frBox3.pack()

        # Buttonを配置
        back_button.pack(side="bottom")


    # ComboBox のセットアップ
    def setup_kindComboBox(self):
        # kindVal ← 選択した時の値
        self.kindVal = tk.StringVar()

        # 空タプル
        v=()
        # 表にデータを入れる
        for i in range(len(self.kind_results)):
            rec = self.kind_results[i]
            item = str(rec[0]) + " " + rec[1]
            v = v + (item,)

        # ComboBox
        self.comboBox = ttk.Combobox(self.frBox1, width=10, values=v, textvariable=self.kindVal, state='readonly')

        # ComboBox bind
        # 項目を選択したら、on_comboBox_select()が呼ばれるようにする
        self.comboBox.bind("<<ComboboxSelected>>", self.on_comboBox_select)

        # TreeViewとScrollView配置
        self.comboBox.pack(side=tk.LEFT, fill=tk.Y)


    # ComboBox 項目選択された時の処理
    def on_comboBox_select(self,event):
        # 選択された値をセット
        k = self.kindVal.get()
        # (code name) からcodeだけ取り出す
        rec = k.split()
        print("selected items:"+k) # for Debug

        # code を条件にして抽出
        self.menu_results=self.Load_OriginalMenu(rec[0])

        # TreeView 中身のクリア
        self.orgMenu.delete(*self.orgMenu.get_children())
        # 表にデータを入れる
        for i in range(len(self.menu_results)):
            rec = self.menu_results[i]
            self.orgMenu.insert("", "end", values=(str(rec[0]), rec[1], str(rec[2]), rec[3] ) )


    # TreeView のセットアップ
    def setup_originalMenuTreeView(self):
        # TreeView (ListBox)
        self.orgMenu = ttk.Treeview(self.frBox2)
        # 列を作成（4列）
        self.orgMenu["columns"] = ('original_menu_id', 'original_menu_name','k_code','standard_price')
        # ヘッダーの設定
        self.orgMenu["show"] = "headings"
        self.orgMenu.heading('original_menu_id', text="ID")
        self.orgMenu.heading('original_menu_name', text="メニュー名")
        self.orgMenu.heading('k_code', text="分類コード")
        self.orgMenu.heading('standard_price', text="標準価格")
        # 各列の幅設定
        self.orgMenu.column('original_menu_id', width=40)
        self.orgMenu.column('original_menu_name',width=180)
        self.orgMenu.column('k_code',width=30)
        self.orgMenu.column('standard_price',width=60)

        # Scrollbarを作る
        self.scrollbar = ttk.Scrollbar(
            self.frBox2,
            orient=tk.VERTICAL,
            command=self.orgMenu.yview)
        self.orgMenu['yscrollcommand'] = self.scrollbar.set

        # TreeView
        # 項目を選択したら、on_tree_select()が呼ばれるようにする
        self.orgMenu.bind("<<TreeviewSelect>>", self.on_orgMenu_select)

        # TreeViewとScrollView配置
        self.orgMenu.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)


    # ComboBox 項目選択された時の処理
    def on_orgMenu_select(self,event):
        print("selected items:")
        self.selectRec['text'] =''
        for item in self.orgMenu.selection():
            self.selectRec['text'] = str(self.orgMenu.item(item)['values'])
            print(self.orgMenu.item(item)['values'])  # for Debug


    def setup_BoxBtn(self):
        self.selectRec = ttk.Label(self.frBoxBtn,text="",width=10)
        label = ttk.Label(self.frBoxBtn,text="提供数",width=5)
        self.availableCount = ttk.Entry(self.frBoxBtn,width=20)
        insert_button = tk.Button(self.frBoxBtn, text=" 追加 [↓] ")
        insert_button["command"] = lambda: self.insert_menu()
        delete_button = tk.Button(self.frBoxBtn, text=" 削除 [↓] ")
        delete_button["command"] = lambda: self.delete_menu()

        self.selectRec.pack(side=tk.LEFT, fill=tk.Y)
        label.pack(side=tk.LEFT, fill=tk.Y)
        insert_button.pack(side=tk.LEFT, fill=tk.Y)
        delete_button.pack(side=tk.LEFT, fill=tk.Y)


    def insert_menu(self):
        # メッセージボックス表示
        messagebox.showinfo("Insert!","その日付にメニューを追加しちゃうよ")


    def delete_menu(self):
        # メッセージボックス表示
        messagebox.showinfo("Delete!","その日付からメニューを除いちゃうよ")


    def setup_orderMenuTreeView(self):
        # TreeView (ListBox)
        self.orderMenutree = ttk.Treeview(self.frBox3)
        # 列を作成（4列）
        self.orderMenutree["columns"] = ('order_menu_id', 'order_date','original_menu_id','price','order_available')
        # ヘッダーの設定
        self.orderMenutree["show"] = "headings"
        self.orderMenutree.heading('order_menu_id', text="ID")
        self.orderMenutree.heading('order_date', text="日付")
        self.orderMenutree.heading('original_menu_id', text="オリジナルメニューID")
        self.orderMenutree.heading('price', text="価格")
        self.orderMenutree.heading('order_available', text="状態")

        # 各列の幅設定
        self.orderMenutree.column('order_menu_id', width=40)
        self.orderMenutree.column('order_date',width=100)
        self.orderMenutree.column('original_menu_id',width=40)
        self.orderMenutree.column('price',width=60)
        self.orderMenutree.column('order_available',width=60)

        # Scrollbarを作る
        self.scrollbar2 = ttk.Scrollbar(
            self.frBox3,
            orient=tk.VERTICAL,
            command=self.orderMenutree.yview)
        self.orderMenutree['yscrollcommand'] = self.scrollbar2.set

        # TreeView
        # 項目を選択したら、on_tree_select()が呼ばれるようにする
        self.orderMenutree.bind("<<TreeviewSelect>>", self.on_orderMenutree_select)

        # TreeViewとScrollView配置
        self.orderMenutree.pack(side=tk.LEFT, fill=tk.Y)
        self.scrollbar2.pack(side=tk.LEFT, fill=tk.Y)


    def on_orderMenutree_select(self,event):
        print("selected items:")
        for item in self.orderMenutree.selection():
            print(self.orderMenutree.item(item)['values'])  # for Debug


    # データベースからデータをロード
    # 種別
    def load_Kind(self):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB()
        # DB Query Execute
        results = myDB.kind_query()
        # Close DataBase
        myDB.close()
        return results  # 検索結果を返す


    # Original Menu
    def Load_OriginalMenu(self, k_code):
        # Connect DataBase ('MyLibrary')
        myDB = MyDB()
        # DB Query Execute
        results = myDB.original_menu_query(k_code)
        # Close DataBase
        myDB.close()
        print(results) # for Debug
        return results  # 検索結果を返す