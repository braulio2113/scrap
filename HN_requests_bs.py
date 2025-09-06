import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://news.ycombinator.com/ "

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36", #^ Esto es para esconder que hacemos scrap
}

respuesta = requests.get(url, headers=headers)
print(respuesta)
soup = bs(respuesta.text, 'lxml')
lista_de_noticias = soup.find_all('tr', class_='athing submission')

df = []
x = 0
for noticia in lista_de_noticias:
    df_noticia = pd.DataFrame()
    titulo = noticia.find('span', class_='titleline').text
    link = noticia.find('span', class_='titleline').find('a').get('href')
    metadata = noticia.find_next_sibling()
    
    #* No siempre estan disponibles algunas caracteristicas
    try:
        score = metadata.find('span', class_='score').text
        score = score.replace('points', '').strip()
    except:
        score = 'No score'

    try:
        user = metadata.find('a', class_='hnuser').text
    except:
        user = 'No user'
    
    try:
        user_link = metadata.find('a', class_='hnuser').get('href')
        user_link = f'{url}{user_link}'
    except:
        user_link = 'No user link'
    
    age = metadata.find('span', class_='age').text
    
    comments = metadata.find_all('a')
    try:
        comment = comments[-1].text
        comment = comment.replace('comments', '').replace('comment', '').strip()
    except:
        comment = 'No comments'
    
    #~ Guardamos cada elemento en columnas de un Dataframe
    df_noticia['Titulo'] = pd.DataFrame([titulo])
    df_noticia['Link'] = pd.DataFrame([link])
    df_noticia['Score'] = pd.DataFrame([score])
    df_noticia['User'] = pd.DataFrame([user])
    df_noticia['User Link'] = pd.DataFrame([user_link])
    df_noticia['Age'] = pd.DataFrame([age])
    df_noticia['Num Comments'] = pd.DataFrame([comment])
    df.append(df_noticia)
    
    x += 1
    print(f'{x}/{len(lista_de_noticias)}')
    print(titulo)
    print(link)
    print(score)
    print(user)
    print(user_link)
    print(age)
    print(comment)
    print()

df = pd.concat(df)
df.to_csv(f'Hacker_News.csv', header=True, index=False)