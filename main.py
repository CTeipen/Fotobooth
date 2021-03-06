#!/usr/bin/python
import sys
import functools
import os
import time
import signal
import subprocess
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QCheckBox, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

########################################################################
########################################################################
wannaShutdown = False
DEFAULT_CLOUD_PATH = "/home/pi/Nextcloud/"
DEFAULT_USB_PATH = "/media/pi/"
SOFTWARE_PATH = "/home/pi/git/Fotobooth/"

class Ui_Fotobox(object):

    def __init__(self):
        super().__init__()
        self.title = 'Fotobox 2.0 - youinthebox.de'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 100

    def setupUi(self, FotoboxDialog):
        FotoboxDialog.setWindowTitle(self.title)
        FotoboxDialog.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()

        qtRectangle = FotoboxDialog.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        FotoboxDialog.move(qtRectangle.topLeft())

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        FotoboxDialog.setLayout(windowLayout)
        app.aboutToQuit.connect(self.closeEvent)

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(2, 3)
        
        gridX = 0
        gridY = 0
        
        # Camera Label
        gridX += 1
        gridY = 0
        lbl_camera = QtWidgets.QLabel(FotoboxDialog)
        lbl_camera.setObjectName("lbl_camera")
        lbl_camera.setText("Kamera")
        layout.addWidget(lbl_camera,gridY,gridX)
        

        # Camera Input
        gridX += 1
        global txt_camera
        txt_camera = QtWidgets.QLineEdit(FotoboxDialog)
        txt_camera.setEnabled(False)
        txt_camera.setObjectName("txt_camera")
        layout.addWidget(txt_camera,gridY,gridX)

        # Camera Button
        gridX += 1
        btn_camera = QtWidgets.QToolButton(FotoboxDialog)
        btn_camera.setObjectName("btn_camera")
        btn_camera.setText('Check')
        btn_camera.clicked.connect(self._check_camera_connection)
        layout.addWidget(btn_camera,gridY,gridX)
         
        
               
        # Cloudfolder Label
        gridX = 1
        gridY += 1
        lbl_cloudFolder = QtWidgets.QLabel(FotoboxDialog)
        lbl_cloudFolder.setObjectName("lbl_cloudFolder")
        lbl_cloudFolder.setText("Cloud Ordner")
        layout.addWidget(lbl_cloudFolder,gridY,gridX)
        

        # Cloudfolder Input
        gridX += 1
        global txt_cloudFolder
        txt_cloudFolder = QtWidgets.QLineEdit(FotoboxDialog)
        txt_cloudFolder.setEnabled(False)
        txt_cloudFolder.setObjectName("txt_cloudFolder")
        layout.addWidget(txt_cloudFolder,gridY,gridX)

        # Cloudfolder Button
        gridX += 1
        global btn_cloudFolder
        btn_cloudFolder = QtWidgets.QToolButton(FotoboxDialog)
        btn_cloudFolder.setObjectName("btn_cloudFolder")
        btn_cloudFolder.setText('...')
        btn_cloudFolder.clicked.connect(functools.partial(self._open_file_dialog, DEFAULT_CLOUD_PATH, txt_cloudFolder))
        layout.addWidget(btn_cloudFolder,gridY,gridX)


        # UsbFolder CheckBox
        gridY += 1
        gridX = 0
        global cb_usbFolder
        cb_usbFolder = QCheckBox()
        cb_usbFolder.setChecked(False)
        cb_usbFolder.stateChanged.connect(lambda:self.btnstate(btn_usbFolder))
        layout.addWidget(cb_usbFolder,gridY,gridX)

        # UsbFolder Label
        gridX += 1
        lbl_usbFolder = QtWidgets.QLabel(FotoboxDialog)
        lbl_usbFolder.setObjectName("lbl_usbFolder")
        lbl_usbFolder.setText("USB Ordner")
        layout.addWidget(lbl_usbFolder,gridY,gridX)

        # UsbFolder Input
        gridX += 1
        global txt_usbFolder
        txt_usbFolder = QtWidgets.QLineEdit(FotoboxDialog)
        txt_usbFolder.setEnabled(False)
        txt_usbFolder.setObjectName("txt_usbFolder")
        layout.addWidget(txt_usbFolder,gridY,gridX)

        # UsbFolder Button
        gridX += 1
        global btn_usbFolder
        btn_usbFolder = QtWidgets.QToolButton(FotoboxDialog)
        btn_usbFolder.setObjectName("btn_usbFolder")
        btn_usbFolder.setText('...')
        btn_usbFolder.setEnabled(False)
        btn_usbFolder.clicked.connect(functools.partial(self._open_file_dialog, DEFAULT_USB_PATH, txt_usbFolder))
        layout.addWidget(btn_usbFolder,gridY,gridX)



        # qrCode CheckBox
        gridY += 1
        gridX = 0
        global cb_qrCode
        cb_qrCode = QCheckBox()
        cb_qrCode.setChecked(False)
        cb_qrCode.stateChanged.connect(lambda:self.btnstate(txt_qrCode))
        layout.addWidget(cb_qrCode,gridY,gridX)

        # qrCode Label
        gridX += 1
        lbl_qrCode = QtWidgets.QLabel(FotoboxDialog)
        lbl_qrCode.setObjectName("lbl_qrCode")
        lbl_qrCode.setText("QR Code")
        layout.addWidget(lbl_qrCode,gridY,gridX)

        # qrCode Input
        gridX += 1
        global txt_qrCode
        txt_qrCode = QtWidgets.QLineEdit(FotoboxDialog)
        txt_qrCode.setEnabled(False)
        txt_qrCode.setObjectName("txt_qrCode")
        layout.addWidget(txt_qrCode,gridY,gridX)

        # Start/End Button
        gridY += 1
        gridX = 2
        global btn_startEnd
        btn_startEnd = QtWidgets.QToolButton(FotoboxDialog)
        btn_startEnd.setObjectName("btn_startEnd")
        btn_startEnd.setText('Starten')
        btn_startEnd.clicked.connect(functools.partial(self._start_fotobox, FotoboxDialog))
        layout.addWidget(btn_startEnd,gridY,gridX)

        gridX += 1
        global btn_reset
        btn_reset = QtWidgets.QToolButton(FotoboxDialog)
        btn_reset.setObjectName("btn_reset")
        btn_reset.setText('Reset')
        btn_reset.clicked.connect(self.resetUI)
        layout.addWidget(btn_reset,gridY,gridX)

        self.horizontalGroupBox.setLayout(layout)

        self.loadData()


