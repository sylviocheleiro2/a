import re
import urllib.request
from bs4 import BeautifulSoup

# URL do jogo
url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
# Headers para simular uma requisição de navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Criar o Request com headers
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
web_content = response.read()
soup = BeautifulSoup(web_content, 'html.parser')


livro_elementos = soup.find_all('h3')
titulos = [livro.find('a')['title']
           for livro in livro_elementos if 'murder' in livro.find('a')['title'].lower()]


# Encontrar todos os elementos que contêm os preços dos livros
preco_elementos = soup.find_all('div', class_='product_price')
precos = [preco.find(
    'p', class_='price_color').text for preco in preco_elementos]

# Combinar títulos e preços
livros = zip(titulos, precos)

# Imprimir títulos e preços dos livros
print("Títulos e preços dos livros:")
for titulo, preco in livros:
    print(f"{titulo}: {preco}")
