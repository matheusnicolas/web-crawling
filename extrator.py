# -*- coding: utf-8 -*-
import requests

data_list = []
final_list = []
page_index = 9950
still_sending = True

def url_request(i):
    return requests.get('http://challenge.dienekes.com.br:8888/api/numbers?page={0}'.format(i))

while(still_sending):
    response = url_request(page_index)
    if(response.status_code == 200):
        dados = response.json()['numbers']
        if(dados):
            for n in dados:
                print(n)
                data_list.append(n)
            print('Dado extraído com sucesso da página {0}'.format(page_index))
            page_index += 1
        else:
            print('Finalizando...')
            still_sending = False

        final_list = data_list
        print('200: {0}'.format(len(data_list)))
        
    else:
        print('Ocorreu um erro na requisição, tentando novamente para a página {0}'.format(page_index))

file_d = open('data.txt', 'w')
for line in final_list:
    file_d.write('{}\n'.format(line))

file_d.close()

print(len(final_list))