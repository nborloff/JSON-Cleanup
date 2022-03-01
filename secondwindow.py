from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon 


class WindowExample(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("JSON Prettifier")
        self.setWindowIcon(QIcon('json.png'))

        self.setStyleSheet('background-color: cyan')
        
        self.show()



app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())