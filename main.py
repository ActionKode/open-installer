import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
from zipfile import ZipFile
import zipfile
import hjson


url: list[str] = ["http://www.ovh.net/files/10Mb.dat"]


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("installer")
        self.initUi()
        self.setFixedSize(QSize(400, 300))
        self.setWindowIcon(QIcon("Icon.ico"))
        self.show()

    def initUi(self):
        self.pbar = QProgressBar(self)

        # setting its geometry
        self.pbar.setGeometry(30, 40, 200, 25)

        # creating push button
        self.btn = QPushButton("Start", self)

        # changing its position
        self.btn.move(40, 80)

        # adding action to push button
        self.btn.clicked.connect(self.download)

        # setting window geometry
        self.setGeometry(300, 300, 280, 170)

        # setting window action
        self.setWindowTitle("Installer")

        # showing all the widgets
        self.show()

    def download(self):
        try:
            for item in url:
                r = requests.get(item, stream=True)
                fileName = "file"
                progress = 0
                with open(f"{fileName}.tmp", "wb") as file:
                    for data in r.iter_content():
                        progress += len(data)
                        self.pbar.setValue(progress)
                        print(progress)
                        file.write(data)
                print("done")
                
                try:
                    with ZipFile(f"{fileName}.tmp", "r") as f:
                        f.extractall(fileName)
                except (zipfile.BadZipFile, FileNotFoundError) as e:
                    print("not a zip file or file not found", e)
            return
        except requests.exceptions.ConnectionError as e:
            if e == requests.exceptions.ConnectionError:
                print("unable to conect to internet")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
