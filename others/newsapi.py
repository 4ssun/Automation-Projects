# Biblioteca requests de HTTP com interação de API do site newsapi, retornando o conteúdo em modelo dict
import requests


def get_artigo(topic, from_date, to_date, language='en', api_key='0275859d838f47cebe7fa143780f052b'):

    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    conteudos = r.json()
    print(conteudos)
    artigo = conteudos['articles']
    result = []
    for busca in artigo:
        result.append('Titulo:', busca['title'],  # type: ignore
                      '\n Descrição:\n', busca['description'])
        return result


print(get_artigo(topic='space', from_date='2023-05-12', to_date='2023-04-11'))
