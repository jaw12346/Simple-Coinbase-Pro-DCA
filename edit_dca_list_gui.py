# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_dca_list.ui'
#
# Created by: PyQt5 UI code generator 5.9.2

from PyQt5 import QtCore, QtGui, QtWidgets
import validation


class Ui_dca_list_dialog(object):
    def setupUi(self, dca_list_dialog, parent=None):
        self.parent = parent  # `parent` of list editor is API setup window
        dca_list_dialog.setObjectName("dca_list_dialog")
        dca_list_dialog.resize(320, 240)
        self.dca_list = QtWidgets.QListWidget(dca_list_dialog)
        self.dca_list.setGeometry(QtCore.QRect(10, 20, 211, 192))
        self.dca_list.setObjectName("dca_list")
        self.verticalLayoutWidget = QtWidgets.QWidget(dca_list_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 20, 77, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dca_buttons_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dca_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.dca_buttons_layout.setObjectName("dca_buttons_layout")

        self.add_dca_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_dca_button.setObjectName("add_dca_button")
        self.dca_buttons_layout.addWidget(self.add_dca_button)

        self.add_dca_button.clicked.connect(self.open_new_dca_window)

        self.edit_dca_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_dca_button.setObjectName("edit_dca_button")
        self.dca_buttons_layout.addWidget(self.edit_dca_button)

        self.edit_dca_button.clicked.connect(self.edit_dca_item)  # Call for edit of selected entry

        self.remove_dca_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_dca_button.setObjectName("remove_dca_button")
        self.dca_buttons_layout.addWidget(self.remove_dca_button)

        self.remove_dca_button.clicked.connect(self.remove_dca_item)  # Call for removal of selected entry

        self.save_list_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_list_button.setDefault(True)
        self.save_list_button.setObjectName("save_list_button")
        self.dca_buttons_layout.addWidget(self.save_list_button)

        self.retranslateUi(dca_list_dialog)
        QtCore.QMetaObject.connectSlotsByName(dca_list_dialog)

    def retranslateUi(self, dca_list_dialog):
        _translate = QtCore.QCoreApplication.translate
        dca_list_dialog.setWindowTitle(_translate("dca_list_dialog", "DCA List Editor"))
        self.add_dca_button.setText(_translate("dca_list_dialog", "Add"))
        self.edit_dca_button.setText(_translate("dca_list_dialog", "Edit"))
        self.remove_dca_button.setText(_translate("dca_list_dialog", "Remove"))
        self.save_list_button.setText(_translate("dca_list_dialog", "Save and Exit"))

    def open_new_dca_window(self):  # Open new DCA window
        from add_dca_gui import Ui_add_dca_dialog  # Prevents circular import for adding to dca list
        self.dialog_window = QtWidgets.QDialog()
        self.dialog_ui = Ui_add_dca_dialog()
        self.dialog_ui.setupUi(self.dialog_window, parent=self)  # `parent` declares the list window as parent
        self.dialog_window.setModal(True)  # Force the dialog to be the only interactable window
        self.dialog_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # Remove the title bar
        self.dialog_window.setFocus()  # Force placeholder text to appear
        self.dialog_window.show()

    def add_new_dca(self, base_currency, quote_currency, amount):
        value = f"${amount} {quote_currency} -> {base_currency}"
        response = validation.validate_new_dca(base_currency, quote_currency, amount)
        if response[0] == 1 and response[1] == 1:
            self.dca_list.addItem(value)
            self.dialog_window.close()
        else:
            self.fail_dca(response)

    def fail_dca(self, failed):
        if failed[1] == 0:
            self.dialog_ui.quote_amount_input.setStyleSheet("QSpinBox { border: 1px solid red;}")
            if failed[0] == 1:
                self.dialog_ui.base_currency_input.setStyleSheet("QLineEdit { border: 1px solid green;}")
                self.dialog_ui.quote_currency_input.setStyleSheet("QLineEdit { border: 1px solid green;}")
        if failed[0] == 0:
            self.dialog_ui.base_currency_input.setStyleSheet("QLineEdit { border: 1px solid red;}")
            self.dialog_ui.quote_currency_input.setStyleSheet("QLineEdit { border: 1px solid red;}")

    def remove_dca_item(self):
        for item in self.dca_list.selectedItems():
            self.dca_list.takeItem(self.dca_list.row(item))

    def edit_dca_item(self):
        item = self.dca_list.currentItem()
        if item is None:
            return
        text = item.text()
        amount = float((text.split(' ')[0]).split('$')[1])
        quote_currency = text.split(' ')[1]
        base_currency = text.split(' ')[-1]
        self.open_edit_window(amount, quote_currency, base_currency)

    def open_edit_window(self, amount, quote_currency, base_currency):
        from add_dca_gui import Ui_add_dca_dialog  # Prevents circular import for adding to dca list
        self.dialog_window = QtWidgets.QDialog()
        self.dialog_ui = Ui_add_dca_dialog()
        self.dialog_ui.setupUi(self.dialog_window, parent=self)  # `parent` declares the list window as parent
        self.dialog_window.setModal(True)  # Force the dialog to be the only interactable window
        self.dialog_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # Remove the title bar

        # Fill in fields with previous data to be edited
        self.dialog_ui.base_currency_input.insert(base_currency)
        self.dialog_ui.quote_currency_input.insert(quote_currency)
        self.dialog_ui.quote_amount_input.setValue(amount)

        self.dialog_window.setFocus()  # Force placeholder text to appear
        self.dialog_window.show()

        self.dialog_ui.confirm_add_button.clicked.connect(self.remove_dca_item)  # Remove old instance upon saving
