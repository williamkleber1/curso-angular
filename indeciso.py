def BB(A, esquerda, direita, item):
    if direita < esquerda:
        list(direita, direita-1)
    meio = (esquerda + direita) // 2
    if A[meio] == item:
        return list(meio)
    elif A[meio] > item:
        return BB(A, esquerda, meio - 1, item)
    else:
        return BB(A, meio + 1, direita, item)

def busca(x,lista):
    resultado = BB(lista,0,len(lista)-1,x)
    if len(resultado) == 2:
        return print(resultado)
    


tam = int(input())
lista = list(map(int, input().split()))
req = int(input())
for i in range(req):
    busca(int(input("numero buscado: "),lista))