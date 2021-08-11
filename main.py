from PyQt5 import uic, QtWidgets
import pyshorteners

import clipboard



def gerar():
    avisofalho.close()
    global clink
    try:
        link = encurtador.lineinserir.text()
        short = pyshorteners.Shortener()
        clink = short.tinyurl.short(link)
        encurtador.linelink.setText(str(clink))
        encurtador.lineinserir.setText("")
    except:
        avisofalho.show()
        encurtador.lineinserir.setText("")

def copiar():
    global clink
    clipboard.copy(clink)
    avisok.show()

def fechar():
    avisofalho.close()
    avisok.close()

app = QtWidgets.QApplication([])
encurtador = uic.loadUi("encurtador.ui")
avisofalho = uic.loadUi("avisof.ui")
avisok = uic.loadUi("avisok.ui")
encurtador.pushButton.clicked.connect(gerar)
encurtador.pushcopiar.clicked.connect(copiar)
avisofalho.ok.clicked.connect(fechar)
avisok.ok.clicked.connect(fechar)
encurtador.show()
app.exec()



