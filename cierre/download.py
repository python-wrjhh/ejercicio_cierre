import requests # importro el móodulo

url = "https://support.spatialkey.com/wp-content/uploads/2021/02/TechCrunchcontinentalUSA.csv" # defino la variable

r = requests.get(url,allow_redirects=True) # hago el get del link, y le digo que me permita el redirect.

file = []                                   # parseo la url para guardar el nombre real del file 
if url.find('/'):
    file = url.rsplit('/', 1)[1]           # el rsplit separa un string en una lista, separando por lo que vos le indiques en este caso un / empezando por la derecha el ",1"
                                        # me dice la cant de elementos que devuelve en este caso una lista de 2 elmentos. 

with open (file, "wb") as f:
    f.write(r.content)
    print (f"el file {file} ya fue bajado y guardado")