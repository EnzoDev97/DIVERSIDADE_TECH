# 25 - Faça uma função que receba um texto e uma palavra, então verifique se a palavra está no texto, retornando True ou False.

def pertence(texto, palavra):
    if palavra in texto:
        return True
    return False

pertence('ENZO','E')

# OU


def word(t, p): # resumido
    return p in t

word('LARI', 'L')