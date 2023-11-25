# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
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
# ///////////////////////////////////////////////////////////////

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from qt_core import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from ui_AbiRechner import Ui_Form
import os
# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.faecher=[]
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        #self.ui = Ui_Form()
        #self.ui.setup_ui(self)

    def CreateNewFach(self,parent):
        fach=PyFach(
            parent=parent,
            app_parent = parent,
            bg_color=self.themes["app_color"]["dark_one"],
        )
        self.ui.verticalLayout_10.addWidget(fach)
        self.faecher.append(fach)
    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self,parent):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////

        self.ui=parent.ui
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings(parent.settingFilesFolderPath)
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes(parent.settingFilesFolderPath)
        self.themes = themes.items

        parent.setWindowTitle(self.settings["app_name"])
        parent.setWindowIcon(QtGui.QIcon(self.settings["icon"]))

        #Tab 1
        self.push_button_New = PyPushButton(
            text="Add New",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_New.setMaximumHeight(30)
        self.push_button_New.setMinimumHeight(30)
        self.push_button_New.setMaximumWidth(150)

        self.push_button_Calculate = PyPushButton(
            text="Calculate",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_Calculate.setMaximumHeight(30)
        self.push_button_New.setMinimumHeight(30)
        self.push_button_Calculate.setMaximumWidth(150)

        self.defaultFach_1=PyFach(
            parent=parent,
            app_parent = parent,
            bg_color=self.themes["app_color"]["dark_one"],
            fachName="LeistungsFach 1.",
            istLeistungsfach=True,
            istAbiFach=True
        )
        self.defaultFach_2 = PyFach(
            parent=parent,
            app_parent=parent,
            bg_color=self.themes["app_color"]["dark_one"],
            fachName="LeistungsFach 1.",
            istLeistungsfach= True,
            istAbiFach=True
        )
        self.defaultFach_3 = PyFach(
            parent=parent,
            app_parent=parent,
            bg_color=self.themes["app_color"]["dark_one"],
            fachName="GrundKurs 2.",
            istLeistungsfach=False,
            istAbiFach=True
        )
        self.defaultFach_4 = PyFach(
            parent=parent,
            app_parent=parent,
            bg_color=self.themes["app_color"]["dark_one"],
            fachName="GrundKurs 2.",
            istLeistungsfach=False,
            istAbiFach=True
        )
        self.defaultFach_5 = PyFach(
            parent=parent,
            app_parent=parent,
            bg_color=self.themes["app_color"]["dark_one"],
            fachName="GrundKurs 3.",
            istLeistungsfach=False,
            istAbiFach=True
        )
        self.faecher.append(self.defaultFach_1)
        self.faecher.append(self.defaultFach_2)
        self.faecher.append(self.defaultFach_3)
        self.faecher.append(self.defaultFach_4)
        self.faecher.append(self.defaultFach_5)
        # Tab 2

        self.push_button_5 = PyPushButton(
            text="频谱图",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_5.setMaximumHeight(30)

        self.push_button_6 = PyPushButton(
            text="Open File",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_6.setMaximumHeight(30)
        self.push_button_6.setMaximumWidth(150)

        self.push_button_7 = PyPushButton(
            text="转原图片",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_7.setMaximumHeight(30)

        self.line_edit_7 = PyLineEdit(
            text="",
            place_holder_text="Opened File Path",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_7.setMinimumHeight(30)
        self.line_edit_7.setMaximumWidth(150)



        #Tab 1 add widget
        self.ui.functionPanel.addWidget(self.push_button_New)
        self.ui.functionPanel.addWidget(self.push_button_Calculate)

        self.ui.verticalLayout_10.addWidget(self.defaultFach_1)
        self.ui.verticalLayout_10.addWidget(self.defaultFach_2)
        self.ui.verticalLayout_10.addWidget(self.defaultFach_3)
        self.ui.verticalLayout_10.addWidget(self.defaultFach_4)
        self.ui.verticalLayout_10.addWidget(self.defaultFach_5)
        #Tab 2 add widget

        self.ui.verticalLayout_8.addWidget(self.push_button_5)
        self.ui.verticalLayout_5.addWidget(self.push_button_6)
        self.ui.verticalLayout_8.addWidget(self.push_button_7)
        self.ui.verticalLayout_5.addWidget(self.line_edit_7)

