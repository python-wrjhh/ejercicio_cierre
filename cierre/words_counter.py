import csv

# https://www.kaggle.com/gpreda/reddit-vaccine-myths?select=reddit_vm.csv

with open("reddit_vm.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)


#with open("reddit_vm.csv", "r") as f:
#    texto = f.readlines()
#    for line in texto:
#        row = line.split(",")
#        print(row[0], row[1])
#