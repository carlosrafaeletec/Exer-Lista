l = list()

#Exer 1 e 2

def preenche_lista(lista) -> None:
    tam = 0
    while tam < 5:
        val = input("Preenche a lista: ")
        lista.append(val)
        tam += 1

def exibe_lista(lista) -> None:
   preenche_lista(l)
   print("lista = ", lista)

#Exer 3
def conta_elementos(lista) -> int:
    print(exibe_lista(l))
    i = 0
    while lista:
        lista.pop()
        i += 1
    return i

#Exer 4
def retorna_indice(lista) -> int:
    print(conta_elementos(l))
    for i in range(len(lista)):
        if lista[i] != l:

