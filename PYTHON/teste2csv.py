#estoque de livros em csv
# ler o csv e armazenar os dados num dict
#verificar se a quantidade do livro é menor q 3 se for avisar
import csv

novos_livros = [
    {"Titulo": "O Morro dos Ventos Uivantes", "Autor": "Emily Brontë", "Quantidade": 1},
    {"Titulo": "A Revolução dos Bichos", "Autor": "George Orwell", "Quantidade": 2},
]


with open("livros.csv", mode='a', newline='') as file:
    campos = ["Titulo", "Autor", "Quantidade"]
    escritor = csv.DictWriter(file, fieldnames=campos)
    escritor.writerows(novos_livros)


with open("livros.csv", "r", newline='') as file:
    leitor = csv.DictReader(file)
    for linha in leitor:
        titulo = linha["Titulo"]
        autor = linha["Autor"]
        quantidade = linha["Quantidade"]
        print(linha)
    
 
   
   