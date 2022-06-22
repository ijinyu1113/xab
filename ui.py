import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Tools.scripts.serve import app
from PIL.ImageQt import ImageQt

from app import *


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)


class AppDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(600, 600)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()

            filetype = get_filetype(os.path.splitext(file_path)[1]);

            if int(filetype) > 0:
                self.set_image_to_image(file_path)
            else:
                pil_img = read_dicom(file_path, f_type='pil')
                qim = ImageQt(pil_img)
                self.set_image_to_byte(qim)

            ResultSupport.result = ChestXrayAnalysis().analysis(file_path)
            print(ResultSupport.result)

            result_label = self.parent().label2
            result_label.setText(ResultSupport.result)
            result_label.setFont(QFont("Arial", 15))
            result_label.setAlignment(Qt.AlignCenter)

            event.accept()
        else:
            event.ignore()

    def set_image_to_byte(self, qim):
        self.photoViewer.setPixmap(QPixmap.fromImage(qim).scaledToWidth(590))

    def set_image_to_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path).scaledToWidth(590))



class ResultSupport():
    result = "";


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.lstView = AppDemo(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('X-ab: Detecting Chest-Xray Abnormality')
        self.setWindowIcon(QIcon('AIimage.jpg'))
        self.setGeometry(300, 300, 300, 200)
        self.resize(850, 600)
        self.center()
        self.setAcceptDrops(True)

        self.label1 = QLabel('Analysis result', self)
        self.label1.setGeometry(QRect(635, 10, 210, 100))
        self.label1.setFont(QFont("Arial", 12))

        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(600, 100, 240, 400))
        self.label2.setStyleSheet('color:navy;background:#ffffff; border-style: solid; border-width: 2px; border-color: #000000; border-radius: 10px;')

        # btnRun = QPushButton("Analyse", self)  # 버튼 텍스트
        # btnRun.move(670, 550)  # 버튼 위치
        # btnRun.clicked.connect(self.btnRun_clicked)

        self.show()

    def btnRun_clicked(self):
        print("btnRun_clicked Start")
        print(ResultSupport().result)
        self.label2.setText(ResultSupport.result)
        self.label2.setFont(QFont("Arial", 12))
        self.label2.setAlignment(Qt.AlignCenter)
        print("btnRun_clicked End")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())