endereco = "Rua: São luiz 24, Bairro: Jockey de Itaparica - " \
           "Cidade: Vila Velha-ES CEP: 29103-890"

import re


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)


    