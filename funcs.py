import requests as req
import os
import csv
import json
from languages import languages

real_path = os.path.dirname(__file__)

def menu():
    print("MENU PRINCIPAL")
    print("1. Buscar Pais")
    print("2. Buscar Continente")
    print("3. Paises por idioma")
    print("4. Descargar bandera")
    print("5. Historial")
    print("6. Mostrar paises mas grandes")
    print("7. Mostrar paises con mayor poblacion")
    print("8. Idioma mas hablado")
    print("Q. Salir")

def ls_region():
    print("Africa")
    print("Americas")
    print("Asia")
    print("Europa")
    print("Oceania")

def add_csv(countrie):
    fileName = "./countries.csv"
    if os.path.exists(fileName) == True:
        with open("./countries.csv", "a", encoding="utf8", newline="") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(countrie)
    else:
        columns = ['name','capital','region','population','area','languages','flag']
        with open("./countries.csv", "a", encoding="utf8", newline="") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(columns)
            csv_writer.writerow(countrie)
    print("Historial actualizado...'")

def get_by_name(countrie_name):
    res = req.get(f"https://restcountries.eu/rest/v2/name/{countrie_name}").json()
    if type(res) == list:
        countrie = res[0]
        result = [countrie['name'], countrie['capital'], countrie['region'], countrie['population'], countrie['area'], countrie['languages'][0]['name'], countrie['flag']]
        add_csv(result)
        return result
    elif type(res) == dict:
        return res['message']

def write_data(region_name,res):
    with open(f"{real_path}/{region_name}.json", "w", encoding="utf8") as file:
        json.dump({"data": res}, file, ensure_ascii=False, indent=4)

def read_json(json_name):
    with open(f"{real_path}/{json_name}.json", encoding="utf8") as file:
        region = json.load(file)["data"]
    return region

def get_total_population(region):
    total_population = 0
    for countrie in region:
        total_population += countrie['population']
    return total_population

def get_by_region(region_name):
    res = req.get(f"https://restcountries.eu/rest/v2/region/{region_name}").json()
    print(type(res))
    if type(res) == list:
        write_data(region_name,res)
        result = read_json(region_name)
        print(res)
        print(get_total_population(result))
        return res
    elif type(res) == dict:
        return res['message']

def get_by_iso(user_language):
    for language in languages:
        if language[1].lower().find(user_language) == 0:
            return language[0]

def get_by_language(iso_language):
    res = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
    if type(res) == list:
        print(iso_language)
        return len(res)
    elif type(res) == dict:
        return res['message']

def down_flag(countrie):
    res = req.get(countrie[-1]).content
    with open(f"{real_path}/flags_download/{countrie[0].lower()}.svg", "wb") as file:
        file.write(res)

def read_csv(data):
    result = []
    with open(f'{real_path}/{data}', encoding="utf8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        result = [row for row in csv_reader]
        return result
        #result = [row for row in csv_reader if row[2] == 'Europe']
        # for row in csv_reader:
        #     result.append(row)
        # crear un filtro sobre una zona concreta

# def show_historial():
#     with open(f'{real_path}/countries.csv', encoding="utf8") as File:  
#         reader = csv.reader(File)
#         for row in reader:
#             if row[0] != 'name':
#                 print(f"name: {row[0]} - population: {row[3]}")
# Muestra el historial sin guardar en una lista

def show_historial(data):
    rows = read_csv(data)
    for row in rows:
        if row[0] != 'name':
                print(f"name: {row[0]} - population: {row[3]}")

def top_larges(user_search):
    res = req.get("https://restcountries.eu/rest/v2/all").json()
    res_sorted = sorted(res, key=lambda country: country['area'] if country['area'] != None else 0, reverse=True)[0:int(user_search)]
    return res_sorted
    
def top_population(user_search):
    res = req.get("https://restcountries.eu/rest/v2/all").json()
    res_sorted = sorted(res, key=lambda country: country['population'] if country['population'] != None else 0, reverse=True)[0:int(user_search)]
    return res_sorted

def count_languages():
    list_languages = []
    res = req.get("https://restcountries.eu/rest/v2/all").json()
    for row in res:
        list_languages.append(row['languages'][0]['name'])
    result_dict = dict( [ (i, list_languages.count(i)) for i in list_languages ] )
    order = dict(sorted(result_dict.items(),key= lambda tupla:tupla[1], reverse=True))
    print (order)