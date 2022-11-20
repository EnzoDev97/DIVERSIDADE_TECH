#**Desafio**

#Pegue a lista abaixo de notas por aluno e calcule:
#- média por aluno
#- média por prova
#- Desvio padrão por aluno
#- Desvio padrão por prova
#- Calcule os quantis 25, 50, 75 por aluno
#- Calcule os quantis 25, 50, 75 por prova

#Considerando que a média para ser aprovado é $5$, diga quais alunos (indices) foram aprovados. Além disso diga a quantidade de alunos aprovados e a sua porcentagem

#Por fim execute um teste de hipótese para verificar se as notas de cada prova seguem uma distribuição normal (código disponível). Comente o que achou desse teste, e quais as conclusões

#Dicas:
#- Utilize a função [`np.quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile)

#Extra:
#- Quais outras análises você faria?

import numpy as np
prova1 = [ 7.32310699,  9.53815353,  4.67334801,  6.59830925,  6.66911822,
        1.77222727,  6.43684924,  5.43160477,  5.68826716,  8.08642338,
        1.0484659 ,  3.92952847,  6.50989246,  2.50691336,  3.44837851,
        5.36087258,  4.1607412 ,  8.16816087,  5.74915158,  6.81928442,
        5.78928423,  5.90857783,  4.76342497,  7.55418044,  6.77148876,
        2.01707694,  6.77867453,  6.89171555,  4.82658369,  7.70076362,
        4.48058631,  5.62032984,  8.67456615,  4.98242627,  6.57045975,
        4.10097055,  6.71796888,  6.13668877,  6.05985766,  6.02895155,
        9.7569509 ,  8.38657445,  8.21004194,  4.63615177,  6.61371496,
        4.9101586 ,  5.08166831,  4.02027733,  6.16362433,  4.15501069,
        4.49508256,  3.27892403,  3.03611322,  3.27375519,  5.28128231,
        5.85303752,  8.49750499,  5.16446418,  1.72850909,  2.03939026,
        7.56084931,  4.1333252 ,  4.60506328,  4.3076715 ,  9.24445958,
        5.90639065,  3.9523371 ,  7.35423713,  6.25553193,  6.86909983,
        4.42940802,  8.41764679,  6.61170966,  3.36589986,  5.3865782 ,
        4.42790597,  7.67905478,  5.74486493,  3.0210713 ,  2.10366003,
        5.9001788 ,  4.03096928,  8.08990797, 10.        ,  8.82667933,
        5.92949768,  5.83254006,  6.38697389,  4.69459527,  6.39838523,
        5.67991139,  0.93141126,  4.39835283,  6.11818097,  5.49677715,
        6.69772736,  9.46427727,  5.24208651,  8.4100053 ,  8.59941824]
prova2 = [ 3.86586422,  5.26894331,  6.31900481,  2.58493657, 10.        ,
        6.34665066,  6.82581122,  3.00438801, 10.        , 10.        ,
       10.        ,  7.31735866,  5.831104  ,  2.98166861,  4.61025961,
        3.15287741,  6.25096741,  8.12234798,  5.69771246,  0.75591952,
        8.72745257,  6.08407841,  5.21078521,  2.96522826, 10.        ,
       10.        ,  4.78343523, 10.        ,  7.25257786, 10.        ,
        4.58105557, 10.        ,  2.80986267, 10.        ,  3.94852279,
        5.43455643,  3.34353164,  1.4052814 ,  2.8684444 , 10.        ,
        3.23324882,  2.56830893, 10.        ,  6.23293846,  4.95740421,
        0.82258908,  8.24300277, 10.        ,  4.04981569,  2.50954976,
        3.85325349,  9.07507697,  2.90281051,  5.57813293,  7.9142119 ,
        2.11802407,  9.66358214,  3.46919201,  3.78690434,  7.20733693,
        5.97441787,  2.03188462,  8.21979382,  4.83739141,  7.57396101,
        9.45448236,  4.98550558,  7.80871829,  9.9060318 ,  8.52904802,
        2.11349418,  7.38857237, 10.        ,  3.80678808, 10.        ,
        4.57788463,  3.84139089,  9.43204842,  7.81033157,  3.5098406 ,
        6.8072703 ,  3.92218258, 10.        ,  2.42707477,  5.89068072,
       10.        ,  2.83580732, 10.        ,  5.56408124,  5.88092815,
        6.29655882, 10.        ,  2.56469929,  2.29020154, 10.        ,
        9.90566998,  5.39044373,  1.70263851,  8.41427847,  4.11856827]
