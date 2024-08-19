palabra = "paralelepipedo"
contador = int(0)
vocales = ["a","e","i","o","u"]

for letra in palabra:
    contador+=1
    if letra in vocales:
        continue
    else:
        print(f'{letra} - {contador}')