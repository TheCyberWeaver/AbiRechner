# coding:utf-8
# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
# PROJECT MADE WITH: Qt Designer and PySide6
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
from qt_core import *
from gui.widgets import *
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
from gui.core.json_settings import Settings

import sys
import numpy as np
#from readonly.HeightsModule import *
#import matplotlib
#import matplotlib.pyplot as plt

#matplotlib.use('Qt5Agg')

#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
#from matplotlib.figure import Figure
from ui_AbiRechner import Ui_Form
from setup_ui import SetupMainWindow
#An Example of ploting graphs in pyside6
"""
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

#An Example of ploting graphs in pyside6
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        self.show()
"""
class AbiRechner(QWidget):

    def __init__(self):
        super().__init__()
        self.settingFilesFolderPath = ""

        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)



        settings = Settings(self.settingFilesFolderPath)
        print("[info]: using", settings.settings_path)
        self.settings = settings.items
        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        # self.hide_grips = True  # Show/Hide resize grips
        self.AddedUI=SetupMainWindow()

        self.AddedUI.setup_gui(parent=self)

        self.filePath=""

        self.uiInitiation()

    def uiInitiation(self):
        # Tab 1
        self.AddedUI.push_button_New.clicked.connect(lambda: self.AddedUI.CreateNewFach(self))
        self.AddedUI.push_button_Calculate.clicked.connect(lambda: self.calculateNote())

        #Tab 2
        #self.push_button_6.clicked.connect(lambda: self.openFile())
        #self.push_button_5.clicked.connect(lambda: self.Conversion())

    # ///////////////////////////////////////////////////////////////////////////////////////////////
    # Tab 1
    # ///////////////////////////////////////////////////////////////////////////////////////////////
    def checkFach(self):
        return True
    def calculateNote(self):
        totalNote=0
        for Fach in self.AddedUI.faecher:
            sumOfFach=0
            currentCountOfSemester=0
            for Semester in Fach.line_edits:
                currentCountOfSemester+=1
                if Semester.text()!="":
                    sumOfFach+=int(Semester.text())
                else:
                    sumOfFach+=sumOfFach/currentCountOfSemester
            if Fach._istLeistungsfach:
                totalNote+=sumOfFach*2
            else:
                totalNote += sumOfFach
        print(totalNote)
    # ///////////////////////////////////////////////////////////////////////////////////////////////
    # Tab 2
    # ///////////////////////////////////////////////////////////////////////////////////////////////
    def openFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            self,
            "选择你要上传的图片",  # 标题
            r"D:\\",  # 起始目录
            "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.line_edit_7.setText(self.filePath)


if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = AbiRechner()
    print("[info]: Process", window.settings["app_name"], "is starting")
    window.show()

    sys.exit(app.exec())