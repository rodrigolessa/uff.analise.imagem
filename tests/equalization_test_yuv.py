import cv2
import numpy as np
from matplotlib import pyplot as plt

imgName = 'pedestrian_test.tif'

# = 0 Return a grayscale image.
# < 0 Return the loaded image as is (with alpha channel).
# img = cv2.imread('pedestrian_test.tif', 0)
img = cv2.imread(imgName)

# We have three channels (RGB) for each pixel and 
# we cannot apply histogram equalization on the three channels 
# in a separate manner.

# Convert image to the YUV - old TV space color
# Representação dos três componentes do tipo de sinal vídeo componentes, um para luminosidade e outros dois para informação de cor. O YUV é o sistema de codificação de cor utlizado pelos padrões analógicos de TV (NTSC, PAL, SECAM). O color space YUV é diferente do RGB, por trabalhar com componentes separados de luz e cor, enquanto o RGB, color space através do qual tanto o olho humano como a câmera enxergam, trabalha com cores básicas, também chamadas primárias.
# O color space RGB ocupa muito espaço para ser representado numericamente, uma vez que são necessárias 3 faixas distintas (intervalos) destinadas a registrar individualmente os valores de cada de suas cores. Na década de 50, a implantação da TV colorida nos EUA exigia que o novo sinal fosse compatível com as existentes TVs P&B. Propunha-se um sinal que pudesse ser exibido na forma colorida pelos novos televisores e ainda assim continuasse a ser exibido em P&B pelos antigos aparelhos.
# Foi então desenvolvido um algoritmo denominado analog encoding, que conseguia, através da separação da parte de luminosidade (Y) e cor do sinal (U / V - mais detalhes adiante), codificá-los analogicamente de forma que o sinal resultante ocupasse bem menos espaço do que o RGB. As TVs P&B decodificam somente a parte (Y) deste sinal. A seguir, a descrição do que ocorre dentro de uma câmera de vídeo seguindo esse processo.
# A conversão RGB para YUV chama-se color space conversion e é efetuada através de fórmulas matemáticas. A parte de luminosidade do sinal YUV, representada pela letra "Y", é calculada somando-se as luminosidades dos sinais R+G+B, porém de maneira desigual: a cor verde é a dominante, a que tem maior participação e a azul a menor. O cálculo é efetuado através da fórmula:
# Y = 0.299R + 0.587G + 0.114B
#ou, aproximadamente, 30% de vermelho, 59% de verde e 11% de azul. O fator maior utilizado para a cor verde decorre de experiências que mostraram que ao analisar-se o brilho de determinada cena através de cada um dos componentes RGB como percebido pelo olho humano, conclui-se que a cor verde é responsável por 60 a 70% de sua intensidade. Este fato pode ser comprovado ao comparar-se a luminosidade no sistema RGB da cor pura verde (RGB = 0,255,0) com a da cor pura azul (RGB = 0,0,255) como mostra o desenho abaixo:
#A luminosidade emitida pelas duas cores é a mesma, porém o olho humano enxerga mais luz em uma e menos luz na outra. É para criar esse desequilíbrio que os fatores numéricos são empregados na fórmula do cálculo da luminosidade, permitindo obter-se assim o balanceamento do brilho entre as 3 cores básicas obtidas a partir da leitura do CCD da forma como o olho humano as enxerga. É por este motivo também (maior sensibilidade ao verde) que a implementação de cores utilizando um único CCD, através do padrão Bayer (descrito no item "CCD") emprega o dobro de filtros coloridos na cor verde em relação aos das cores vermelha e azul.
img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow("YUV", img)
cv2.waitKey(0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()
plt.close()

img[:,:,0] = cv2.equalizeHist(img[:,:,0])
img = cv2.equalizeHist(img)

hist_equalization_result = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)

cv2.imshow("Equalization", hist_equalization_result)
cv2.waitKey(0)

cv2.destroyAllWindows()