########################################################################
########################################################################

    def loadData(self):
        if os.path.isfile(SOFTWARE_PATH + "save.p"):
            fotobox_data = pickle.load( open( SOFTWARE_PATH + "save.p", "rb" ) )

            txt_cloudFolder.setText(str(fotobox_data['pathCloudFolder']))
            cb_usbFolder.setChecked(fotobox_data['boolUsbFolder'])
            txt_usbFolder.setText(fotobox_data['pathUsbFolder'])
            cb_qrCode.setChecked(fotobox_data['boolQrCode'])
            txt_qrCode.setText(fotobox_data['textQrCode'])

########################################################################

    def resetUI(self, FotoboxDialog):
        
        txt_cloudFolder.setText("")
        txt_cloudFolder.update()

        cb_usbFolder.setChecked(False)
        txt_usbFolder.setText("")

        cb_qrCode.setChecked(False)
        txt_qrCode.setText("")
 
        if os.path.isfile(SOFTWARE_PATH + "save.p"):
            os.remove(SOFTWARE_PATH + "save.p")

        python = sys.executable
        os.execl(python, python, * sys.argv)

########################################################################

    def _check_camera_connection(self):
        ret = False
        name = "Keine Kamera verbunden"
        
        ex = subprocess.Popen(['gphoto2', '--auto-detect'], stdout=subprocess.PIPE)
        out, err = ex.communicate()

        for line in out.splitlines():
            if b'usb:' in line:
                name = line.decode('ASCII').split('usb')[0]
                ret = True
                self._kill_gphoto()
                break
                
        txt_camera.setText(name)
        return ret


########################################################################

    def _open_file_dialog(self, destinyDir, inputField):

        if inputField.text() != "":
            directory = inputField.text()
        else:
            directory = destinyDir

        directory = str(QtWidgets.QFileDialog.getExistingDirectory(directory=str(directory), options=QtWidgets.QFileDialog.ShowDirsOnly))
        inputField.setText('{}/'.format(directory))

########################################################################

    def btnstate(self,obj):
        if obj.isEnabled():
            obj.setEnabled(False)
        else:
            obj.setEnabled(True)

########################################################################

    def checkVars(self, FotoboxDialog):
        
        if not self._check_camera_connection():
            QMessageBox.question(FotoboxDialog, 'Keine Kamera angeschlossen', 'Die Kamera ist nicht mit dem Computer verbunden. Schliessen Sie die Kamera an und versuchen Sie es erneut.', QMessageBox.Ok)
            return False
        
        if len(txt_cloudFolder.text()) <= 1:
            QMessageBox.question(FotoboxDialog, 'Fehlende Eingabe', 'Bitte geben Sie den Pfad zum You In The Cloud Ordner an.', QMessageBox.Ok)
            return False

        if cb_usbFolder.isChecked():
            if len(txt_usbFolder.text()) <= 1:
                QMessageBox.question(FotoboxDialog, 'Fehlende Eingabe', 'Bitte geben Sie den Pfad zum USB Stick an.', QMessageBox.Ok)
                return False

        if cb_qrCode.isChecked():
            if len(txt_qrCode.text()) <= 0:
                QMessageBox.question(FotoboxDialog, 'Fehlende Eingabe', 'Bitte geben Sie eine URL an, auf die der QR Code zeigen soll.', QMessageBox.Ok)
                return False
            else:
                subprocess.Popen("qrencode -o %sqrcode.png -s 10 %s"
                    % (txt_cloudFolder.text(), txt_qrCode.text()), shell=True)

        return True

