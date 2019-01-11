def insertionSort(v, n):
    i = 0
    j = 1
    aux = 0
    while(j < n):
        aux = v[j]
        i = j - 1
        while((i >= 0) and (v[i] > aux)):
            v[i + 1] = v[i]
            i = i - 1
        v[i + 1] = aux
        j = j + 1
    return v

file_data = open('data.txt', 'r')

total = file_data.readlines()

lista = []

for linha in total:
    lista.append(linha)

lista_ordenada = insertionSort(lista, len(lista))

file_data = open('data_ordered.txt', 'w')
for i in lista_ordenada:
    file_data.write('{}\n'.format(i))
print('Terminou')