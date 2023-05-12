# Biblioteca requests de HTTP com interação de API do site newsapi, retornando o conteúdo em modelo dict
import requests
r = requests.get(
    'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0275859d838f47cebe7fa143780f052b')
conteudo = r.json()
print(type(conteudo))  # dict
conteudo = conteudo['articles']
for artigo in conteudo:
    print(artigo['title'])
