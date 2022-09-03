import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer
import serial.tools.list_ports
from myui import *


class PyqtSerial(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(PyqtSerial, self).__init__(parent)
        self.setupUi(self)
        self.ser = None
        self.scanSerial()

        # Button事件绑定
        self.scanCK.clicked.connect(lambda: self.scanSerial())
        self.openCK.clicked.connect(lambda: self.openSerial())
        self.closeCK.clicked.connect(lambda: self.closeSerial())
        self.stopRX.clicked.connect(lambda: self.stopReceive())
        self.send.clicked.connect(lambda: self.dataSend())
        self.clearTX.clicked.connect(lambda: self.dataClear())
        self.openFile.clicked.connect(lambda: self.fileOpen())

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.dataReceive())

    # 键盘监听事件
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    # 串口搜索
    def scanSerial(self):
        self.chooseCK.clear()
        port_list = list(serial.tools.list_ports.comports())
        for i in port_list:
            self.chooseCK.addItem(i.name)

    # 打开串口
    def openSerial(self):
        port = self.chooseCK.currentText()
        baudrate = self.baudRate.currentText()
        bytesize = self.dataBit.currentText()
        checkbit = self.checkBit.currentText()
        stopbit = self.stopBit.currentText()
        if port == '':
            QMessageBox.warning(self, '警告', "请检查串口！", QMessageBox.Ok)
        else:
            try:
                self.ser = serial.Serial(port, int(baudrate), int(bytesize), 'N', int(stopbit))
                print(self.ser)
                self.openCK.setEnabled(False)
                self.closeCK.setEnabled(True)
                self.dataReceive()
            except Exception as e:
                QMessageBox.warning(self, '警告', "请检查串口！", QMessageBox.Ok)
                print(e)

    # 关闭串口
    def closeSerial(self):
        try:
            self.ser.close()
            self.ser = None
            self.openCK.setEnabled(True)
            self.closeCK.setEnabled(False)
            self.timer.stop()
        except Exception as e:
            print(e)

    # 数据接收
    def dataReceive(self):
        num = self.ser.inWaiting()
        if num > 0:
            data = self.ser.read(num)
            code = self.hexRX.isChecked()
            if code:
                data = data.hex()
                res = ''
                for i in range(0, len(data), 2):
                    res = res + data[i:i + 2] + ' '
                res = res[:-1]
            else:
                res = data.decode('Ascii')
            self.rxData.appendPlainText(res)
        self.timer.start(20)

    # 停止接收
    def stopReceive(self):
        if self.stopRX.isChecked():
            self.timer.stop()
        elif self.ser is None:
            return
        else:
            self.dataReceive()

    # 发送数据
    def dataSend(self):
        # if self.ser.isOpen():
        res = self.txData.toPlainText()
        if res != "":
            if self.hexTX.isChecked():
                res = bytes.fromhex(res)
            else:
                res = (res + '\r\n').encode("utf-8")
            try:
                self.ser.write(res)
            except Exception as e:
                print(e)

    # 清除发送区
    def dataClear(self):
        self.txData.clear()

    # 打开文件
    def fileOpen(self):
        path, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', '*.txt')
        print(path)
        if path:
            f = open(path, 'r', encoding='utf-8')
            with f:
                data = f.read()
                self.txData.setPlainText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = PyqtSerial()
    myWin.show()
    sys.exit(app.exec_())
