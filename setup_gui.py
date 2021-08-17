# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(682, 300))
        MainWindow.setMaximumSize(QtCore.QSize(682, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 80, 431, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.api_input_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.api_input_layout.setContentsMargins(0, 0, 0, 0)
        self.api_input_layout.setObjectName("api_input_layout")
        self.api_key_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.api_key_label.setFont(font)
        self.api_key_label.setObjectName("api_key_label")
        self.api_input_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.api_key_label)
        self.api_key_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.api_key_input.setFont(font)
        self.api_key_input.setObjectName("api_key_input")
        self.api_input_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.api_key_input)
        self.api_secret_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.api_secret_label.setFont(font)
        self.api_secret_label.setObjectName("api_secret_label")
        self.api_input_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.api_secret_label)
        self.api_secret_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.api_secret_input.setFont(font)
        self.api_secret_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoPredictiveText)
        self.api_secret_input.setText("")
        self.api_secret_input.setObjectName("api_secret_input")
        self.api_input_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.api_secret_input)
        self.api_passphrase_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.api_passphrase_label.setFont(font)
        self.api_passphrase_label.setObjectName("api_passphrase_label")
        self.api_input_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.api_passphrase_label)
        self.api_passphrase_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.api_passphrase_input.setFont(font)
        self.api_passphrase_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoPredictiveText)
        self.api_passphrase_input.setObjectName("api_passphrase_input")
        self.api_input_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.api_passphrase_input)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 90, 187, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.api_type_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.api_type_layout.setContentsMargins(0, 0, 0, 0)
        self.api_type_layout.setObjectName("api_type_layout")
        self.api_type_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.api_type_label.setFont(font)
        self.api_type_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.api_type_label.setObjectName("api_type_label")
        self.api_type_layout.addWidget(self.api_type_label)
        self.market_type_layout = QtWidgets.QHBoxLayout()
        self.market_type_layout.setObjectName("market_type_layout")
        self.market_button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.market_button.setFont(font)
        self.market_button.setChecked(True)
        self.market_button.setObjectName("market_button")
        self.market_type_layout.addWidget(self.market_button)
        self.sandbox_button = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sandbox_button.setFont(font)
        self.sandbox_button.setObjectName("sandbox_button")
        self.market_type_layout.addWidget(self.sandbox_button)
        self.api_type_layout.addLayout(self.market_type_layout)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(0, 10, 679, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 180, 631, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.start_button.setDefault(True)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 0, 3, 1, 1)
        self.edit_configuration_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.edit_configuration_button.setObjectName("edit_configuration_button")
        self.gridLayout.addWidget(self.edit_configuration_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coinbase Pro DCA Setup"))
        self.api_key_label.setText(_translate("MainWindow", "API Key:"))
        self.api_key_input.setPlaceholderText(_translate("MainWindow", "Enter API key from Coinbase Pro"))
        self.api_secret_label.setText(_translate("MainWindow", "API Secret:"))
        self.api_secret_input.setPlaceholderText(_translate("MainWindow", "Enter API secret from Coinbase Pro"))
        self.api_passphrase_label.setText(_translate("MainWindow", "API Passphrase:"))
        self.api_passphrase_input.setPlaceholderText(_translate("MainWindow", "Enter custom API passphrase from Coinbase Pro"))
        self.api_type_label.setText(_translate("MainWindow", "API Type"))
        self.market_button.setText(_translate("MainWindow", "Real Market"))
        self.sandbox_button.setText(_translate("MainWindow", "Sandbox Market"))
        self.title_label.setText(_translate("MainWindow", "Coinbase Pro Dollar-Cost-Averaging"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.edit_configuration_button.setText(_translate("MainWindow", "Edit DCA Purchase List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

