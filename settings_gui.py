# Form implementation generated from reading ui file 'ui/settings.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(909, 429)
        Dialog.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.cam_sets_label = QtWidgets.QLabel(parent=Dialog)
        self.cam_sets_label.setGeometry(QtCore.QRect(20, 10, 300, 65))
        self.cam_sets_label.setMaximumSize(QtCore.QSize(300, 70))
        self.cam_sets_label.setStyleSheet("border: 0px solid rgba(0,0,0,255);")
        self.cam_sets_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.cam_sets_label.setObjectName("cam_sets_label")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 311, 51))
        self.pushButton.setObjectName("pushButton")
        self.group_set_check = QtWidgets.QCheckBox(parent=Dialog)
        self.group_set_check.setGeometry(QtCore.QRect(10, 150, 311, 41))
        self.group_set_check.setObjectName("group_set_check")
        self.auto_set_check = QtWidgets.QCheckBox(parent=Dialog)
        self.auto_set_check.setGeometry(QtCore.QRect(10, 200, 311, 41))
        self.auto_set_check.setObjectName("auto_set_check")
        self.exp_spin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.exp_spin.setGeometry(QtCore.QRect(10, 250, 62, 41))
        self.exp_spin.setObjectName("exp_spin")
        self.gain_spin = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.gain_spin.setGeometry(QtCore.QRect(10, 300, 62, 41))
        self.gain_spin.setObjectName("gain_spin")
        self.fps_spin = QtWidgets.QSpinBox(parent=Dialog)
        self.fps_spin.setGeometry(QtCore.QRect(10, 350, 61, 41))
        self.fps_spin.setObjectName("fps_spin")
        self.exp_label = QtWidgets.QLabel(parent=Dialog)
        self.exp_label.setGeometry(QtCore.QRect(80, 260, 81, 16))
        self.exp_label.setObjectName("exp_label")
        self.gain_label = QtWidgets.QLabel(parent=Dialog)
        self.gain_label.setGeometry(QtCore.QRect(80, 310, 81, 16))
        self.gain_label.setObjectName("gain_label")
        self.fps_label = QtWidgets.QLabel(parent=Dialog)
        self.fps_label.setGeometry(QtCore.QRect(80, 360, 131, 16))
        self.fps_label.setObjectName("fps_label")
        self.set_trigger = QtWidgets.QLabel(parent=Dialog)
        self.set_trigger.setGeometry(QtCore.QRect(330, 10, 300, 65))
        self.set_trigger.setMaximumSize(QtCore.QSize(300, 70))
        self.set_trigger.setStyleSheet("border: 0px solid rgba(0,0,0,255);")
        self.set_trigger.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.set_trigger.setObjectName("set_trigger")
        self.consecration_label = QtWidgets.QLabel(parent=Dialog)
        self.consecration_label.setGeometry(QtCore.QRect(630, 10, 300, 65))
        self.consecration_label.setMaximumSize(QtCore.QSize(300, 70))
        self.consecration_label.setStyleSheet("border: 0px solid rgba(0,0,0,255);")
        self.consecration_label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.consecration_label.setObjectName("consecration_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cam_sets_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Настройка камер</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "cam_model_btn"))
        self.group_set_check.setText(_translate("Dialog", "Групповая настройка"))
        self.auto_set_check.setText(_translate("Dialog", "Автоматическая настройка"))
        self.exp_label.setText(_translate("Dialog", "Экспозиция"))
        self.gain_label.setText(_translate("Dialog", "Усиление"))
        self.fps_label.setText(_translate("Dialog", "Частота кадров, кадр/с"))
        self.set_trigger.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Настройка триггера</span></p></body></html>"))
        self.consecration_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Освещение</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
