from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo
from PyQt5.QtCore import QIODevice
app = QtWidgets.QApplication([])
ui = uic.loadUi("dising.ui")
ui.setWindowTitle("SerialGUI")

serial = QSerialPort()
serial.setBaudRate(115200)
portlist = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portlist.append(port.portName())
    ui.comL.addItems(portlist)
def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)

def onClose():
    serial.close()

def serialSend(data): #список int
    txs = ""
    for val in data:
        txs +=str(val)
        txs +=','
    txs = txs[:-1]
    txs +=";"
    serial.write(txs.encode())
    print(txs)

def onRead():
    rx = serial.readLine()
    rxs =str(rx, 'utf-8').strip()
    print(rxs)
    data = rxs.strip(',')
    print(data)

def EnableMotor(val):
    if val == 2: val =1;
    serialSend([1,val])

def HomeX(val):
    if val == False: val = 1;
    serialSend([2, val])

def HomeZ(val):
    if val == False: val = 1;
    serialSend([3, val])


def Home(val):
    if val == False: val = 1;
    serialSend([4, val])


def EnableAaxis(val):
    if val == 2: val = 1;
    serialSend([5, val])


def Aasixtozero(val):
    if val == False: val = 1;
    serialSend([6, val])

def Aasixtozero(val):
    if val == False: val = 1;
    serialSend([7, vaL, ])


ui.Azero.clicked.connect(Aasixtozero)
ui.EnableA.stateChanged.connect(EnableAaxis)
ui.home.clicked.connect(Home)
ui.homeZ.clicked.connect(HomeZ)
ui.homeX.clicked.connect(HomeX)
ui.EnableM.stateChanged.connect(EnableMotor)
serial.readyRead.connect(onRead)
ui.openB.clicked.connect(onOpen)
ui.closeB.clicked.connect(onClose)



ui.show()
app.exec()