"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lst.append(row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        for element in lst:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, lst, lst1):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    lst : Archivo con la info de actores y director
    lst1 : Archivo con la info de genero,vote average , etc 
    """
    contador = 0 
    for renglon in lst :
        if criteria.lower() == renglon["director_name"].lower() :
            id = renglon["id"]
            for otros_renglones in lst1 :
                if otros_renglones["id"] == id :
                    puntaje = otros_renglones["vote_average"]
                    if float(puntaje) >= 6.0 :
                        contador += 1
    return contador


def main():
    lista = [] #instanciar una lista vacia
    lista1 = []
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                print("1) Cargar archivo MoviesCastingRaw-small ")
                print("2) Cargar archivo SmallMoviesDetailsCleaned")
                print("3) Cargar los dos archivos")
                i = input( "Seleccione una opcion ")
                if i == "1" :
                    loadCSVFile("Data/MoviesCastingRaw-small.csv", lista) #llamar funcion cargar datos
                    print("Datos cargados, "+str(len(lista))+" elementos cargados")
                elif i == "2" :
                    loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", lista1)
                    print("Datos cargados, "+str(len(lista1))+" elementos cargados")
                elif i == "3":
                    loadCSVFile("Data/MoviesCastingRaw-small.csv", lista) #llamar funcion cargar datos
                    print("Datos cargados del archivo MoviesCastingRaw-small , "+str(len(lista))+" elementos cargados")
                    loadCSVFile("Data/SmallMoviesDetailsCleaned.csv", lista1) 
                    print("Datos cargados del archivo SmallMoviesDetailsCleaned , "+str(len(lista1))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: 
                    print("1) Longitud del archivo MoviesCastingRaw-small ")
                    print("2) Longitud del archivo SmallMoviesDetailsCleaned")
                    print("3) Longitud de los dos archivos")
                    o = input("Seleccione una opcion ")
                    if o == "1" :
                        print("La lista tiene "+str(len(lista))+" elementos")
                    elif o == "2":
                        print("La lista tiene "+str(len(lista1))+" elementos")
                    elif o == "3":
                        print("El archivo MoviesCastingRaw-small tiene " + str(len(lista)) + " elementos")
                        print("El archivo SmallMoviesDetailsCleaned tiene " + str(len(lista1)) + " elementos")
            elif int(inputs[0])==3: #opcion 3
                print("1) Filtrar sobre el archivo MoviesCastingRaw-small")
                print("2) Filtrar sobre el archivo SmallMoviesDetailsCleaned")
                t = input("Seleccione una opcion : ")
                columna = input("Ingrese el nombre de la columna\n ")
                criteria =input('Ingrese el criterio de búsqueda\n')
                if t == "1":
                    counter=countElementsFilteredByColumn(criteria, columna, lista) #filtrar una columna por criterio
                    print("Coinciden ",counter," elementos con el criterio: ", criteria  )
                elif t == "2":
                    counter=countElementsFilteredByColumn(criteria, columna, lista1) #filtrar una columna por criterio
                    print("Coinciden ",counter," elementos con el criterio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                criteria =input('Ingrese el nombre del director\n')
                counter=countElementsByCriteria(criteria,lista,lista1)
                print("Coinciden ",counter," elementos con el criterio: '", criteria )
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
