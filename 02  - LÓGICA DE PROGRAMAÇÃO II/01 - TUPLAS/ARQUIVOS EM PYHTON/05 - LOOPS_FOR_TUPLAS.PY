#05 - Crie Tuplas e fatie as informações que estão contidas nela


cadastros = (
    ('Ana', 32, 'SP'),
    ('João', 25, 'RJ'),
    ('Maria', 19, 'PE')
)
# Percorrendo a tupla de tuplas
for cadastro in cadastros:
  # Imprimindo cada tupla
  print(cadastro)

print('Primeira pessoa cadastrada:', cadastros[0])
print('Nome da pessoa cadastrada:', cadastros[0][0])
print('Nome e idade da pessoa cadastrada:', cadastros[0][:2])