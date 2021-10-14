import csv
from collections import Counter
from os import read
import sys 

# https://www.kaggle.com/gpreda/reddit-vaccine-myths?select=reddit_vm.csv
filepath = "/home/nuxion/Projects/python-wrjhh/ejercicio_cierre"
with open(f"{filepath}/stop_en.txt", "r") as f:
    _words = f.read()

stop_words = _words.split()
textos = []
with open(f"{filepath}/reddit_vm.csv", "r") as f:
    csvreader = csv.reader(f)
    rows = []
    
    for row in csvreader:
        textos.append(row[6])

palabras = []
for frase in textos:
    lista_palabras = frase.split()
    for palabra in lista_palabras:
        if palabra.lower() not in stop_words:
            palabras.append(palabra)

top = Counter(palabras).most_common(5)
print(top)
