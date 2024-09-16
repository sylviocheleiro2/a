import re
import requests
from bs4 import BeautifulSoup

# URL da página com a tabela de medalhas
url = 'https://en.wikipedia.org/wiki/2024_Summer_Olympics#Medal_table'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Enviar a solicitação HTTP para obter o conteúdo da página
response = requests.get(url, headers=headers)
response.raise_for_status()

# Ler o conteúdo da página
web_content = response.text

# Usar regex para encontrar a tabela
# Nota: regex para HTML é sempre arriscado e pode não ser confiável em HTML complexo
pattern = re.compile(
    r'<table[^>]*class="wikitable sortable sticky-header-multi plainrowheaders jquery-tablesorter[^"]*"[^>]*>(.*?)</table>', re.DOTALL)

# Encontrar a tabela na página
matches = pattern.findall(web_content)

# Se não encontrar a tabela, exibir mensagem
if not matches:
    print("Tabela não encontrada")
    exit()

# Para analisar a tabela HTML, vamos usar BeautifulSoup novamente
# porque regex não é confiável para parsing de HTML complexo
table_html = matches[0]  # Supondo que queremos a primeira tabela encontrada

# Analisar o HTML da tabela com BeautifulSoup
table_soup = BeautifulSoup(table_html, 'html.parser')

# Lista para armazenar os dados das medalhas
data = []

# Obter todas as linhas da tabela
rows = table_soup.find_all('tr')

# Iterar sobre as linhas da tabela e extrair os dados
for row in rows[1:11]:  # Começar da segunda linha para pular o cabeçalho
    cols = row.find_all('td')
    if len(cols) >= 5:
        # Ajustado para a primeira coluna
        country = cols[0].get_text(strip=True)
        gold = cols[1].get_text(strip=True)
        silver = cols[2].get_text(strip=True)
        bronze = cols[3].get_text(strip=True)
        total = cols[4].get_text(strip=True) if len(cols) > 4 else 'N/A'

        data.append({
            'Country': country,
            'Gold': gold,
            'Silver': silver,
            'Bronze': bronze,
            'Total': total
        })

# Exibir os resultados
for item in data:
    print(f"Country: {item['Country']}, Gold: {item['Gold']}, Silver: {
          item['Silver']}, Bronze: {item['Bronze']}, Total: {item['Total']}")
