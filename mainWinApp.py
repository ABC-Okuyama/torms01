import tkinter as tk
from LayeredFrame import LayeredFrame
from MyFrame01 import MyFrama01
from MyFrame02 import MyFrama02
from MyFrame04 import MyFrama04
from CustomerList import CustomerList
from OrderMenuList import OrderMenuList


# アプリケーションクラスだよ
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Windowの大きさを指定
        self.master.geometry("600x400")
        self.create_windows()


    # Window の設定
    def create_windows(self):
        # master=rootの上に frameを構築する
        # frame に対して複数のページを登録する
        layered_frame = LayeredFrame(self.master)

        # frameのレイアウトを設定
        # 以下 参照のこと
        # https://www.shido.info/py/tkinter2.html
        layered_frame.pack(fill=tk.BOTH, expand=True)

        # frameに onPageChanged をくっつける
        # 仮想イベント<<StackedFrame_PageChanged>>が発生したら、onPageChaneged()が呼ばれる
        layered_frame.bind("<<StackedFrame_PageChanged>>", self.onPageChanged)

        # page1 はMyFrame01クラスのインスタンスを作り、追加
        page1 = MyFrama01(layered_frame)
        # 第1引数:仮想イベントと 第2引数:処理  を結びつける(bindする)
        page1.bind("<<Page_Menu>>", layered_frame.toPage("テキスト入力"))
        page1.bind("<<Page_Customer>>", layered_frame.toPage("お客様情報"))
        page1.bind("<<Page_Reservation>>", layered_frame.toPage("page4"))
        page1.bind("<<Page_ViewMenu>>", layered_frame.toPage("viewMenu"))
        page1.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了

        # frameに page1を 追加
        layered_frame.addPage(page1, "メイン")

        # # page2 は MyFrame02クラスのインスタンスを作る
        page2 = MyFrama02(layered_frame)
        page2.bind("<<Page_Back>>", layered_frame.toPage("メイン"))
        page2.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了

        # frameに page2を 追加
        layered_frame.addPage(page2, "テキスト入力")

        # page3 は CustomerListクラスのインスタンスを作る
        page3 = CustomerList(layered_frame)
        page3.bind("<<Page_Back>>", layered_frame.toPage("メイン"))
        page3.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了

        # frameに page3を 追加
        layered_frame.addPage(page3, "お客様情報")

        # pageMenu は MenuListクラスのインスタンスを作る
        pageMenu = OrderMenuList(LayeredFrame)
        pageMenu.bind("<<Page_Back>>", layered_frame.toPage("メイン"))
        pageMenu.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了

        # frameに pageMenuを追加
        layered_frame.addPage(pageMenu, "viewMenu")

        page4 = MyFrama04(layered_frame)
        page4.bind("<<Page_Back>>", layered_frame.toPage("メイン"))
        page4.bind("<<Page_Exit>>", lambda _: self.master.quit())  # アプリ終了
        #
        layered_frame.addPage(page4, "page4")

        # root.main_loopの中で
        # frame.changePage()を呼び出すようにする
        # 最初に page1 の表示をするように
        self.master.after_idle(layered_frame.changePage, "メイン")


    # pageが変わったら呼ばれる
    def onPageChanged(self, event):
        if isinstance(event.widget, LayeredFrame):
            name = event.widget.currentPageName
            print("PageChanged", name)      # for Debug
            self.master.title(name)


    def callBack(self):
        pass        # 使わないかも pass


# main() だよ
def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


# Startup EntryPoint
if __name__ == "__main__":
    main()
