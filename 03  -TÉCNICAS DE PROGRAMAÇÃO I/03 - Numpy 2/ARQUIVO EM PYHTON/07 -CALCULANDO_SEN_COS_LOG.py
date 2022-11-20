import numpy as np

x = np.linspace(1, 15, 150)
x

funcoes = [
    np.sin(x),
    np.cos(x),
    np.exp(x),
    np.log(x)
]

for funcao in funcoes:
  print(funcao[0:10])


import matplotlib.pyplot as plt

titulos = ['Função seno','Função cos', 'Função exp', 'Função log']
plt.figure(figsize=(11, 11))
for index, funcao in enumerate(funcoes):
    plt.subplot(2,2, index+1)
    plt.plot(x, funcao)
    plt.title(titulos[index])