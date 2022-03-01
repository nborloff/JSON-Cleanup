from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtGui import QIcon 


class WindowExample(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("JSON Prettifier")
        self.setWindowIcon(QIcon('json.png'))

        self.setStyleSheet('background-color: cyan')
        self.create_buttons()
        
        self.show()

    def create_buttons(self):
        btn1 = QPushButton("Click Me", self)
        btn1.setStyleSheet('background-color: white')
        btn1.setGeometry(100, 100, 100, 100)

        



app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())