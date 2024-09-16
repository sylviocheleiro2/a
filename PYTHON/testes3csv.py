import csv

with open("palavriado.csv", newline='') as csvfile:
    leitor = csv.reader(csvfile)
    palavras_lista = [row for row in leitor] #palavra feia
   

with open("comentario.txt", mode="r") as texto:
    palavras_feias = ["feio", "chato", "burro"]
    leitor = texto.readline()
    for palavra in palavras_feias:
        leitor = leitor.replace(palavra, "***")

    print(leitor)







    # palavras_feias = palavras_lista.split()
    # print(palavras_feias)

    # if palavras_feias in leitor:
    #     print(palavras_feias)
    # print(leitor)



# with open("arquivo.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(linha)