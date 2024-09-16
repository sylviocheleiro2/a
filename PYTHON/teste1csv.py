import csv

with open("arquivo.csv", newline='') as csvfile:
    leitor = csv.reader(csvfile)
    linha = [row for row in leitor]
    for row in linha:
       if linha[0] == "joao":
           linha[1] = "24"
with open("arquivo.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(linha)
