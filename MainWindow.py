# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 230)
        Form.setMinimumSize(QSize(400, 230))
        Form.setMaximumSize(QSize(400, 230))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 16))
        self.today = QLabel(Form)
        self.today.setObjectName(u"today")
        self.today.setGeometry(QRect(10, 30, 381, 51))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.today.setFont(font)
        self.today.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 91, 16))
        self.save_addr = QLineEdit(Form)
        self.save_addr.setObjectName(u"save_addr")
        self.save_addr.setGeometry(QRect(10, 130, 381, 21))
        self.catch_button = QPushButton(Form)
        self.catch_button.setObjectName(u"catch_button")
        self.catch_button.setGeometry(QRect(150, 180, 100, 32))
        self.status = QLabel(Form)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(170, 160, 58, 16))
        self.status.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u65e5\u671f\uff1a", None))
        self.today.setText(QCoreApplication.translate("Form", u"/", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.save_addr.setPlaceholderText(QCoreApplication.translate("Form", u"BingImages", None))
        self.catch_button.setText(QCoreApplication.translate("Form", u"\u6293\u53d6", None))
        self.status.setText("")
    # retranslateUi

