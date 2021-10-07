import csv
from collections import Counter
from os import read

# https://www.kaggle.com/gpreda/reddit-vaccine-myths?select=reddit_vm.csv

with open("../reddit_vm.csv", "r") as f:
    csvreader = csv.reader(f)
    rows = []
    
    for row in csvreader:
        rows.append(row)

body = []
for i in rows:
    body.append(i[6])

# Creo una nueva lista
palabras = []
# Itero sobre mi lista creada del body for words in body:
for words in body:
    #hago un split de los strings en una nueva lista de palabras
    listapalabras = words.split()
    #extend newlist to include all itemWords
    palabras.extend(listapalabras)
print(palabras[3])


with open("../stop_en.txt", "r") as f:
    text = f.read()


#c = Counter()
#numero = Counter(palabras).most_common(5)

top_5 = []
for element in text:
    if element in palabras:
        top_5.append(element)
    else
    



#with open("reddit_vm.csv", "r") as f:
#    texto = f.readlines()
#    for line in texto:
#        row = line.split(",")
#        print(row[0], row[1])
#