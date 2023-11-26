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
from gui.core.json_themes import Themes

import sys


#matplotlib.use('Qt5Agg')

#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
#from matplotlib.figure import Figure
from ui_AbiRechner import Ui_Form
from setup_ui import SetupMainWindow
#An Example of ploting graphs in pyside6

converting_table=[(300,4.0),(301,3.9),(319,3.8),(337,3.7),(355,3.6),(373,3.5),(391,3.4),(409,3.3),(427,3.2),(445,3.1),
                  (463,3.0),(481,2.9),(499,2.8),(517,2.7),(535,2.6),(553,2.5),(571,2.4),(589,2.3),(607,2.2),(625,2.1),
                  (643,2.0),(661,1.9),(679,1.8),(697,1.7),(715,1.6),(733,1.5),(751,1.4),(769,1.3),(787,1.2),(805,1.1),(823,1.0)]


def convert900to6(note: int):
    if note<300:
        return 5.0
    if note>900:
        return 0

    low = 0
    high = len(converting_table) - 1

    while low <= high:

        mid = (low + high) // 2

        guess, note_6 = converting_table[mid]

        if guess == note:
            return note_6

        if guess > note:
            high = mid - 1

        else:
            low = mid + 1
    guess, note_6 = converting_table[high]
    return note_6
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


    # ///////////////////////////////////////////////////////////////////////////////////////////////
    # Tab 1
    # ///////////////////////////////////////////////////////////////////////////////////////////////
    def checkFach(self):
        returnStr="Rechnen nicht möglich wegen folgenden Ursachen:\n"

        FachNameList=[]

        hasTwoSameFach=False
        #BlockOne
        hasDeutsch=False
        hasMathe=False
        hasGesellschaftswissenschaft=False

        #BlockTwo
        hasfremdSprache=False
        hasMusikOderKunst=False
        hasSport=False
        hasGemeinschaftskundeOderGeo=False
        hasReligionOderPhilo=False
        for Fach in self.AddedUI.faecher:
            fachName=Fach.comboBoxFach.currentText()
            FachNameList.append(fachName)
            if fachName=="Deutsch":
                hasDeutsch=True
            if fachName=="Mathe":
                hasMathe=True
            if fachName=="Geschichte" or fachName=="Geographie" or fachName=="Gemeinschaftskunde":
                hasGesellschaftswissenschaft=True

        if not hasDeutsch:
            returnStr += "Deustch muss gewählt werden!\n"
        if not hasMathe:
            returnStr += "Mathe muss gewählt werden!\n"
        if not hasGesellschaftswissenschaft:
            returnStr += "Eine Gesellschaftswissenschaft muss gewählt werden!\n"

        set_lst = set(FachNameList)
        print(set_lst)

        if len(set_lst) != len(FachNameList):
            print("ah?")
            hasTwoSameFach=True
            returnStr += "Zwei gleiche Fächer werden gleichzeitiggewählt!\n"

        if not hasTwoSameFach and hasDeutsch and hasMathe and hasGesellschaftswissenschaft:
            return "success"
        return returnStr

    def calculateNote(self):

        if self.checkFach()!="success":
            dlg = CalculateFailedDialog(self.checkFach())
            dlg.setWindowTitle("Calculation Failed!")
            dlg.exec_()
            return
        totalNote=0

        blockOne=0
        for Fach in self.AddedUI.faecher[:5]:
            if Fach.line_edits[4].text()!="":
                blockOne+=int(Fach.line_edits[4].text())*4

        blockTwo=0
        for Fach in self.AddedUI.faecher:
            sumOfFach=0
            currentCountOfSemester=0
            for semesterIndex in range(4):
                currentCountOfSemester+=1
                if Fach.line_edits[semesterIndex].text()!="":
                    sumOfFach+=int(Fach.line_edits[semesterIndex].text())
                else:
                    sumOfFach+=sumOfFach/currentCountOfSemester
            if Fach._istLeistungsfach:
                blockTwo+=sumOfFach*2
            else:
                blockTwo += sumOfFach
        totalNote=blockTwo+blockOne

        dlg = CalculationOutputPanel(totalNote)
        dlg.setWindowTitle("Calculation Success!")
        dlg.exec_()
        #print(totalNote)




class CalculateFailedDialog(QDialog):
    def __init__(self,errorMessage:str):
        super().__init__()

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(errorMessage)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CalculationOutputPanel(QDialog):
    def __init__(self,note):
        super().__init__()
        self.settings = Settings("").items
        self.themes = Themes().items
        self.setWindowTitle("Success!")

        self.setMinimumHeight(200)
        self.setMinimumWidth(300)

        notePercentage=round(note/900*100)
        self.circular_progress_1 = PyCircularProgress(
            value=notePercentage,
            progress_color=self.themes["app_color"]["pink"],
            text_color=self.themes["app_color"]["context_color"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"],
        )

        self.circular_progress_1.setFixedSize(100, 100)


        self.line_edit = PyLineEdit(
            text=str(convert900to6(note))+" <"+str(round(note))+">",
            place_holder_text="",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setEnabled(False)
        self.line_edit.setMinimumHeight(30)
        self.line_edit.setMaximumWidth(150)
        self.line_edit.setAlignment(Qt.AlignCenter)

        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignCenter)
        title_size = 10
        font_family = "Segoe UI"
        self.title_label.setStyleSheet(f'font: {title_size}pt "{font_family}"')
        self.title_label.setText("Total Points:")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.circular_progress_1)

        self.setLayout(self.layout)
if __name__ == "__main__":

    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = AbiRechner()
    print("[info]: Process", window.settings["app_name"], "is starting")
    window.show()

    sys.exit(app.exec())