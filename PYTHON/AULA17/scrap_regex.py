import requests
from bs4 import BeautifulSoup

# URL da página com a tabela de medalhas
url = 'https://en.wikipedia.org/wiki/2024_Summer_Olympics#Medal_table'

# Enviar a solicitação HTTP para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

# Analisar o conteúdo da página usando BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar a tabela com a classe correta
table = soup.find('table', {
                  'class': 'wikitable sortable sticky-header-multi plainrowheaders jquery-tablesorter'})

# Obter todas as linhas da tabela
rows = table.find_all('tr')

# Lista para armazenar os dados das medalhas
medal_list = []

# Iterar sobre as linhas da tabela e extrair os dados
for row in rows[1:11]:  # Começar da segunda linha para pular o cabeçalho
    cols = row.find_all('td')
    # Adicione uma verificação para garantir que a linha tem o número esperado de colunas
    if len(cols) >= 5:
        country = cols[0].get_text(strip=True)
        gold = cols[1].get_text(strip=True)
        silver = cols[2].get_text(strip=True)
        bronze = cols[3].get_text(strip=True)

        medal_list.append({
            'Country': country,
            'Gold': gold,
            'Silver': silver,
            'Bronze': bronze,
        })

# Exibir os resultados
for medal in medal_list:
    print(f"Country: {medal['Country']}, Gold: {medal['Gold']}, Silver: {
          medal['Silver']}, Bronze: {medal['Bronze']}")