########################################################################

    def _kill_gphoto(self):
            
        ex = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = ex.communicate()

        for line in out.splitlines():
            if b'gvfsd-gphoto2' in line:
                pid = int(line.split(None,1)[0])
                os.kill(pid, signal.SIGKILL)

########################################################################

    def _start_fotobox(self, FotoboxDialog):
            
        if btn_startEnd.text() == 'Starten':

            if self.checkVars(FotoboxDialog):
                    
                if cb_usbFolder.isChecked():
                        
                    print("################################")
                    print(txt_cloudFolder.text())
                    print(txt_usbFolder.text())
                    subprocess.Popen(SOFTWARE_PATH + "start.sh %s %s"
                        % (txt_cloudFolder.text(),
                        txt_usbFolder.text()), stdout=subprocess.PIPE, shell=True)
                        
                else:
                        
                    subprocess.Popen(SOFTWARE_PATH + "start.sh %s"
                        % (txt_cloudFolder.text()), stdout=subprocess.PIPE, shell=True)


                btn_cloudFolder.setEnabled(False)
                cb_usbFolder.setEnabled(False)
                cb_qrCode.setEnabled(False)
                btn_reset.setEnabled(False)

                if cb_usbFolder.isChecked():
                    btn_usbFolder.setEnabled(False)

                if cb_qrCode.isChecked():
                    txt_qrCode.setEnabled(False)


                btn_startEnd.setText('Beenden')

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Fotobox wurde gestartet")
                msg.setText("Die Fotobox 2.0 wurde erfolgreich gestartet. Die Anwendung kann minimiert werden. Zum Beenden der Fotobox auf den 'Beenden'-Button klicken. Viel Spass!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        else:

            ex = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = ex.communicate()

            for line in out.splitlines():
                if b'feh' in line or b'startSlideshow' in line or b'gphoto2' in line:
                    pid = int(line.split(None,1)[0])
                    os.kill(pid, signal.SIGKILL)


            btn_cloudFolder.setEnabled(True)
            cb_usbFolder.setEnabled(True)
            cb_qrCode.setEnabled(True)
            btn_reset.setEnabled(True)

            if cb_usbFolder.isChecked():
                    btn_usbFolder.setEnabled(True)

            if cb_qrCode.isChecked():
                txt_qrCode.setEnabled(True)


            btn_startEnd.setText('Starten')
            self._before_exit()

########################################################################

    def closeEvent(self):
        if btn_startEnd.text() == 'Beenden':
            ex = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = ex.communicate()

            for line in out.splitlines():
                if b'feh' in line or b'startSlideshow' in line or b'gphoto2' in line:
                    pid = int(line.split(None,1)[0])
                    os.kill(pid, signal.SIGKILL)


            btn_cloudFolder.setEnabled(True)
            cb_usbFolder.setEnabled(True)
            cb_qrCode.setEnabled(True)

            if cb_usbFolder.isChecked():
                    btn_usbFolder.setEnabled(True)

            if cb_qrCode.isChecked():
                txt_qrCode.setEnabled(True)


            btn_startEnd.setText('Starten')
        self._before_exit()
        
            
########################################################################


    def _before_exit(self):
            
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Fotobox beendet")
        msg.setText("Fotobox 2.0 wurd erfolgreich beendet. Soll der Rechner runtergefahren werden?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msg.exec_()

        fotobox_data = {
            "pathCloudFolder": txt_cloudFolder.text(),
            "boolUsbFolder": cb_usbFolder.isChecked(),
            "pathUsbFolder": txt_usbFolder.text(),
            "boolQrCode": cb_qrCode.isChecked(),
            "textQrCode": txt_qrCode.text()
        }
        pickle.dump( fotobox_data, open( SOFTWARE_PATH + "save.p", "wb" ) )

        if ret == QMessageBox.Yes:
            os.system('shutdown -P -t 0')

########################################################################
########################################################################

if __name__ == "__main__":
    global app
    app = QApplication(sys.argv)
    FotoboxDialog = QtWidgets.QDialog()
    ex = Ui_Fotobox()
    ex.setupUi(FotoboxDialog)
    FotoboxDialog.show()
    sys.exit(app.exec_())
