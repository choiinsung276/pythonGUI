import wx


class ChildFrame(wx.Frame):
    def __init__(self, parent, title=None, size=(200,200)):  # 생성자
        super().__init__(parent, title=title, size=size)
        self.gui()


    def gui(self):
        # 메뉴 디자인 : 고정식 메뉴 , 이동식 메뉴
        # MenuBar, Menu, MenuItem
        menubar=wx.MenuBar()
        mnuFile = wx.Menu()
        mnuEdit = wx.Menu()

        mnuFile_new = wx.MenuItem(mnuFile,wx.ID_NEW,"New","New Document")
        mnuFile_open = wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", "파일 열기")
        mnuFile_exit = wx.MenuItem(mnuFile, wx.ID_EXIT, "Exit", "프로그램 종료")

        mnuFile.Append(mnuFile_new)
        mnuFile.Append(mnuFile_open)
        mnuFile.AppendSeparator()
        mnuFile.Append(mnuFile_exit)
        menubar.Append(mnuFile,"파일")
        menubar.Append(mnuEdit,"편집")
        self.SetMenuBar(menubar)

        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.Bind(wx.EVT_MENU, self.onNew, mnuFile_new)
        self.Bind(wx.EVT_MENU, self.onOpen, mnuFile_open)
        self.Bind(wx.EVT_MENU, self.onExit, mnuFile_exit)

        #self.Move(100, 50)
        self.Center() #가운데로
        self.Show(True)

    def onNew(self, ev):
        self.txtA.SetLabelText("새 문서를 선택하였습니다.")


    def onOpen(self, ev):
        #self.txtA.SetLabelText("파일 열기를 선택하였습니다.")
        f = open("C:\\Users\\최인성\\PycharmProjects\\pythonproject\\download\\GUI 파이썬.txt","r")
        data = f.read()
        self.txtA.SetLabelText(data)
        f.close()

    def onExit(self, ev):
        self.txtA.SetLabelText("프로그램 종료를 선택하였습니다.")
        self.Close(True)
if __name__ == "__main__":
    app = wx.App()
    ChildFrame(None, "간단한 메모장 프로그램",(400, 600))
   # frame.Show(True)
    app.MainLoop()
