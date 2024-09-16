import urllib.request
from bs4 import BeautifulSoup

# URL do jogo
url = 'https://www.backloggd.com/games/grand-theft-auto-san-andreas/'

# Headers para simular uma requisição de navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Criar o Request com headers
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
web_content = response.read()
soup = BeautifulSoup(web_content, 'html.parser')

# Extraindo informações usando Open Graph meta tags
og_tags = {
    'title': soup.find('meta', property='og:title'),
    'description': soup.find('meta', property='og:description'),
    'image': soup.find('meta', property='og:image'),
    'release_date': soup.find('meta', property='og:release_date'),
    'developers': soup.find('meta', property='og:developers'),
    'platforms': soup.find('meta', property='og:platforms')
}

# Extraindo dados de lançamento e desenvolvedores do HTML (Se não estiver nas meta tags)
# OBS: A estrutura da página pode variar, então você pode precisar inspecionar o HTML e ajustar os seletores.
data_lancamento = None
desenvolvedores = None

# Verifique se a meta tag está presente e obtenha o conteúdo
for tag, element in og_tags.items():
    if element:
        print(f"{tag.capitalize()}: {element.get('content')}")
    else:
        print(f"{tag.capitalize()} não encontrado.")

# Extraindo o título da página
title = soup.title.text
print("Título da Página:", title)

# Tentando localizar a data de lançamento e desenvolvedores no HTML
# (Adapte os seletores conforme necessário)
data_lancamento_element = soup.find(
    'a', href='/games/lib/popular/release_year_custom:2004/')
if data_lancamento_element:
    data_lancamento = data_lancamento_element.text
print("Data de Lançamento:", data_lancamento)

# Adapte o seletor abaixo com base na estrutura real da página para encontrar os desenvolvedores
# Por exemplo, pode estar em uma seção com uma classe específica.
desenvolvedores_element = soup.find(
    'div', class_="col-auto pl-lg-1 sub-title",)
if desenvolvedores_element:
    desenvolvedores = desenvolvedores_element.text.strip()
print("Desenvolvedores:", desenvolvedores)
