#Importar librerias
import csv
import os
import time
import random
#funcion para limpiar pantalla
def Limpiar_pantalla():
    time.sleep(1)
    os.system("cls")
#Lista de trabajadores
TRABAJADORES = [
    "Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    ]
#Menu
def main():
    archivo="Reporte_sueldo.csv"
    while True:
        print("1.Asignar sueldos aleatorios")
        print("2.Clasificar sueldos")
        print("3.Ver estadisticas")
        print("4.Reporte de sueldo")
        print("5.Salir del programa")
        try:
            opc = int(input("Elija una opcion: "))
        except ValueError:
            print("Elija un numero del 1 al 5")
        if opc == 1:
            Asignar_sueldos_aleatorios()
        elif opc == 2:
            Clasificar_Sueldos()
        elif opc == 3:
            Ver_estadistica()
        elif opc == 4:
            Reporte_de_sueldos(archivo)
        elif opc == 5:
            Salir_Programa()
            break            



#Funcion para asignar sueldos aleatorios
def Asignar_sueldos_aleatorios():
    Sueldos_aleatorios=[]
    Sueldos_aleatorios.append(TRABAJADORES)
    for i in range(10):
        for i in TRABAJADORES:
            sueldos = random.randint(300000,2500000)
            Sueldos_aleatorios.append(sueldos)
    print(Sueldos_aleatorios)
    
    
#Funcion para Clasificar sueldo
def Clasificar_Sueldos():
    Limpiar_pantalla()
    Bajo=[]
    promedio=[]
    alto=[]
    #if Sueldo < 800000:
        #print(f"Nombre {TRABAJADORES}",f"Sueldo {Sueldos_aleatorios}")
    #elif Sueldo_aleatorio >= 800000 and Sueldo_aleatorio <= 2000000:
        #print(f"Nombre {TRABAJADORES}",f"Sueldo {Sueldo_aleatorio}")
    

#funcion para ver el sueldo mas bajo el promedio y el mas alto
def Ver_estadistica():
    Limpiar_pantalla()
    media_geometrica()#dentro de la funcion se le agrega el argumento de Bajo,promedio,alto
#Funcion para sacar la media geometrica    
def media_geometrica(data):
    producto=1
    for valor in data:
        producto += valor
        return producto**(1/len(data))

    
#Funcion para mostrar detalle de sueldo y guardar en csv
def Reporte_de_sueldos(archivo_csv):
    Limpiar_pantalla()
    #Desc_salud=0.7*Sueldo_aleatorio
    #Desc_afp=0.12*Sueldo_aleatorio
    #Sueldo_Liquido=Desc_salud-Desc_afp-Sueldo_aleatorio
    with open(archivo_csv,"a",newline="")as archivo:
        campos=["Nombre Empleado","Sueldo Base","Descuento salud","Descuento AFP","Sueldo Liquido"]
        writer=csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()

#Funcion para salir del programa
def Salir_Programa():
    Limpiar_pantalla()
    print("Finalizando Programa....\nDesarrollado por Samuel Mansilla\nRut 24.655.835-3")
    
if __name__=="__main__":
    main()