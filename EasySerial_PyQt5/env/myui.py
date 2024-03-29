# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{background: #d9a7c7;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(217, 167, 199), stop:1 rgb(255, 252, 220));}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.RX = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RX.setFont(font)
        self.RX.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RX.setStyleSheet("QGroupBox{border:1px solid #00917C;border-radius:5px;margin-top:2ex}\n"
"QGroupBox::title{subcontrol-origin:margin;left:10px}")
        self.RX.setFlat(False)
        self.RX.setCheckable(False)
        self.RX.setObjectName("RX")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.RX)
        self.verticalLayout_5.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rxData = QtWidgets.QPlainTextEdit(self.RX)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rxData.setFont(font)
        self.rxData.setReadOnly(True)
        self.rxData.setObjectName("rxData")
        self.verticalLayout_5.addWidget(self.rxData)
        self.horizontalLayout_9.addWidget(self.RX)
        self.ckSet = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckSet.sizePolicy().hasHeightForWidth())
        self.ckSet.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ckSet.setFont(font)
        self.ckSet.setStyleSheet("QGroupBox{border:1px solid #00917C;border-radius:5px;margin-top:2ex}\n"
"QGroupBox::title{subcontrol-origin:margin;left:10px}\n"
"\n"
"")
        self.ckSet.setObjectName("ckSet")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ckSet)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 8, -1, 25)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.scanCK = QtWidgets.QPushButton(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanCK.sizePolicy().hasHeightForWidth())
        self.scanCK.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.scanCK.setFont(font)
        self.scanCK.setStyleSheet("background-color: #FF8A5E;")
        self.scanCK.setObjectName("scanCK")
        self.horizontalLayout_7.addWidget(self.scanCK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.chooseCK = QtWidgets.QComboBox(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseCK.sizePolicy().hasHeightForWidth())
        self.chooseCK.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chooseCK.setFont(font)
        self.chooseCK.setObjectName("chooseCK")
        self.horizontalLayout_8.addWidget(self.chooseCK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.baudRate = QtWidgets.QComboBox(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.baudRate.setFont(font)
        self.baudRate.setObjectName("baudRate")
        self.baudRate.addItem("")
        self.baudRate.addItem("")
        self.horizontalLayout_3.addWidget(self.baudRate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dataBit = QtWidgets.QComboBox(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dataBit.setFont(font)
        self.dataBit.setEditable(False)
        self.dataBit.setObjectName("dataBit")
        self.dataBit.addItem("")
        self.dataBit.addItem("")
        self.horizontalLayout_4.addWidget(self.dataBit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.checkBit = QtWidgets.QComboBox(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBit.setFont(font)
        self.checkBit.setObjectName("checkBit")
        self.checkBit.addItem("")
        self.checkBit.addItem("")
        self.checkBit.addItem("")
        self.horizontalLayout_5.addWidget(self.checkBit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.stopBit = QtWidgets.QComboBox(self.ckSet)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stopBit.setFont(font)
        self.stopBit.setObjectName("stopBit")
        self.stopBit.addItem("")
        self.stopBit.addItem("")
        self.stopBit.addItem("")
        self.horizontalLayout_6.addWidget(self.stopBit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stopRX = QtWidgets.QCheckBox(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopRX.sizePolicy().hasHeightForWidth())
        self.stopRX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.stopRX.setFont(font)
        self.stopRX.setObjectName("stopRX")
        self.verticalLayout_3.addWidget(self.stopRX)
        self.hexRX = QtWidgets.QCheckBox(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexRX.sizePolicy().hasHeightForWidth())
        self.hexRX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hexRX.setFont(font)
        self.hexRX.setObjectName("hexRX")
        self.verticalLayout_3.addWidget(self.hexRX)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.closeCK = QtWidgets.QPushButton(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeCK.sizePolicy().hasHeightForWidth())
        self.closeCK.setSizePolicy(sizePolicy)
        self.closeCK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeCK.setObjectName("closeCK")
        self.verticalLayout.addWidget(self.closeCK)
        self.openCK = QtWidgets.QPushButton(self.ckSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openCK.sizePolicy().hasHeightForWidth())
        self.openCK.setSizePolicy(sizePolicy)
        self.openCK.setObjectName("openCK")
        self.verticalLayout.addWidget(self.openCK)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.setStretch(0, 4)
        self.verticalLayout_6.setStretch(1, 1)
        self.horizontalLayout_9.addWidget(self.ckSet)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.TX = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TX.setFont(font)
        self.TX.setStyleSheet("QGroupBox{border:1px solid #00917C;border-radius:5px;margin-top:2ex}\n"
"QGroupBox::title{subcontrol-origin:margin;left:10px}")
        self.TX.setObjectName("TX")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TX)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txData = QtWidgets.QPlainTextEdit(self.TX)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.txData.setFont(font)
        self.txData.setObjectName("txData")
        self.horizontalLayout.addWidget(self.txData)
        self.line_2 = QtWidgets.QFrame(self.TX)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hexTX = QtWidgets.QCheckBox(self.TX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexTX.sizePolicy().hasHeightForWidth())
        self.hexTX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hexTX.setFont(font)
        self.hexTX.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.hexTX.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hexTX.setObjectName("hexTX")
        self.verticalLayout_2.addWidget(self.hexTX)
        self.clearTX = QtWidgets.QPushButton(self.TX)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.clearTX.setFont(font)
        self.clearTX.setObjectName("clearTX")
        self.verticalLayout_2.addWidget(self.clearTX)
        self.openFile = QtWidgets.QPushButton(self.TX)
        self.openFile.setObjectName("openFile")
        self.verticalLayout_2.addWidget(self.openFile)
        self.send = QtWidgets.QPushButton(self.TX)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send.sizePolicy().hasHeightForWidth())
        self.send.setSizePolicy(sizePolicy)
        self.send.setSizeIncrement(QtCore.QSize(0, 0))
        self.send.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setIconSize(QtCore.QSize(20, 20))
        self.send.setCheckable(False)
        self.send.setObjectName("send")
        self.verticalLayout_2.addWidget(self.send)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addWidget(self.TX)
        self.verticalLayout_7.setStretch(0, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口助手"))
        self.RX.setTitle(_translate("MainWindow", "接收区"))
        self.ckSet.setTitle(_translate("MainWindow", "串口设置"))
        self.label_5.setText(_translate("MainWindow", "串口检测："))
        self.scanCK.setText(_translate("MainWindow", "检测串口"))
        self.label_6.setText(_translate("MainWindow", "端口选择："))
        self.label.setText(_translate("MainWindow", "波特率："))
        self.baudRate.setItemText(0, _translate("MainWindow", "115200"))
        self.baudRate.setItemText(1, _translate("MainWindow", "9600"))
        self.label_4.setText(_translate("MainWindow", "数据位："))
        self.dataBit.setCurrentText(_translate("MainWindow", "8"))
        self.dataBit.setItemText(0, _translate("MainWindow", "8"))
        self.dataBit.setItemText(1, _translate("MainWindow", "7"))
        self.label_2.setText(_translate("MainWindow", "校验位："))
        self.checkBit.setItemText(0, _translate("MainWindow", "无"))
        self.checkBit.setItemText(1, _translate("MainWindow", "奇"))
        self.checkBit.setItemText(2, _translate("MainWindow", "偶"))
        self.label_3.setText(_translate("MainWindow", "停止位："))
        self.stopBit.setItemText(0, _translate("MainWindow", "1"))
        self.stopBit.setItemText(1, _translate("MainWindow", "1.5"))
        self.stopBit.setItemText(2, _translate("MainWindow", "2"))
        self.stopRX.setText(_translate("MainWindow", "停止接收"))
        self.hexRX.setText(_translate("MainWindow", "HEX接收"))
        self.closeCK.setText(_translate("MainWindow", "关闭串口"))
        self.openCK.setText(_translate("MainWindow", "打开串口"))
        self.TX.setTitle(_translate("MainWindow", "发送区"))
        self.hexTX.setText(_translate("MainWindow", "HEX发送"))
        self.clearTX.setText(_translate("MainWindow", "清除发送"))
        self.openFile.setText(_translate("MainWindow", "打开文件"))
        self.send.setText(_translate("MainWindow", "发送"))
