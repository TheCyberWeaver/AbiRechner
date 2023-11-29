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
from qt_core import *

# IMPORT FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
# IMPORT DIV
# ///////////////////////////////////////////////////////////////
from . py_div import PyDiv

# IMPORT BUTTON
# ///////////////////////////////////////////////////////////////
from . py_fach_button import PyTitleButton
from ..py_push_button import PyPushButton
from ..py_slider import PySlider
from ..py_line_edit import PyLineEdit
# GLOBALS
# ///////////////////////////////////////////////////////////////
_is_maximized = False
_old_size = QSize()

#TODO:Add all subjects
NameAllerFaecher=["Deutsch", "Mathe",
                  "Englisch", "Spanisch", "Französisch","Latein","Russisch",
                  "Geschichte", "Info",
                  "Physik", "Chemie", "Biologie",
                  "Musik","Kunst",
                  "Religion", "Philosophie",
                  "Gemeinschaftskunde","Geographie",
                  "Sport"]

class PyFach(QWidget):
    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)
    def __init__(
        self,
        parent,
        app_parent,
        logo_image = "logo_top_22x22.svg",
        logo_width = 100,
        buttons = None,
        dark_one = "#1b1e23",
        bg_color = "#343b48",
        div_color = "#3c4454",
        btn_bg_color = "#343b48",
        btn_bg_color_hover = "#3c4454",
        btn_bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#6c99f4",
        text_foreground = "#8a95aa",
        radius = 8,
        font_family = "Segoe UI",
        title_size = 10,
        is_custom_title_bar = True,

        fachName="FachName1",
        istLeistungsfach=False,
        istAbiFach=False

    ):
        super().__init__()

        settings = Settings()
        self.settings = settings.items

        self.themes = Themes().items

        # PARAMETERS
        self._logo_image = logo_image
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._div_color = div_color
        self._parent = parent
        self._app_parent = app_parent
        self._btn_bg_color = btn_bg_color
        self._btn_bg_color_hover = btn_bg_color_hover
        self._btn_bg_color_pressed = btn_bg_color_pressed  
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._font_family = font_family
        self._title_size = title_size
        self._text_foreground = text_foreground
        self._is_custom_title_bar = is_custom_title_bar

        self._fachName=fachName
        self._istLeistungsfach=istLeistungsfach
        self._istAbiFach=istAbiFach
        #self.name="Deutsch"
        # SETUP UI
        self.setup_ui()

    # SETUP APP
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.titleFrame = QFrame()
        self.titleLayout= QVBoxLayout(self.titleFrame)

        # TITLE LABEL
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setStyleSheet(f'font: {self._title_size}pt "{self._font_family}"')
        self.title_label.setText(self._fachName)

        self.marksInputLineEditsFrame = QFrame()
        self.marksInputLineEditsLayout = QHBoxLayout(self.marksInputLineEditsFrame)

        self.rightFrame = QFrame()
        self.rightFrame.setMaximumWidth(300)
        self.rightLayout = QVBoxLayout(self.rightFrame)


        self.comboBoxFach = QComboBox()
        self.comboBoxFach.addItems(NameAllerFaecher)

        self.marksInput_line_edits=[]
        numberOfLineEdit=4
        if self._istAbiFach:
            numberOfLineEdit=5
        for i in range(numberOfLineEdit):
            line_edit = PyLineEdit(
                text="",
                place_holder_text=str(i+1)+".",
                radius=8,
                border_size=2,
                color=self.themes["app_color"]["text_foreground"],
                selection_color=self.themes["app_color"]["white"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_active=self.themes["app_color"]["dark_three"],
                context_color=self.themes["app_color"]["context_color"]
            )
            line_edit.setMinimumHeight(30)
            line_edit.setMaximumWidth(50)
            self.marksInput_line_edits.append(line_edit)


        self.slider = PySlider(
            parent=self._parent,
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],

        )
        self.slider.setOrientation (Qt.Orientation.Horizontal)
        self.slider.setMaximum(15)
        self.slider.setMinimum(0)
        self.slider.setMinimumHeight(25)

        self.titleLayout.addWidget(self.title_label)
        self.titleLayout.addWidget(self.comboBoxFach)

        for line_edit in self.marksInput_line_edits:
            self.marksInputLineEditsLayout.addWidget(line_edit)

        self.rightLayout.addWidget(self.marksInputLineEditsFrame)
        self.rightLayout.addWidget(self.slider)

        self.main_layout.addWidget(self.titleFrame)
        self.main_layout.addWidget(self.rightFrame)

        #change the numbers in the input area when slider has been changed
        self.slider.valueChanged.connect(lambda: self.sliderChanged())

    def sliderChanged(self):
        for lineEdit in self.marksInput_line_edits:
            lineEdit.setText(str(self.slider.value()))