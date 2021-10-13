#Importando la libreria necesaria para el manejo de archivos csv
import csv 


lista_datos = [] #Creando una lista para guardar los registros de la base de datos

#Leyendo el archivo y guardando en una lista los registros
with open('synergy_logistics_database.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    skip = 0
    for linea in lector:
        if skip == 0:
            skip += 1
        else:
            lista_datos.append(linea)

#Opción 1) Rutas de importación y exportación.
        

#Haciendo registro de las rutas
#Generando variable de busqueda de sentido 
def rutas_demanda(direccion): #Definiendo una función que genere las listas para opcion 1
    rutas_conteo = [] # Lista para guardar la ruta y cuantas veces se repite
    contador = 0 # Variable para contar el número de veces que una ruta se presenta
    valor = 0 #Variable para sumar el valor de la exportacion
    rutas_contadas = [] #Lista para guardar las listas que ya han sido registradas
    
    for ruta in lista_datos:
        ruta_actual  = [ruta[2],ruta[3]]
        if ruta[1] == direccion and ruta_actual not in rutas_contadas:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2],movimiento[3]] and movimiento[1] == direccion:
                    contador += 1
                    valor += int(movimiento[9])        
                    rutas_contadas.append(ruta_actual)
            formato = [ruta[2],ruta[3],contador,valor]
            rutas_conteo.append(formato)
            contador = 0
            valor = 0
    
    sorted(rutas_conteo,reverse=True,key=lambda x:x[2]) #Ordenando las rutas por su conteo
    count = 0
    for i in rutas_conteo:
        if count < 10:    
            print(i[0],i[1])
            count += 1
    print('')
#Opción 2) Medio de transporte utilizado.

def transportes_demanda(direccion): #Definiendo una función que genere las listas para opcion 2
    transporte_valor = [] # Lista para guardar la ruta y su valor total por sentido logistico
    valor = 0 # Variable para contar el número de veces que una ruta se presenta
    transporte_valuado = [] #Lista para guardar las listas que ya han sido registradas
    
    for transporte in lista_datos: #creando a lista de los transportes y su valor
        transporte_actual  = [transporte[7]]
        if transporte[1] == direccion and transporte_actual not in transporte_valuado:
            for movimiento in lista_datos:
                if transporte_actual == [movimiento[7]] and movimiento[1] == direccion:
                    valor += int(movimiento[9])        
                    transporte_valuado.append(transporte_actual)
            formato = [transporte[7],valor]
            transporte_valor.append(formato)
            valor = 0
    
    sorted(transporte_valor,reverse=True,key=lambda x:x[1]) #Ordenando las rutas 
    
    print(f'Los tres medios de transporte más importantes de las {direccion}')
    count = 0
    for i in transporte_valor:
        if count < 3:    
            print(i[0],i[1])
            count += 1
    print('')
    
#Opción 3) Valor total de Imports y Exports.

def paises_demanda(direccion): #Definiendo una función que genere las listas para opcion 3
    pais_valor = [] # Lista para guardar el pais y su valor total por sentido logistico
    pais_porcentaje = []
    valor = 0 # Variable para contar el número de veces que una ruta se presenta
    pais_valuado = [] #Lista para guardar las listas que ya han sido registradas
    suma_total = 0
    if direccion == "Exports":
        indice = 2
    elif direccion == "Imports":
        indice = 3
    for pais in lista_datos:
        pais_actual  = pais[indice]
        if pais[1] == direccion and pais_actual not in pais_valuado:
            for movimiento in lista_datos:
                if pais_actual == movimiento[indice] and movimiento[1] == direccion:
                    valor += int(movimiento[9])
                    suma_total += int(movimiento[9])
                    pais_valuado.append(pais_actual)
            formato = [pais_actual,valor]
            pais_valor.append(formato)
            valor = 0
    suma_total
    pais_valor.sort(reverse=True,key=lambda x:x[1]) #Ordenando las rutas por su conteo
    porcentaje = 0  
    for pais in pais_valor: # Se crea una lista ordenada solo con los paises que suman el 80%
        if porcentaje < 80:
            porc = (pais[1]/suma_total)*100
            pais_porcentaje.append([pais[0],porc])
            porcentaje += porc
    print(f'Los países con el 80% del valor de las {direccion}')
    for i in pais_porcentaje:
        print(i[0],f'{i[1]}%')
    print('')
    return pais_porcentaje

print("Bienvenidoo al sistema de Synergy Logistics")
opcion = 0 
while opcion != 4:
        print(""" --- Selecciona una opción ---
            [1] Listado rutas de Importación y Exportación
            [2] Listado medio de transporte utilizado
            [3] Total de Importaciones y Exportaciones 
            [4] Salir
            """)

        opcion = input("Ingresar una opción: ")
        if opcion.isnumeric():
            if opcion == "1":
                print("Rutas de exportaciones: \n")
                rutas_demanda("Exports") # Llama a la funcion
                print("Rutas de importaciones: \n")
                rutas_demanda("Imports") # Llama a la funcion
            elif opcion == "2":
                transportes_demanda("Exports") # Llama a la funcion
                transportes_demanda("Imports") # Llama a la funcion
            elif opcion == "3":
                paises_demanda("Exports") # Llama a la funcion 
                paises_demanda("Imports") # Llama a la funcion 
            elif opcion == "4": # Sale del menu y cierra programa.
                print("Sesión terminada...")
                break
            else :
                opcion = input("Selecciona una opción válida")

