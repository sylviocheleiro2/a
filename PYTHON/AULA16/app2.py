import urllib.request
from bs4 import BeautifulSoup

base_url = 'https://www.backloggd.com/games/lib/popular?page='
num_paginas = 5  # Número de páginas a serem processadas

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

todos_titulos = []

for pagina in range(1, num_paginas + 1):
    url = f'{base_url}{pagina}'

    # Criar o Request com headers
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    web_content = response.read()
    soup = BeautifulSoup(web_content, 'html.parser')

    # Encontrar todos os elementos que contêm os títulos dos jogos
    titulo_elementos = soup.find_all('div', class_='game-text-centered')

    # Extrair e adicionar os títulos dos jogos à lista
    titulos = [titulo.text.strip() for titulo in titulo_elementos]
    todos_titulos.extend(titulos)

# Imprimir todos os títulos dos jogos
print("Títulos dos jogos:")
for titulo in todos_titulos:
    print(titulo)
