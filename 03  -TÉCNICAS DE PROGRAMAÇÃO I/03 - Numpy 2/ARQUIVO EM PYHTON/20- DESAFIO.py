#DESAFIO

#**12 - Nesse desafio, iremos praticar o conceito de indexação em imagens! Pois é, caso você ainda não saiba, as imagens são formadas com conjuntos de pixels, e esses pixels são números inteiros (entre 0 e 255). Sendo assim, quando carregamos uma imagem no Python, essa imagem será armazenada em um matriz (Numpy), ou seja, cada pixel dessa imagem será um elemento dessa matriz.**

#**No entanto, é importante que você também saiba que uma imagem colorida é composta por três matrizes, visto que uma imagem colorida é formada por 3 cores básicas: vermelho, verde e azul. Esse é o famoso padrão RGB. Portanto, sua imagem será armazenada em um array tridimensional.**

#**Sabendo disso, sua missão será carregar uma imagem colorida (em jpg) e exibir apenas a metade dessa imagem, tanto na horizontal quanto na vertical. Mas, calma... vamos te dar uma ajuda.**

#**Primeiro, você precisa instalar a biblioteca skimage para carregar a imagem, além da biblioteca do matplotlib para exibir a imagem (veremos essa biblioteca com mais detalhes nesse curso!), caso você ainda não tenha elas instaladas, claro. Para isso, utilize o comando pip install scikit-image matplotlib, se você estiver utilizando o pip, ou conda install scikit-image matplotlib, se estiver utilizando o Anaconda.**

#**Em seguida, observe o código abaixo; ele te mostra como você pode carregar uma imagem e exibi-la. Lembrando... Sua missão será carregar uma imagem colorida (em jpg) e exibir apenas a metade dessa imagem, tanto na horizontal quanto na vertical.**


from skimage import io
import numpy as np
import matplotlib.pyplot as plt

img = io.imread('images/numpy-logo.jpg') # Carregamento da imagem

print(type(img))

plt.imshow(img) # Exibição da imagem
