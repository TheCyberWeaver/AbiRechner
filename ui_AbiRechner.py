# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AbiRechner.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(501, 646)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"/*\u8bbe\u7f6e\u5bf9\u8c61\u540d\u4e3aTW_SampleResult\u7684QTabWidget\u63a7\u4ef6*/\n"
"QTabWidget#TW_SampleResult>QTabBar::tab\n"
"{\n"
"     font: 15pt \"Chinese fine black\";\n"
"     background-color:rgb(104,191,249);\n"
"     min-width: 100px;\n"
"     min-height: 30px;\n"
"     padding: 2px;\n"
"}\n"
"/*\u8bbe\u7f6e\u5bf9\u8c61\u540d\u4e3aTW_SampleResult\u7684QTabWidget\u63a7\u4ef6*/\n"
"QTabWidget#TW_SampleResult>QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(228, 233, 242);\n"
"}\n"
" \n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(228, 233, 242);\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 32))
        self.label_11.setStyleSheet(u"font: 700 18pt \"Segoe Print\";")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 12))
        self.label_12.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.functionPanel = QHBoxLayout()
        self.functionPanel.setObjectName(u"functionPanel")

        self.verticalLayout.addLayout(self.functionPanel)

        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"#scrollArea{\n"
"border: none;\n"
"border-radius:15px;\n"
"background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 459, 517))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_6.addLayout(self.verticalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 32))
        self.label.setStyleSheet(u"font: 700 18pt \"Segoe Print\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 12))
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe Print\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout_2.addLayout(self.verticalLayout_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Abitur-Note-Prognose", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Field1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Mecklenburg Vorpommern", None))
        self.label.setText(QCoreApplication.translate("Form", u"Abitur-Note-Prognose", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Field 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Analyze", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Page", None))
    # retranslateUi

