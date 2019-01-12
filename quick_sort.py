import json

def quickSort(list_v, p, r):
   if(p < r):
       q = partition(list_v, p, r)
       quickSort(list_v, p, q - 1)
       quickSort(list_v, q + 1, r)

def partition(list_v, p, r):
   pivot = list_v[r]
   i = p - 1

   for j in range(p, r):
       if(list_v[j] <= pivot):
           i = i + 1
           aux = list_v[i]
           list_v[i] = list_v[j]
           list_v[j] = aux

   aux = list_v[i + 1]
   list_v[i + 1] = list_v[r]
   list_v[r] = aux
   
   return i + 1

list_v = [9, 8, 378, 8317, 317389, 137, 10, 1, 22, 9, 8137431, 84137439, 384943]
quickSort(list_v, 0, len(list_v) - 1)
print("Lista ordenada: {}".format(list_v))


print(list_v)
data = {}
data['numbers'] = []

for i in list_v:
    data['numbers'].append(i)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
print(data)