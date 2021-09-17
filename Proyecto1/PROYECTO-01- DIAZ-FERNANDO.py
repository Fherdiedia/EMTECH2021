#Listas importadas requeridas para el analisis
from lifestore_file import lifestore_products
from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales

total_products = len(lifestore_products) # Número de productos que se venden
# Crear listas para contar las busquedas y scores.
count_searches = []
count_score = []
for n in range(total_products):
    count_searches.append([n+1,0,lifestore_products[n][1]])
    count_score.append([n+1,0,0,lifestore_products[n][1]])
    for search in lifestore_searches:
        if search[1] == count_searches[n][0]:
            count_searches[n][1] += 1
    for search in lifestore_sales:
        if search[1] == count_score[n][0]:
            count_score[n][1] += search[2]
            count_score[n][2] += 1
#Se seaparan los productos de los que sí tienen busquedas de los que no.
without_searches = []
with_searches = []
with_searches_copy =[]
for count in count_searches:
    if count[1] != 0:
        with_searches.append(count)
        with_searches_copy.append(count)
    else:
        without_searches.append(count)
ord_search_less = []
ord_search_more = []
#Se ordenan los valores de menor busqueda a mayor busqueda
while with_searches:
    minimo = with_searches[0][1]
    searches_actual = with_searches[0]
    for search in with_searches:
        if search[1] < minimo:
            minimo = search[1]
            searches_actual = search
    ord_search_less.append(searches_actual)
    with_searches.remove(searches_actual)
#Se ordenan los valores de mayor busqueda a menor
while with_searches_copy:
    maximo = with_searches_copy[0][1]
    searches_actual = with_searches_copy[0]
    for search in with_searches_copy:
        if search[1] > maximo:
            maximo = search[1]
            searches_actual = search
    ord_search_more.append(searches_actual)
    with_searches_copy.remove(searches_actual)
vendidos = []
vendidos_copy = []
promedio = []
promedio_copy = []
sin_registro = []
for score in count_score:
    if score[2] != 0:
        vendidos.append([score[0],score[2],score[3]])
        vendidos_copy.append([score[0],score[2],score[3]])
        promedio.append([score[0], round(score[1]/score[2],2),score[3]])
        promedio_copy.append([score[0], round(score[1]/score[2],2),score[3]])
    else:
        sin_registro.append([score[0], "Sin registro de venta"])
#Se ordenan productos mas vendidos, score de mayoor a menor y viceversa
mas_vendidos = []
menos_vendidos = []
promedio_mas = []
promedio_menos = []
while vendidos:
    minimo = vendidos[0][1]
    ventas_actual = vendidos[0]
    for ventas in vendidos:
        if ventas[1] < minimo:
            minimo = ventas[1]
            ventas_actual = ventas
    menos_vendidos.append(ventas_actual)
    vendidos.remove(ventas_actual)
while promedio_copy:
    maximo =promedio_copy[0][1]
    promedio_actual = promedio_copy[0]
    for puntuacion in promedio_copy:
        if puntuacion[1] > maximo:
            maximo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_mas.append(promedio_actual)
    promedio_copy.remove(promedio_actual)
while promedio:
    minimo = promedio[0][1]
    promedio_actual = promedio[0]
    for puntuacion in promedio:
        if puntuacion[1] < minimo:
            minimo = puntuacion[1]
            promedio_actual = puntuacion
    promedio_menos.append(promedio_actual)
    promedio.remove(promedio_actual)
while vendidos_copy:
    maximo = vendidos_copy[0][1]
    vendidos_actual = vendidos_copy[0]
    for ventas in vendidos_copy:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    mas_vendidos.append(vendidos_actual)
    vendidos_copy.remove(vendidos_actual)
#Se crean listas para el calculo de ventas por mes y anual, tambien se ordenan de mayor a menor
by_date = []
for sale in lifestore_sales:
    by_date.append([lifestore_products[sale[1]-1][2],sale[3][3:],sale[4]])
month_list = []
year_list= []
for month in by_date:
    if not month[1] in month_list:
        month_list.append(month[1])
    if not month[1][-4:] in year_list:
        year_list.append(month[1][-4:])
contador_ventas_mensual = []
for month in month_list:
    contador_ventas_mensual.append([month, 0])
for sale in by_date:
    for month in contador_ventas_mensual:
        if sale[1] == month[0]:
            month[1] += sale[0]
contador_ventas_anual = []
for year in year_list:
    contador_ventas_anual.append([year,0,0])
for sale in contador_ventas_mensual:
    for year in contador_ventas_anual:
        if sale[0][-4:] == year[0]:
            year[1] += sale[1]
            year[2] += 1
