# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_builder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFont, ImageDraw
from builder import add_image, resize, costs_img, characteristic_img


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        font_db = QtGui.QFontDatabase
        font_db.addApplicationFont('Templates/Fonts/Agency Font for Letters.ttf')

        font = QtGui.QFont()
        font.setFamily("Agency FB")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 601)

        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.unique = QtWidgets.QCheckBox(self.centralwidget)
        self.unique.setGeometry(QtCore.QRect(250, 20, 82, 23))
        font.setPointSize(11)
        self.unique.setFont(font)
        self.unique.setObjectName("UNIQUE")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 480, 141, 61))


        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.card_type = QtWidgets.QComboBox(self.centralwidget)
        self.card_type.setGeometry(QtCore.QRect(130, 20, 111, 31))


        font.setPointSize(11)
        self.card_type.setFont(font)
        self.card_type.setObjectName("card_type")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.card_type.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))


        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 54, 17))


        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 54, 17))


        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.subtitle = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.subtitle.setGeometry(QtCore.QRect(70, 50, 171, 31))


        font.setPointSize(11)
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.subtype = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.subtype.setGeometry(QtCore.QRect(70, 80, 171, 31))


        font.setPointSize(11)
        self.subtype.setFont(font)
        self.subtype.setObjectName("subtype")
        self.health = QtWidgets.QSpinBox(self.centralwidget)
        self.health.setGeometry(QtCore.QRect(730, 10, 61, 26))


        font.setPointSize(11)
        self.health.setFont(font)
        self.health.setObjectName("health/cost")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 0, 41, 31))


        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.category = QtWidgets.QComboBox(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(20, 110, 101, 31))


        font.setPointSize(11)
        self.category.setFont(font)
        self.category.setObjectName("category")
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.color = QtWidgets.QComboBox(self.centralwidget)
        self.color.setGeometry(QtCore.QRect(130, 110, 101, 31))


        font.setPointSize(11)
        self.color.setFont(font)
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.card_type_4 = QtWidgets.QComboBox(self.centralwidget)
        self.card_type_4.setGeometry(QtCore.QRect(250, 110, 101, 31))


        font.setPointSize(11)
        self.card_type_4.setFont(font)
        self.card_type_4.setObjectName("card_type_4")
        self.card_type_4.addItem("")
        self.card_type_4.addItem("")
        self.card_type_4.addItem("")
        self.card_type_4.addItem("")
        self.points = QtWidgets.QSpinBox(self.centralwidget)
        self.points.setGeometry(QtCore.QRect(730, 50, 61, 26))


        font.setPointSize(11)
        self.points.setFont(font)
        self.points.setObjectName("points")
        self.elite_points = QtWidgets.QSpinBox(self.centralwidget)
        self.elite_points.setGeometry(QtCore.QRect(730, 90, 61, 26))


        font.setPointSize(11)
        self.elite_points.setFont(font)
        self.elite_points.setObjectName("elite_points")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 50, 41, 16))


        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 90, 71, 16))


        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(20, 150, 181, 201))


        font.setPointSize(11)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.quote = QtWidgets.QTextEdit(self.centralwidget)
        self.quote.setGeometry(QtCore.QRect(20, 370, 181, 91))


        font.setPointSize(11)
        self.quote.setFont(font)
        self.quote.setObjectName("quote")
        self.plus_point = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point.setGeometry(QtCore.QRect(390, 0, 31, 31))


        font.setPointSize(11)
        self.plus_point.setFont(font)
        self.plus_point.setObjectName("plus_point")
        self.value = QtWidgets.QSpinBox(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(430, 0, 71, 31))


        font.setPointSize(11)
        self.value.setFont(font)
        self.value.setObjectName("value")
        self.cost = QtWidgets.QSpinBox(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(580, 0, 71, 31))
        font.setPointSize(11)
        self.cost.setFont(font)
        self.cost.setObjectName("cost")

        self.characteristic = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic.setGeometry(QtCore.QRect(500, 0, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic.setFont(font)
        self.characteristic.setObjectName("characteristic")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")
        self.characteristic.addItem("")

        self.img_cost = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost.setGeometry(QtCore.QRect(540, 0, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost.setFont(font)
        self.img_cost.setObjectName("characteristic")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")
        self.img_cost.addItem("")

        self.plus_point_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point_2.setGeometry(QtCore.QRect(390, 40, 31, 31))
        font.setPointSize(11)
        self.plus_point_2.setFont(font)
        self.plus_point_2.setObjectName("plus_point_2")
        self.cost_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_2.setGeometry(QtCore.QRect(580, 40, 71, 31))


        font.setPointSize(11)
        self.cost_2.setFont(font)
        self.cost_2.setObjectName("cost_2")
        self.value_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.value_2.setGeometry(QtCore.QRect(430, 40, 71, 31))
        font.setPointSize(11)
        self.value_2.setFont(font)
        self.value_2.setObjectName("value_2")

        self.plus_point_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point_3.setGeometry(QtCore.QRect(390, 80, 31, 31))
        self.plus_point_3.setFont(font)
        self.plus_point_3.setObjectName("plus_point_3")

        self.x_point_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_1.setGeometry(QtCore.QRect(360, 0, 31, 31))
        self.x_point_1.setFont(font)
        self.x_point_1.setObjectName("x_point_1")

        self.x_point_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_2.setGeometry(QtCore.QRect(360, 40, 31, 31))
        self.x_point_2.setFont(font)
        self.x_point_2.setObjectName("x_point_2")

        self.x_point_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_3.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.x_point_3.setFont(font)
        self.x_point_3.setObjectName("x_point_3")

        self.x_point_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_4.setGeometry(QtCore.QRect(360, 120, 31, 31))
        self.x_point_4.setFont(font)
        self.x_point_4.setObjectName("x_point_4")

        self.x_point_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_5.setGeometry(QtCore.QRect(360, 160, 31, 31))
        self.x_point_5.setFont(font)
        self.x_point_5.setObjectName("x_point_5")

        self.x_point_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.x_point_6.setGeometry(QtCore.QRect(360, 200, 31, 31))
        self.x_point_6.setFont(font)
        self.x_point_6.setObjectName("x_point_6")


        self.cost_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_3.setGeometry(QtCore.QRect(580, 80, 71, 31))


        font.setPointSize(11)
        self.cost_3.setFont(font)
        self.cost_3.setObjectName("cost_3")
        self.value_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.value_3.setGeometry(QtCore.QRect(430, 80, 71, 31))


        font.setPointSize(11)
        self.value_3.setFont(font)
        self.value_3.setObjectName("value_3")
        self.plus_point_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point_4.setGeometry(QtCore.QRect(390, 120, 31, 31))


        font.setPointSize(11)
        self.plus_point_4.setFont(font)
        self.plus_point_4.setObjectName("plus_point_4")
        self.cost_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_4.setGeometry(QtCore.QRect(580, 120, 71, 31))


        font.setPointSize(11)
        self.cost_4.setFont(font)
        self.cost_4.setObjectName("cost_4")
        self.value_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.value_4.setGeometry(QtCore.QRect(430, 120, 71, 31))


        font.setPointSize(11)
        self.value_4.setFont(font)
        self.value_4.setObjectName("value_4")
        self.plus_point_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point_5.setGeometry(QtCore.QRect(390, 160, 31, 31))


        font.setPointSize(11)
        self.plus_point_5.setFont(font)
        self.plus_point_5.setObjectName("plus_point_5")
        self.cost_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_5.setGeometry(QtCore.QRect(580, 160, 71, 31))


        font.setPointSize(11)
        self.cost_5.setFont(font)
        self.cost_5.setObjectName("cost_5")
        self.value_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.value_5.setGeometry(QtCore.QRect(430, 160, 71, 31))


        font.setPointSize(11)
        self.value_5.setFont(font)
        self.value_5.setObjectName("value_5")
        self.plus_point_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.plus_point_6.setGeometry(QtCore.QRect(390, 200, 31, 31))


        font.setPointSize(11)
        self.plus_point_6.setFont(font)
        self.plus_point_6.setObjectName("plus_point_6")
        self.cost_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_6.setGeometry(QtCore.QRect(580, 200, 71, 31))


        font.setPointSize(11)
        self.cost_6.setFont(font)
        self.cost_6.setObjectName("cost_6")
        self.value_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.value_6.setGeometry(QtCore.QRect(430, 200, 71, 31))


        font.setPointSize(11)
        self.value_6.setFont(font)
        self.value_6.setObjectName("value_6")
        self.file_select = QtWidgets.QPushButton(self.centralwidget)
        self.file_select.setGeometry(QtCore.QRect(210, 240, 191, 25))


        font.setPointSize(11)
        self.file_select.setFont(font)
        self.file_select.setObjectName("file_select")
        self.imagelbl = QtWidgets.QLabel(self.centralwidget)
        self.imagelbl.setGeometry(QtCore.QRect(410, 240, 251, 311))


        font.setPointSize(11)
        self.imagelbl.setFont(font)
        self.imagelbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imagelbl.setText("")
        self.imagelbl.setObjectName("imagelbl")
        self.card_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.card_name.setGeometry(QtCore.QRect(230, 280, 171, 31))


        font.setPointSize(11)
        self.card_name.setFont(font)
        self.card_name.setObjectName("card_name")

        self.autor_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.autor_name.setGeometry(QtCore.QRect(230, 330, 171, 31))


        font.setPointSize(11)
        self.autor_name.setFont(font)
        self.autor_name.setObjectName("autor_name")
        self.characteristic_2 = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic_2.setGeometry(QtCore.QRect(500, 40, 40, 31))

        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic_2.setFont(font)
        self.characteristic_2.setObjectName("characteristic_2")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")
        self.characteristic_2.addItem("")

        self.img_cost_2 = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost_2.setGeometry(QtCore.QRect(540, 40, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost_2.setFont(font)
        self.img_cost_2.setObjectName("characteristic")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")
        self.img_cost_2.addItem("")

        self.characteristic_3 = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic_3.setGeometry(QtCore.QRect(500, 80, 40, 31))

        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic_3.setFont(font)
        self.characteristic_3.setObjectName("characteristic_3")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")
        self.characteristic_3.addItem("")

        self.img_cost_3 = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost_3.setGeometry(QtCore.QRect(540, 80, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost_3.setFont(font)
        self.img_cost_3.setObjectName("characteristic")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")
        self.img_cost_3.addItem("")

        self.characteristic_4 = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic_4.setGeometry(QtCore.QRect(500, 120, 40, 31))

        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic_4.setFont(font)
        self.characteristic_4.setObjectName("characteristic_4")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")
        self.characteristic_4.addItem("")

        self.img_cost_4 = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost_4.setGeometry(QtCore.QRect(540, 120, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost_4.setFont(font)
        self.img_cost_4.setObjectName("characteristic")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")
        self.img_cost_4.addItem("")

        self.characteristic_5 = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic_5.setGeometry(QtCore.QRect(500, 160, 40, 31))

        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic_5.setFont(font)
        self.characteristic_5.setObjectName("characteristic_5")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")
        self.characteristic_5.addItem("")

        self.img_cost_5 = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost_5.setGeometry(QtCore.QRect(540, 160, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost_5.setFont(font)
        self.img_cost_5.setObjectName("characteristic")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")
        self.img_cost_5.addItem("")

        self.characteristic_6 = QtWidgets.QComboBox(self.centralwidget)
        self.characteristic_6.setGeometry(QtCore.QRect(500, 200, 40, 31))

        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.characteristic_6.setFont(font)
        self.characteristic_6.setObjectName("characteristic_6")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")
        self.characteristic_6.addItem("")

        self.img_cost_6 = QtWidgets.QComboBox(self.centralwidget)
        self.img_cost_6.setGeometry(QtCore.QRect(540, 200, 40, 31))
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.img_cost_6.setFont(font)
        self.img_cost_6.setObjectName("characteristic")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")
        self.img_cost_6.addItem("")

        self.Die_box = QtWidgets.QCheckBox(self.centralwidget)
        self.Die_box.setGeometry(QtCore.QRect(700, 130, 82, 23))


        font.setPointSize(11)
        self.Die_box.setFont(font)
        self.Die_box.setObjectName("Die_box")
        self.Die_box.setText("Die box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 22))
        self.menubar.setObjectName("menubar")
        self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com = QtWidgets.QMenu(self.menubar)
        self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com.setObjectName("menuQuestions_Contact_me_dereinzigefuer_protonmail_com")
        self.menudereinzigefuer_protonmail_com = QtWidgets.QMenu(self.menubar)
        self.menudereinzigefuer_protonmail_com.setObjectName("menudereinzigefuer_protonmail_com")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com.addSeparator()
        self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com.addSeparator()
        self.menubar.addAction(self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com.menuAction())
        self.menubar.addAction(self.menudereinzigefuer_protonmail_com.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.file_select.clicked.connect(self.setImage)
        self.pushButton.clicked.connect(self.start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.unique.setText(_translate("MainWindow", "UNIQUE"))
        self.pushButton.setText(_translate("MainWindow", "Create"))
        self.card_type.setItemText(0, _translate("MainWindow", "CHARACTER"))
        self.card_type.setItemText(1, _translate("MainWindow", "BATTLEFIELD"))
        self.card_type.setItemText(2, _translate("MainWindow", "EVENT"))
        self.card_type.setItemText(3, _translate("MainWindow", "DOWNGRADE"))
        self.card_type.setItemText(4, _translate("MainWindow", "PLOT"))
        self.card_type.setItemText(5, _translate("MainWindow", "SUPPORT"))
        self.card_type.setItemText(6, _translate("MainWindow", "UPGRADE"))
        self.label.setText(_translate("MainWindow", "I WANT TO BUILD"))
        self.label_2.setText(_translate("MainWindow", "Subtitle"))
        self.label_3.setText(_translate("MainWindow", "Subtype"))
        self.subtitle.setPlainText(_translate("MainWindow", "Subtitle"))
        self.subtype.setPlainText(_translate("MainWindow", "Subtype"))
        self.label_4.setText(_translate("MainWindow", "Health"))
        self.category.setItemText(0, _translate("MainWindow", "Hero"))
        self.category.setItemText(1, _translate("MainWindow", "Villain"))
        self.category.setItemText(2, _translate("MainWindow", "Neutral"))
        self.color.setItemText(0, _translate("MainWindow", "Blue"))
        self.color.setItemText(1, _translate("MainWindow", "Red"))
        self.color.setItemText(2, _translate("MainWindow", "Yellow"))
        self.color.setItemText(3, _translate("MainWindow", "Grey"))
        self.color.setItemText(4, _translate("MainWindow", "Green"))
        self.card_type_4.setItemText(0, _translate("MainWindow", "Common"))
        self.card_type_4.setItemText(1, _translate("MainWindow", "Uncommon"))
        self.card_type_4.setItemText(2, _translate("MainWindow", "Rare"))
        self.card_type_4.setItemText(3, _translate("MainWindow", "LEGENDARY"))
        self.label_5.setText(_translate("MainWindow", "Points"))
        self.label_6.setText(_translate("MainWindow", "Elite points"))
        self.text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">text\\description</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\';\">Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į ı</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\';\">text</span></p></body></html>"))
        self.quote.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\'; font-size:11pt;\">cool epic quote</span></p></body></html>"))
        self.plus_point.setText(_translate("MainWindow", "+"))

        self.img_cost.setItemText(10, _translate("MainWindow", "Ą"))
        self.img_cost.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost.setItemText(9, _translate("MainWindow", "č"))

        self.img_cost_2.setItemText(10, _translate("MainWindow", "Ą"))
        self.img_cost_2.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost_2.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost_2.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost_2.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost_2.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost_2.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost_2.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost_2.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost_2.setItemText(9, _translate("MainWindow", "č"))

        self.img_cost_3.setItemText(10, _translate("MainWindow", "Ą"))
        self.img_cost_3.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost_3.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost_3.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost_3.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost_3.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost_3.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost_3.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost_3.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost_3.setItemText(9, _translate("MainWindow", "č"))

        self.img_cost_4.setItemText(10, _translate("MainWindow", "Ą"))
        self.img_cost_4.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost_4.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost_4.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost_4.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost_4.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost_4.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost_4.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost_4.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost_4.setItemText(9, _translate("MainWindow", "č"))

        self.img_cost_5.setItemText(10, _translate("MainWindow", "Ą"))
        self.img_cost_5.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost_5.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost_5.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost_5.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost_5.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost_5.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost_5.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost_5.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost_5.setItemText(9, _translate("MainWindow", "č"))


        self.img_cost_6.setItemText(1, _translate("MainWindow", "ą"))
        self.img_cost_6.setItemText(2, _translate("MainWindow", "Ć"))
        self.img_cost_6.setItemText(3, _translate("MainWindow", "ć"))
        self.img_cost_6.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.img_cost_6.setItemText(5, _translate("MainWindow", "ĉ"))
        self.img_cost_6.setItemText(6, _translate("MainWindow", "Ċ"))
        self.img_cost_6.setItemText(7, _translate("MainWindow", "ċ"))
        self.img_cost_6.setItemText(8, _translate("MainWindow", "Č"))
        self.img_cost_6.setItemText(9, _translate("MainWindow", "č"))
        self.img_cost_6.setItemText(10, _translate("MainWindow", "Ą"))

        self.characteristic.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic.setItemText(9, _translate("MainWindow", "č"))
        self.plus_point_2.setText(_translate("MainWindow", "+"))
        self.plus_point_3.setText(_translate("MainWindow", "+"))
        self.plus_point_4.setText(_translate("MainWindow", "+"))
        self.plus_point_5.setText(_translate("MainWindow", "+"))
        self.plus_point_6.setText(_translate("MainWindow", "+"))

        self.x_point_1.setText(_translate("MainWindow", "X"))
        self.x_point_2.setText(_translate("MainWindow", "X"))
        self.x_point_3.setText(_translate("MainWindow", "X"))
        self.x_point_4.setText(_translate("MainWindow", "X"))
        self.x_point_5.setText(_translate("MainWindow", "X"))
        self.x_point_6.setText(_translate("MainWindow", "X"))

        self.file_select.setText(_translate("MainWindow", "Select image"))
        self.card_name.setPlainText(_translate("MainWindow", "Set card name"))
        self.autor_name.setPlainText(_translate("MainWindow", "Set autor name"))
        self.characteristic_2.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic_2.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic_2.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic_2.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic_2.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic_2.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic_2.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic_2.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic_2.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic_2.setItemText(9, _translate("MainWindow", "č"))
        self.characteristic_3.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic_3.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic_3.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic_3.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic_3.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic_3.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic_3.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic_3.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic_3.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic_3.setItemText(9, _translate("MainWindow", "č"))
        self.characteristic_4.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic_4.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic_4.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic_4.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic_4.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic_4.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic_4.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic_4.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic_4.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic_4.setItemText(9, _translate("MainWindow", "č"))
        self.characteristic_5.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic_5.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic_5.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic_5.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic_5.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic_5.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic_5.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic_5.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic_5.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic_5.setItemText(9, _translate("MainWindow", "č"))
        self.characteristic_6.setItemText(0, _translate("MainWindow", "Ą"))
        self.characteristic_6.setItemText(1, _translate("MainWindow", "ą"))
        self.characteristic_6.setItemText(2, _translate("MainWindow", "Ć"))
        self.characteristic_6.setItemText(3, _translate("MainWindow", "ć"))
        self.characteristic_6.setItemText(4, _translate("MainWindow", "Ĉ"))
        self.characteristic_6.setItemText(5, _translate("MainWindow", "ĉ"))
        self.characteristic_6.setItemText(6, _translate("MainWindow", "Ċ"))
        self.characteristic_6.setItemText(7, _translate("MainWindow", "ċ"))
        self.characteristic_6.setItemText(8, _translate("MainWindow", "Č"))
        self.characteristic_6.setItemText(9, _translate("MainWindow", "č"))
        self.menuQuestions_Contact_me_dereinzigefuer_protonmail_com.setTitle(_translate("MainWindow", "Questions? Contact me:"))
        self.menudereinzigefuer_protonmail_com.setTitle(_translate("MainWindow", "georgiy-egor.burdin@mail.ru"))

    def start(self):
        fileName=filename

        if fileName:  # If the user gives a file

            image = Image.open(fileName)

            if self.Die_box.isChecked() == True:
                if self.card_type.currentText() == "BATTLEFIELD":
                    if self.color.currentText() == 'Red':
                        typ = Image.open('Templates/Battlefields/Red BF With Die.png')
                    elif self.color.currentText() == 'Blue':
                        typ = Image.open('Templates/Battlefields/Blue BF With Die.png')
                    elif self.color.currentText() == 'Yellow':
                        typ = Image.open('Templates/Battlefields/Yellow BF With Die.png')
                    elif self.color.currentText() == 'Grey':
                        typ = Image.open('Templates/Battlefields/Grey BF With Die.png')
                    elif self.color.currentText() == 'Green':
                        typ = Image.open('Templates/Battlefields/Green BF With Die.png')

                    place_die = (20, 35)
                    place_hero = (413, 664)
                    place = (0, 0)
                    fon = Image.new('RGB', (1000, 705))
                else:

                    if self.card_type.currentText() == "CHARACTER":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Chars/Red Char With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Chars/Blue Char With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Chars/Yellow Char With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Chars/Grey Char With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Chars/Green Char No Die.png')
                        place = (0, 0)
                        place_die = (13, 530)
                        place_cost = (565, 75)
                        place_hero = (126, 952)
                    if self.card_type.currentText() == "DOWNGRADE":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Downgrades/Red Downgrade With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Downgrades/Blue Downgrade With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Downgrades/Yellow Downgrade With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Downgrades/Grey Downgrade With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Downgrades/Green Downgrade With Die.png')
                        place = (0, 450)
                        place_cost = (45, 75)
                        place_die = (12, 590)
                        place_hero = (126, 952)
                    if self.card_type.currentText() == "EVENT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Events/Red Event With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Events/Blue Event With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Events/Yellow Event With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Events/Grey Event With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Events/Green Event With Die.png')
                        place = (0, 0)
                        place_cost = (40, 70)
                        place_die = (589, 20)
                        place_hero = (126, 952)
                    if self.card_type.currentText() == "PLOT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Plots/Red Plot With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Plots/Blue Plot With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Plots/Yellow Plot With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Plots/Grey Plot With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Plots/Green Plot With Die.png')
                        place = (0, 0)
                        place_cost = (25, 905)
                        place_die = (588, 20)
                        place_hero = (129, 950)
                    if self.card_type.currentText() == "SUPPORT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Support/Red Support With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Support/Blue Support With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Support/Yellow Support With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Support/Grey Support With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Support/Green Support With Die.png')
                        place = (0, 0)
                        place_cost = (40, 70)
                        place_die = (588, 20)
                        place_hero = (127, 953)
                    if self.card_type.currentText() == "UPGRADE":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Upgrades/Red Upgrade With Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Upgrades/Blue Upgrade With Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Upgrades/Yellow Upgrade With Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Upgrades/Grey Upgrade With Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Upgrades/Green Upgrade With Die.png')
                        place = (0, 0)
                        place_die = (16, 603)
                        place_cost = (40, 70)
                        place_hero = (126, 952)


                    fon = Image.new('RGB', (705, 1000))
            else:
                if self.card_type.currentText() == "BATTLEFIELD":
                    if self.color.currentText() == 'Red':
                        typ = Image.open('Templates/Battlefields/Red BF No Die.png')
                    elif self.color.currentText() == 'Blue':
                        typ = Image.open('Templates/Battlefields/Blue BF No Die.png')
                    elif self.color.currentText() == 'Yellow':
                        typ = Image.open('Templates/Battlefields/Yellow BF No Die.png')
                    elif self.color.currentText() == 'Grey':
                        typ = Image.open('Templates/Battlefields/Grey BF No Die.png')
                    elif self.color.currentText() == 'Green':
                        typ = Image.open('Templates/Battlefields/Green BF No Die.png')

                    place_hero = (413, 664)
                    place = (0, 0)

                    fon = Image.new('RGB', (1000, 705))
                else:
                    fon = Image.new('RGB', (705, 1000))
                    if self.card_type.currentText() == "CHARACTER":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Chars/Red Char No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Chars/Blue Char No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Chars/Yellow Char No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Chars/Grey Char No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Chars/Green Char No Die.png')
                        place = (0, 0)
                        place_cost = (565, 75)
                        place_hero = (126, 952)

                    if self.card_type.currentText() == "DOWNGRADE":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Downgrades/Red Downgrade No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Downgrades/Blue Downgrade No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Downgrades/Yellow Downgrade No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Downgrades/Grey Downgrade No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Downgrades/Green Downgrade No Die.png')
                        place = (0, 450)
                        place_cost = (45, 75)
                        place_hero = (126, 952)

                    if self.card_type.currentText() == "EVENT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Events/Red Event No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Events/Blue Event No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Events/Yellow Event No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Events/Grey Event No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Events/Green Event No Die.png')
                        place = (0, 0)
                        place_cost = (40, 70)
                        place_hero = (126, 952)

                    if self.card_type.currentText() == "PLOT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Plots/Red Plot No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Plots/Blue Plot No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Plots/Yellow Plot No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Plots/Grey Plot No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Plots/Green Plot No Die.png')
                        place = (0, 0)
                        place_cost = (25, 905)
                        place_hero = (129, 950)

                    if self.card_type.currentText() == "SUPPORT":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Support/Red Support No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Support/Blue Support No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Support/Yellow Support No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Support/Grey Support No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Support/Green Support No Die.png')
                        place = (0, 0)
                        place_cost = (40, 70)
                        place_hero = (127, 953)

                    if self.card_type.currentText() == "UPGRADE":
                        if self.color.currentText() == 'Red':
                            typ = Image.open('Templates/Upgrades/Red Upgrade No Die.png')
                        elif self.color.currentText() == 'Blue':
                            typ = Image.open('Templates/Upgrades/Blue Upgrade No Die.png')
                        elif self.color.currentText() == 'Yellow':
                            typ = Image.open('Templates/Upgrades/Yellow Upgrade No Die.png')
                        elif self.color.currentText() == 'Grey':
                            typ = Image.open('Templates/Upgrades/Grey Upgrade No Die.png')
                        elif self.color.currentText() == 'Green':
                            typ = Image.open('Templates/Upgrades/Green Upgrade No Die.png')
                        place = (0, 0)
                        place_cost = (40, 70)
                        place_hero = (126, 952)

            if self.category.currentText() == 'Hero':
                hero = Image.open('Templates/Symbology and Misc/HERO.png')
            elif self.category.currentText() == 'Villain':
                hero = Image.open('Templates/Symbology and Misc/VILLAIN.png')
            elif self.category.currentText() == 'Neutral':
                hero = Image.open('Templates/Symbology and Misc/NEUTRAL.png')

            dies = [0, 1, 2, 3, 4, 5]
            dies[0] = characteristic_img(self.characteristic)
            dies[1] = characteristic_img(self.characteristic_2)
            dies[2] = characteristic_img(self.characteristic_3)
            dies[3] = characteristic_img(self.characteristic_4)
            dies[4] = characteristic_img(self.characteristic_5)
            dies[5] = characteristic_img(self.characteristic_6)
            cost_imgs = [0, 1, 2, 3, 4, 5]
            cost_imgs[0] = costs_img(self.img_cost)
            cost_imgs[1] = costs_img(self.img_cost_2)
            cost_imgs[2] = costs_img(self.img_cost_3)
            cost_imgs[3] = costs_img(self.img_cost_4)
            cost_imgs[4] = costs_img(self.img_cost_5)
            cost_imgs[5] = costs_img(self.img_cost_6)
            values = [0, 1, 2, 3, 4, 5]
            values[0] = str(self.value.value())
            values[1] = str(self.value_2.value())
            values[2] = str(self.value_3.value())
            values[3] = str(self.value_4.value())
            values[4] = str(self.value_5.value())
            values[5] = str(self.value_6.value())
            costs = [0, 1, 2, 3, 4, 5]
            costs[0] = str(self.cost.value())
            costs[1] = str(self.cost_2.value())
            costs[2] = str(self.cost_3.value())
            costs[3] = str(self.cost_4.value())
            costs[4] = str(self.cost_5.value())
            costs[5] = str(self.cost_6.value())
            plus_points = [0, 1, 2, 3, 4, 5]
            plus_points[0] = self.plus_point.isChecked()
            plus_points[1] = self.plus_point_2.isChecked()
            plus_points[2] = self.plus_point_3.isChecked()
            plus_points[3] = self.plus_point_4.isChecked()
            plus_points[4] = self.plus_point_5.isChecked()
            plus_points[5] = self.plus_point_6.isChecked()
            x_points = [0, 1, 2, 3, 4, 5]
            x_points[0] = self.x_point_1.isChecked()
            x_points[1] = self.x_point_2.isChecked()
            x_points[2] = self.x_point_3.isChecked()
            x_points[3] = self.x_point_4.isChecked()
            x_points[4] = self.x_point_5.isChecked()
            x_points[5] = self.x_point_6.isChecked()
            if self.subtype.toPlainText()!="":
                type_subtype=self.card_type.currentText() + ' - ' + self.subtype.toPlainText()
            else:
                type_subtype = self.card_type.currentText()
            font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 35)
            font_text = ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 20)
            i = 0
            draw = ImageDraw.Draw(fon)
            add_image(fon, image, place)
            add_image(fon, typ, (0, 0))

            if self.Die_box.isChecked() == True:
                font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 35)
                if self.card_type.currentText()=="DOWNGRADE" or self.card_type.currentText()=="BATTLEFIELD":
                    k=59
                else:
                    k=60
                for die in dies:
                    if die == 'Templates/Symbology and Misc/Blank Die Fill.png':

                        place_box = (place_die[0], place_die[1]+4 + i * k)
                        img_box = Image.open(die)
                        img_box=resize(img_box,98,65)
                        add_image(fon, img_box, place_box)
                        i = i + 1
                    elif plus_points[i] == True and costs[i] == '0':
                        place_box = (place_die[0] + 60, place_die[1] + 17 + i * k)
                        img_box = Image.open(die)
                        img_box = resize(img_box, 20, 20)
                        if x_points[i]==True:
                            number="X"
                        else:
                            number = values[i]
                        draw.rectangle((place_die[0], place_die[1] + 4 + i * k, place_die[0] + 97,
                                        place_die[1] + 4 + i * k + 57), fill=(6, 76, 162))
                        draw.text(
                            (place_die[0] + 55 - draw.textsize(number, font_numbers)[0], place_die[1] + 15 + i * k),
                            number, (255, 255, 255), font=font_numbers, align='right')
                        draw.text((place_die[0] + 51 - draw.textsize(number, font_numbers)[0] -
                                   draw.textsize('+', font_numbers)[0], place_die[1] + 15 + i * k),
                                  '+', (255, 255, 255), font=font_numbers, align='right')
                        add_image(fon, img_box, place_box)
                        i = i + 1
                    elif plus_points[i] == True and costs[i] != '0':
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 23)
                        place_box = (place_die[0] + 60, place_die[1] + 10 + i * k)
                        img_box = Image.open(die)
                        img_box = resize(img_box, 23, 23)
                        if x_points[i] == True:
                            number = "X"
                        else:
                            number = values[i]
                        draw.rectangle((place_die[0], place_die[1] + 4 + i * k, place_die[0] + 97,
                                        place_die[1] + 4 + i * k + 57), fill=(6, 76, 162))
                        draw.text(
                            (place_die[0] + 55 - draw.textsize(number, font_numbers)[0], place_die[1] + 10 + i * k),
                            number, (255, 255, 255), font=font_numbers, align='right')
                        draw.text((place_die[0] + 51 - draw.textsize(number, font_numbers)[0] -
                                   draw.textsize('+', font_numbers)[0], place_die[1] + 10 + i * k),
                                  '+', (255, 255, 255), font=font_numbers, align='right')
                        add_image(fon, img_box, place_box)
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 21)
                        place_box = (place_die[0] + 50, place_die[1] + 35 + i * k)
                        img_box = Image.open(cost_imgs[i])
                        img_box = resize(img_box, 18, 18)
                        number = costs[i]
                        draw.text(
                            (place_die[0] + 45 - draw.textsize(number, font_numbers)[0], place_die[1] + 35 + i * k),
                            number, (235,201,79), font=font_numbers, align='right',)
                        add_image(fon, img_box, place_box)
                        i = i + 1
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 35)
                    elif plus_points[i] != True and costs[i] != '0':
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 26)
                        place_box = (place_die[0] + 50, place_die[1] + 10 + i * k)
                        img_box = Image.open(die)
                        img_box = resize(img_box, 23, 23)
                        if x_points[i] == True:
                            number = "X"
                        else:
                            number = values[i]

                        draw.text(
                            (place_die[0] + 45 - draw.textsize(number, font_numbers)[0], place_die[1] + 10 + i * k),
                            number, (255, 255, 255), font=font_numbers, align='right')

                        add_image(fon, img_box, place_box)
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 21)
                        place_box = (place_die[0] + 50, place_die[1] + 35 + i * k)
                        img_box = Image.open(cost_imgs[i])
                        img_box = resize(img_box, 18, 18)
                        number = costs[i]
                        draw.text(
                            (place_die[0] + 45 - draw.textsize(number, font_numbers)[0], place_die[1] + 35 + i * k),
                            number, (235,201,79), font=font_numbers, align='right',)
                        add_image(fon, img_box, place_box)
                        i = i + 1
                        font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 35)
                    else:
                        place_box = (place_die[0] + 50, place_die[1] + 17 + i * k)
                        img_box = Image.open(die)
                        img_box = resize(img_box, 23, 23)
                        if x_points[i] == True:
                            number = "X"
                        else:
                            number = values[i]
                        draw.text(
                            (place_die[0] + 45 - draw.textsize(number, font_numbers)[0], place_die[1] + 15 + i * k),
                            number, (255, 255, 255), font=font_numbers, align='right')
                        add_image(fon, img_box, place_box)
                        i = i + 1
            if self.card_type.currentText() != "BATTLEFIELD":
                number = str(self.health.value())

                if self.card_type.currentText() == "PLOT":
                    font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 30)
                    color_cost = (0, 0, 0)
                    draw.text((place_cost[0] + 5, place_cost[1] + 25), number, color_cost, font=font_numbers)
                elif self.card_type.currentText() == 'CHARACTER':

                    font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 60)
                    color_cost = (255, 255, 255)
                    draw.text(
                        (place_cost[0] + 45 - draw.textsize(number, font=font_numbers)[0] / 2, place_cost[1] + 25),
                        number, color_cost, font=font_numbers)
                else:
                    font_numbers = ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 45)
                    color_cost = (0, 0, 0)
                    draw.text((130 -
                               draw.textsize('E', font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 30))[0],
                               place_cost[1] + 25), 'E', color_cost,
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 30))
                    draw.text((130 -
                               draw.textsize('E', font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 30))[
                                   0] - draw.textsize(number, font=font_numbers)[0], place_cost[1] + 25), number,
                              color_cost, font=font_numbers)

                fon.save(self.card_name.toPlainText() + '.png')
            if self.elite_points.value()!=0:
                points = str(self.points.value()) + '/' + str(self.elite_points.value())
            else:
                points = str(self.points.value())
            if self.card_type.currentText() == "CHARACTER" and self.Die_box.isChecked() == True:
                draw.text((10, 944), points,
                          (0, 0, 0), font=ImageFont.truetype("Templates/Fonts/Eurostile Font for numbers.ttf", 25))
                place_quote = (135, 730 + draw.textsize(self.text.toPlainText(), font=font_text)[1])
                place_text = (135, 700)
            elif self.card_type.currentText() == "CHARACTER" and self.Die_box.isChecked() != True:
                place_quote = (35, 730 + draw.textsize(self.text.toPlainText(), font=font_text)[1])
                place_text = (35, 700)

            if self.card_type.currentText() == "BATTLEFIELD":
                place_name = (350, 50, 300, 70)
                place_description = (120, 500, 750, 120)
                place_autor = (585, 665, 260, 25)
                place_freq = (857, 646)
                if self.unique.isChecked() == True:
                    draw.text((460 - 35 - draw.textsize(self.card_name.toPlainText())[0] / 2, 40),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((460 - draw.textsize(self.card_name.toPlainText())[0] / 2, 40),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')
                draw.multiline_text(
                    (480 - draw.textsize(self.subtitle.toPlainText())[0] / 2, 90),
                    self.subtitle.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30), align='center')

                draw.multiline_text(
                    (585, 664),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (120, 500),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35))
            if self.card_type.currentText() == "CHARACTER":
                place_name = (210, 50)
                place_description = (135, 650)
                place_autor = (305, 955)
                place_freq = (575, 932)
                if self.unique.isChecked() == True:
                    draw.text((345 - 35 - draw.textsize(self.card_name.toPlainText())[0], 50),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((345 - draw.textsize(self.card_name.toPlainText())[0], 50),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')
                draw.multiline_text(
                    (335 - draw.textsize(self.subtitle.toPlainText())[0] / 2, 90),
                    self.subtitle.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30), align='center')
                draw.multiline_text(
                    (305, 953),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (375 - draw.textsize(type_subtype)[0], 660),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    place_text,
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    place_quote,
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
            if self.card_type.currentText() == "DOWNGRADE":
                place_name = ()
                place_description = ()
                place_autor = ()
                place_hero = (133, 942)
                place_freq = (573, 925)
                if self.unique.isChecked() == True:
                    draw.text((265 - draw.textsize(self.card_name.toPlainText())[0]/2, 55),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((300 - draw.textsize(self.card_name.toPlainText())[0] / 2, 55),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')

                draw.multiline_text(
                    (310, 945),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (345 - draw.textsize(type_subtype)[0], 155),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    (70, 210),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    (70, 230 + draw.textsize(self.text.toPlainText(), font=font_text)[1]),
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
            if self.card_type.currentText() == "EVENT":
                place_name = ()
                place_description = ()
                place_autor = ()
                place_hero = (126, 955)
                place_freq = (575, 940)
                if self.unique.isChecked() == True:
                    draw.text((335 - 35 - draw.textsize(type_subtype)[0], 595),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((335 - draw.textsize(self.card_name.toPlainText())[0], 595),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')

                draw.multiline_text(
                    (305, 953),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (335 - draw.textsize(type_subtype)[0], 715),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    (70, 760),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    (70, 800 + draw.textsize(self.text.toPlainText(), font=font_text)[1]),
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
            if self.card_type.currentText() == "PLOT":
                place_name = ()
                place_description = ()
                place_autor = ()
                place_freq = (575, 932)
                if self.unique.isChecked() == True:
                    draw.text((295 - draw.textsize(self.card_name.toPlainText())[0], 522),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((330 - draw.textsize(self.card_name.toPlainText())[0], 522),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')

                draw.multiline_text(
                    (305, 951),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (340 - draw.textsize(type_subtype)[0], 655),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    (70, 700),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    (70, 750 + draw.textsize(self.text.toPlainText(), font=font_text)[1]),
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
            if self.card_type.currentText() == "SUPPORT":
                place_name = ()
                place_description = ()
                place_autor = ()
                place_freq = (575, 938)
                place_hero = (126, 956)
                if self.unique.isChecked() == True:
                    draw.text((295 - draw.textsize(self.card_name.toPlainText())[0], 80),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))
                draw.multiline_text((330 - draw.textsize(self.card_name.toPlainText())[0], 80),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')
                draw.multiline_text(
                    (330 - draw.textsize(self.subtitle.toPlainText())[0] / 2, 120),
                    self.subtitle.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30), align='center')
                draw.multiline_text(
                    (305, 955),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (340 - draw.textsize(type_subtype)[0], 660),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    (135, 700),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    (135, 730 + draw.textsize(self.text.toPlainText(), font=font_text)[1]),
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
            if self.card_type.currentText() == "UPGRADE":
                place_name = ()
                place_freq = (575, 939)
                place_description = ()
                place_autor = ()
                place_hero = (126, 956)
                if self.unique.isChecked() == True:
                    draw.text((345 - 35 - draw.textsize(self.card_name.toPlainText())[0], 560),
                              'o', (0, 0, 0),
                              font=ImageFont.truetype("Templates/Fonts/Symbology Font.ttf", 40))

                draw.multiline_text((345 - draw.textsize(self.card_name.toPlainText())[0], 560),
                                    self.card_name.toPlainText(), (0, 0, 0),
                                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 40),
                                    align='center')

                draw.multiline_text(
                    (305, 955),
                    self.autor_name.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 22), align='center')
                draw.multiline_text(
                    (340 - draw.textsize(type_subtype)[0], 660),
                    type_subtype, (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 35), align='center')
                draw.multiline_text(
                    (135, 700),
                    self.text.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))
                draw.multiline_text(
                    (135, 730 + draw.textsize(self.text.toPlainText(), font=font_text)[1]),
                    self.quote.toPlainText(), (0, 0, 0),
                    font=ImageFont.truetype("Templates/Fonts/Agency Font for Letters.ttf", 30))

            if self.card_type_4.currentText() == 'LEGENDARY':
                freq = Image.open('Templates/freq/Legendary.png')
            if self.card_type_4.currentText() == 'Rare':
                freq = Image.open('Templates/freq/Rare.png')
            if self.card_type_4.currentText() == 'Uncommon':
                freq = Image.open('Templates/freq/Uncommom.png')
            if self.card_type_4.currentText() == 'Common':
                freq = Image.open('Templates/freq/Commom.png')
            add_image(fon, freq, place_freq)

            add_image(fon, hero, place_hero)
            if self.card_type.currentText() != "BATTLEFIELD" and self.card_type.currentText() != "DOWNGRADE" and self.card_type.currentText() != "EVENT" and self.card_type.currentText() != "UPGRADE" and self.card_type.currentText() != "SUPPORT":
                draw.text((240, 950), self.color.currentText(), (0, 0, 0), font=font_text)
            if self.card_type.currentText() == "BATTLEFIELD":
                draw.text((525, 663), self.color.currentText(), (0, 0, 0), font=font_text)
            if self.card_type.currentText() == "DOWNGRADE":
                draw.text((240, 940), self.color.currentText(), (0, 0, 0), font=font_text)
            if self.card_type.currentText() == "EVENT" or self.card_type.currentText() == "UPGRADE" or self.card_type.currentText() == "SUPPORT":
                draw.text((235, 957), self.color.currentText(), (0, 0, 0), font=font_text)

            fon.save(self.card_name.toPlainText() + '.png')

    def setImage(self):

        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png)")  # Ask for file
        global filename
        filename = self.fileName

        if filename:
            pixmap = QtGui.QPixmap(filename)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imagelbl.width(), self.imagelbl.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.imagelbl.setPixmap(pixmap)  # Set the pixmap onto the label
            self.imagelbl.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center


