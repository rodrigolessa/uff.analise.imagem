#timer -	Displays a seconds timer with start and stop buttons.
#           Control-c and control-q cause it to exit.
# Selecionar imagem
# Se for RGB
# Selecionar canal da imagem
# Selecionar tipo de conversão em outros espaços de cores
# Selecionar tipo de filtro para remover ruido (gaussiano)
# Selecionar tipo de treshold
# Selecionar grau do treshold
# Selecionar tipo de binarização
# Selecionar extração de caracteristicas

import os
import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle('Análise de imagens')
    w.show()
    sys.exit(app.exec_())

window()
