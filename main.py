# https://github.com/vgenov-py/T-522/blob/master/countries.md

import requests as req
import funcs
import csv

option_exit = True

while option_exit == True:
    funcs.menu()
    user_option = input("Introduzca una opcion: ").upper()

    if user_option == 'Q':  #Exit
        option_exit = False # Salir del programa
        print("Cerrando aplicacion...")
    elif user_option == '1':    #Buscar por pais
        print("OPCION BUSCAR PAIS")
        user_search = input("Pais: ")
        print(funcs.get_by_name(user_search))
    elif user_option == '2':    #Opcion Continente
        print("OPCION CONTINENTE")
        user_search = input("Continente: ")
        funcs.get_by_region(user_search)
    elif user_option == '3':    #Opcion idioma
        print("OPCION IDIOMA")
        user_search = input("Idioma: ")
        iso_language = funcs.get_by_iso(user_search)
        print(funcs.get_by_language(iso_language))       
    elif user_option == '4':
        print("OPCION DESCARGAR BANDERA")
        user_search = input("Introduzca pais para descargar la bandera: ")
        result = funcs.get_by_name(user_search)
        print(result[0], ":", result[-1])
        funcs.down_flag(result)
    elif user_option == '5':
        print("OPCION HISTORIAL")
        funcs.show_historial("./countries.csv")
    elif user_option == '6':  
        print("TOP PAISES MAS GRANDES:")
        user_search = input("Introduzca numero de paises a mostrar: ")
        print(funcs.top_larges(user_search))
    elif user_option == '7':
        print("TOP PAISES MAS POBLADOS:")
        user_search = input("Introduzca numero de paises a mostrar: ")
        print(funcs.top_population(user_search))
    elif user_option == '8':
        print("IDIOMA MAS HABLADO:")
        funcs.count_languages()


