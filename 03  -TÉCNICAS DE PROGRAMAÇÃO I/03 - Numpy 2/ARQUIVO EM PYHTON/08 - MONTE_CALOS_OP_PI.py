## Monte Carlo Calculo de Pi

#Imagine que você tenha um quadrado de lado 2. Dentro desse quadrado conseguimos inserir um circulo com raio 1.

#Logo a área do quadrado é: $l^2 = (2*r)^2$  
#E a área do circulo é: $\pi * r^2$  

#Imagine que eu jogue 1000 agulhas aleatoriamente nesse quadrado.  
#Quantas agulhas irão cair dentro do circulo?  
#Quantas agulhas irão cair fora do circulo?

#$P(agulha \ dentro) = ÁreaCirculo / AreaQuadrado$  
#$P(agulha \ dentro) = \pi * r^2 / 4r^2$  
#$P(agulha \ dentro) = \pi / 4$  
#$\pi = (Dentro/Total) * 4$  


#Construa um programa que simule o lançamento de $n$ agulhas (1000 por exemplo).  
#Qual seria o valor de pi?  
#E se fizermos essa simulação (Monte Carlo) muitas vezes(1, 10, 100, 1000, 10000)? Qual o valor de pi (média e desvio padrão)?  

#distância <= 1 agulha dentro do círculo

#e lembrando que:
#$d^2 = x^2 + y^2$ ==> $d =  sqrt(x^2 + y^2)$

#%%time
import random

pis = []
n_sim = 10000
agulhas = 1000
for _ in range(n_sim):
    pontos_circulo = 0
    total = 0
    for i in range(agulhas):
        total +=1
        x = random.random()
        y = random.random()
        dist = (x**2 + y**2) ** 0.5
        if dist <= 1:
            pontos_circulo += 1
    pi = 4 * (pontos_circulo / total) 
    pis.append(pi)

import seaborn as sns
sns.kdeplot(pis)