prova3 = [ 6.0397507 ,  1.42758776,  1.68758623,  0.91323371,  5.68435676,
        1.09500724,  1.26344938,  2.70028337,  0.85173695,  1.04351072,
       10.        ,  6.47959549,  1.2512433 ,  4.80403122,  1.81182283,
        2.21371919,  4.89478956,  6.54842281,  1.22367174,  0.76344403,
        2.31855296,  1.15926703,  6.51540784,  0.7400826 ,  1.58270615,
        0.85871609,  0.13482385,  3.50788938,  6.05712552,  6.80902627,
        4.66503693,  5.75545349,  2.34482129,  0.48553074,  1.27016792,
        3.2906171 , 10.        ,  4.55726513,  0.81727528,  2.498553  ,
        7.26586947,  0.40711405,  0.3298744 , 10.        ,  8.26779967,
        2.23897715,  5.15003198,  6.13644229,  1.60405181,  2.29246806,
        7.88342556,  0.05383723,  1.65182029, 10.        ,  2.45158052,
        2.07959184,  0.13234637,  5.22031833, 10.        ,  4.78589039,
        4.28469673, 10.        ,  0.66910424,  0.43945092,  4.62847799,
        0.30599809,  9.58022274,  4.61891776,  5.9770302 ,  9.13004073,
        0.34504645,  1.64374136,  3.2312216 ,  7.69209464,  3.24761461,
        3.41467533,  3.40437786,  4.38337641,  5.1508133 ,  4.63401958,
        0.59473791, 10.        ,  7.64282232,  2.55936951,  4.12515056,
        1.24403381,  7.08569765,  3.67544459,  1.21855821,  7.35122313,
        0.41457172,  1.17833162,  1.64644444,  0.53046253,  2.49672963,
        5.80514786,  2.09146878,  4.74818797,  0.86284908,  7.01854907]
notas = np.asarray([prova1, prova2, prova3])

# Média por aluno
media_aluno = notas.mean(axis=0)
print(f'Média por aluno #Total {media_aluno.size}:', media_aluno)
print('-'*32)
# Média por prova
media_prova = notas.mean(axis=1)
print(f'Média por prova #Total {media_prova.size}:', media_prova)
print('-'*32)
# Desvio padrão por aluno
std_aluno = notas.std(axis=0)
print('Desvio padrão da nota por aluno', std_aluno)
print('-'*32)
# Desvio padrão por prova
std_prova = notas.std(axis=1)
print('Desvio padrão da nota por prova', std_prova)
print('-'*32)
# Quantis 25, 50, 75 por aluno
q_25_aluno = np.quantile(notas, 0.25, axis=0)
q_50_aluno = np.quantile(notas, 0.5, axis=0)
q_75_aluno = np.quantile(notas, 0.75, axis=0)
print(f'Quantil 25 {q_25_aluno}, quantil 50 {q_50_aluno}, quantil 75 {q_75_aluno} por aluno')
print('-'*32)
# Quantis 25, 50, 75 por prova
q_25_prova = np.quantile(notas, 0.25, axis=1)
q_50_prova = np.quantile(notas, 0.5, axis=1)
q_75_prova = np.quantile(notas, 0.75, axis=1)

print(f'Quantil 25 {q_25_prova}, quantil 50 {q_50_prova}, quantil 75 {q_75_prova} por prova')
print('-'*32)
# Quais alunos (indices) foram aprovados (nota >=5)
idx_aprovados = []
for idx, nota in enumerate(media_aluno):
  if nota >= 5:
    idx_aprovados.append(idx)


print('Os seguintes alunos foram aprovados', idx_aprovados)
print('-'*32)
# Quantos alunos foram aprovados (`int`)
print(f'{len(idx_aprovados)} alunos foram aprovados')
print('-'*32)
# Porcentagem de alunos aprovados (`float`)
print(f'Porcentagem de alunos aprovados {(len(idx_aprovados)/media_aluno.size) * 100:.2f}%')
print('-'*32)
# ---------

# D'Agostino and Pearson's Test
from scipy.stats import normaltest
# Teste de normalidade
stats, p_values = normaltest(notas, axis=1)
nome_provas = ['Prova1', 'Prova2', 'Prova3']
for nome, stat, p_value in zip(nome_provas, stats, p_values):
  print(f'Statistics={stat:.3f}, p={p_value:.3f}')
  alpha = 0.05
  if p_value > alpha:
      print(f'A {nome} parece normal (hipótese nula aceita)')
  else:
      print(f'A {nome} não parece normal (hipótese nula rejeitada)')