import sys
from PyQt5.QtWidgets import*
from ytmp3 import Ui_Form
from main import Fetch_video_and_turn_to_mp3

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.music_num=0
        self.ui = Ui_Form() #新增剛剛拉的前端介面
        self.ui.setupUi(self)
        self.ui.Transform_button.clicked.connect(self.button_click)
        self.show() #show
    def button_click(self):
        URL=self.ui.URL_input.text()
        filename=self.ui.Filename_input.text()
        if filename=='':
            filename="tmp"+str(self.music_num)
        if URL!='':
            To_mp3_class=Fetch_video_and_turn_to_mp3(URL,filename)
            To_mp3_class.downloadmp3()
            self.music_num+=1


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
