# -*- coding: utf-8 -*-
import requests
import json

data_list = []
final_list = []
page_index = 1
still_sending = True

def url_request(i):
    return requests.get('http://challenge.dienekes.com.br:8888/api/numbers?page={0}'.format(i))

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

def extractToJson(list_data):
    data = {}
    data['numbers'] = []
    for element in list_data:
        data['numbers'].append(element)
    with open('static/data.json', 'w') as outfile:
        json.dump(data, outfile)

while(still_sending):
    response = url_request(page_index)
    if(response.status_code == 200):
        dados = response.json()['numbers']
        if(dados):
            for d in dados:
                data_list.append(d)
            #print('Dado extraído com sucesso da página {0}'.format(page_index))
            page_index += 1
        else:
            print('Finalizando...')
            still_sending = False

        final_list = data_list

    else:
        print('Ocorreu um erro na requisição, tentando novamente para a página {0}'.format(page_index))

print(len(final_list))

quickSort(final_list, 0, len(final_list) - 1)
extractToJson(final_list)