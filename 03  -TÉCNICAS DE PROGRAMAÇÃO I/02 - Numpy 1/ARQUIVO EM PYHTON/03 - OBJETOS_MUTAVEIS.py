ds = ["Python", "SQL", 'R']
web = ["HTML", "CSS", 'JavaScript']

# Concatenando as listas com `+`
linguagens_mais = ds + web

print(f'''
Utilizando o operador "+"
ds: [id:\033[34m{id(ds)}\033[0m]: \033[31m{ds}\033[0m
web: [id:\033[33m{id(web)}\033[0m]: \033[32m{web}\033[0m
linguagens_mais: [id:\033[36m{id(linguagens_mais)}\033[0m]: \033[35m{linguagens_mais}\033[0m
''')

# Extendendo as listas com `extend`
linguagens_extend = ds
print(f'''
Antes de utilizar o extend
ds: [id:\033[34m{id(ds)}\033[0m]: \033[31m{ds}\033[0m
web: [id:\033[33m{id(web)}\033[0m]: \033[32m{web}\033[0m
linguagens_extend: [id:\033[36m{id(linguagens_extend)}\033[0m]: \033[35m{linguagens_extend}\033[0m
''')

linguagens_extend.extend(web)

print(f'''
Após utilizar o extend
ds: [id:\033[34m{id(ds)}\033[0m]: \033[31m{ds}\033[0m
web: [id:\033[33m{id(web)}\033[0m]: \033[32m{web}\033[0m
linguagens_extend: [id:{id(linguagens_extend)}]: {linguagens_extend}
''')

#No exemplo acima, ao utilizar o extend houve a mudança da lista original ds

#Para evitar esse comportamento precisamos alterar o endereço de memória, ou seja, realizar uma cópia profunda!

#Para ser seguro utilizamos o deepcopy


from copy import deepcopy

ds = ["Python", "SQL", 'R']
web = ["HTML", "CSS", 'JavaScript']

# Concatenando as listas com `+`
linguagens_mais = ds + web

print(f'''
Utilizando o operador "+"
ds: [id:\033[34m{id(ds)}\033[0m]: {ds}
web: [id:\033[33m{id(web)}\033[0m]: {web}
linguagens_mais: [id:\033[32m{id(linguagens_mais)}\033[0m]: \033[31m{linguagens_mais}\033[0m
''')

# Extendendo as listas com `extend`
linguagens_extend = deepcopy(ds)
print(f'''
Antes de utilizar o extend
ds: [id:\033[34m{id(ds)}\033[0m]: {ds}
web: [id:\033[33m{id(web)}\033[0m]: {web}
linguagens_extend: [id:\033[32m{id(linguagens_extend)}\033[0m]: \033[31m{linguagens_extend}\033[0m
''')

linguagens_extend.extend(web)

print(f'''
Após utilizar o extend
ds: [id:\033[34m{id(ds)}\033[0m]: {ds}
web: [id:\033[33m{id(web)}\033[0m]: {web}
linguagens_extend: [id:\033[32m{id(linguagens_extend)}\033[0m]: \033[31m{linguagens_extend}\033[0m
''')