meses_mayor_ventas = []
while contador_ventas_mensual:
    maximo = contador_ventas_mensual[0][1]
    vendidos_actual = contador_ventas_mensual[0]
    for ventas in contador_ventas_mensual:
        if ventas[1] > maximo:
            maximo = ventas[1]
            vendidos_actual = ventas
    meses_mayor_ventas.append(vendidos_actual)
    contador_ventas_mensual.remove(vendidos_actual)
meses = ["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio", "Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]

# Pantalla de inicio lifestore.
print("¡Bienvenido al sitio de análisis de ventas de Lifestore!")


# Ingresar usuario y contraseña para el sistema
usuario = input("Ingresa el usuario: ")
password = input("Ingresa la contraseña: ")

es_admin = 0  # Si es 1, es admin. Si es 0, no lo es.
intentos = 0  #Contador para evitar el exceso de intentos y saldra del programa si pasa de ellos.

while usuario != "Admin" and password != "lifestore01" and intentos <2:
    print("Datos incorrectos, vuelva a intentar")
    usuario = input("Ingresa el usuario: ")
    password = input("Ingresa la contraseña: ")
    intentos += 1

if usuario == "Admin" and password == "lifestore01":
    es_admin = 1

# Si el usuario esta autorizado, pasa al menu de opciones.
opcion = 0
if es_admin == 1:
    while opcion != 4:
        print(""" --- Selecciona una opción ---
            [1] Listado ventas de productos
            [2] Listado reseñas de productos
            [3] Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año
            [4] Salir
            """)

        opcion = input("Ingresar una opción: ")


        eleccion = 0
        if opcion.isnumeric():
            if opcion == "1": # 3Ingresa al submenu Listao ventas de productos.
                while eleccion != "3":
                    print(""" --- Selecione lo que desea imprimir ---
                    [1] Lista de más vendidos y más buscados.
                    [2] Lista de menos vendidos y menos buscados.
                    [3] Regresar
                    """)
                    eleccion = input("Ingresa una opción: ")
                    if eleccion == "1": # Ingresa a Lista de más vendidos y más buscados.
                    # Más vendidos
                        print("{} más vendidos:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(mas_vendidos[n][1]),mas_vendidos[n][2].split(",")[0]))
                    # Mas buscados
                        print("{} más buscados:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(ord_search_more[n][1]),ord_search_more[n][2].split(",")[0]))
                    elif eleccion == "2": #Ingresa a Lista de menos vendidos y menos buscados.
                    # Menos vendidos
                        print("{} menos vendidos:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} piezas se vendieron de {}".format(str(n+1),str(menos_vendidos[n][1]),menos_vendidos[n][2].split(",")[0]))
                    # Menos buscados
                        print("{} menos buscados:".format(10))
                        for n in range(10):
                            print("{:>2s}. {:>3s} busquedas de {}".format(str(n+1),str(ord_search_less[n][1]),ord_search_less[n][2].split(",")[0]))
                    elif eleccion == "3": # Regresa al menu antetrior.
                        continue
                    else:
                        print("Ingrese una opción valida")
            elif opcion == "2":
                #Mejores reseñas
                print("{} Mejores reseñas:".format(20))
                for n in range(20):
                    print("{:>2s}. Calificación {:>2s}/5 de {}".format(str(n+1),str(promedio_mas[n][1]),promedio_mas[n][2].split(",")[0]))
                # Peores reseñas
                print("{} Peores reseñas:".format(20))
                for n in range(20):
                    print("{:>2s}. Calificación {:>2s}/5  de {}".format(str(n+1),str(promedio_menos[n][1]),promedio_menos[n][2].split(",")[0]))
            elif opcion == "3":
                #Ventas, anuales y mensuales
                print("Ventas anuales")
                for year in contador_ventas_anual:
                    print("{}: $ {},{}.00".format(year[0],str(year[1])[:-3],str(year[1])[-3:]))
                print("Promedio mensual")
                for year in contador_ventas_anual:
                    promedio_mensual = str(round(year[1]/year[2],2))
                    print("{}: $ {}".format(year[0],promedio_mensual))
                print("Ventas por mes")
                indice = 0
                for mes in meses_mayor_ventas:
                    indice += 1
                    a = int(mes[0][:2])-1
                    print("{:>2s}. {:>10s} {}: ${},{}.00".format(str(indice),meses[a],mes[0][-4:],str(mes[1])[:-3],str(mes[1])[-3:]))
            elif opcion == "4": #Sale del menu y cierra programa.
                print("Sesion terminada...")
                break

            else:
                print("Opción no valida.")