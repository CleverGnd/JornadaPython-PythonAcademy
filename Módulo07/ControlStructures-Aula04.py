from random import randint
capacidade_max_balde = 1000

balde = 0
copos = 0
while balde <= capacidade_max_balde:
    volume_copo = randint(95, 100)

    print(f'O copo foi enchido com {volume_copo} mls.')

    copos +=1
    balde += volume_copo

    print(f'O volume do balde é de {balde} mls.\n')

print(f'O volume do balde ultrapassou a capacidade máxima de {capacidade_max_balde} mls e está com {balde} mls!\n'
      f'Foram utilizados {copos} copos.')