# La inmobiliaria "casa feliz", necesita desarrollar una aplicacion que permite controlar la venta de departamentos en un nuevo proyecto ubicado en su comuna.
# Este proyecto tiene a la venta 40 departamentos en un edificio de 10 pisos, donde cada piso se encuentran disponibles 4 dep.

# sistema debe permitir:

# comprar departamento 

# mostrar departamento disponible

# ver el listado de compradores 

# mostrar ganancias totales

# salir

# COMPRAR DEPARTAMENTO: EL SISTEMA DEBE SOLICITA AL CLIENTE EL DEP. A COMPRAR. EXISTEN 4 DEP. POR PISO. EN EL PISO 1 SE ENCUENTRA EL DEP. TIPO A, B, C Y D.

# SE DEBE INGRESAR EL PISO Y EL TIPO DEP QUE SE ADQUIRIRA.

# EL SISTEMA DESPLEGARA EN PANTALLA LOS DEP. QUE SE ENCUENTRAN DISPONIBLES Y LOS VENDIDOS MARCADOS CON UNA X

import numpy as np

flag = True

departamemtosDisponibles = [i for i in range (1, 41)]

departamentosComprados = []

#MOSTRAR DEPAS DISPO

def mostrarDepartamentosDisponibles():
  
  print("\nMOSTRANDO DEPARTAMENTOS DISPONIBLES: ")

  print(f"{departamemtosDisponibles}")
  
  print("""

  PISO  |         TIPO
        | A   |   B   |   C  |   D
  ---------------------------------
   10   |     |       |      |
  ---------------------------------
   9    |     |       |      |
  ---------------------------------
   8    |     |       |      |
  ---------------------------------
   7    |     |       |      |
  ---------------------------------
   6    |     |       |      |
  ---------------------------------
   5    |     |       |      |
  ---------------------------------
   4    |     |       |      |
  ---------------------------------
   3    |     |       |      |
  ---------------------------------
   2    |     |       |      |
  ---------------------------------
   1    |     |       |      |
  
  
  """)

#COMPRA DEPARTAMENTO

def comprarDepartamento():
  
    try:
      
      cantidadCompra = int(input("\nINGRESE LA CANTIDAD DE EDIFICIOS QUE QUIERA COMPRAR: "))
    
      tipoDepartamento = int(input("\nSELECCIONE EL TIPO DE DEPARTAMENTO QUE QUIERE: "))
  
      if tipoDepartamento == 1:
  
        totalA = cantidadCompra * 3800
  
        print(f"el total de la compra es: {totalA}")
  
      elif tipoDepartamento == 2:
  
        totalB = cantidadCompra * 3000
  
        print(f"el total de la compra es: {totalB}")
  
      elif tipoDepartamento == 3:
        
        totalC = cantidadCompra * 2800
  
        print(f"el total de la compra es: {totalC}")
  
      elif tipoDepartamento == 4:
        
        totalD = cantidadCompra * 3500
  
        print(f"el total de la compra es: {totalD}")
  
      else: 
  
        print("\nNUMERO INGRESADO INCORRECTO")
        
    except ValueError:
  
      print("CARACTER NO VALIDO")

#ASIGNAR DEPARTAMENTO 

def asignarDepartamento():

  while flag:

    departamento = int(input("\nINGRESE QUE DEPARTAMENTO QUIERE:"))
    
    if departamento in departamemtosDisponibles:
        
        rut = int(input("\nINGRESE A QUE RUT QUIERE EL DEPARTAMENTO:"))
  
        lista = [departamento, rut]
  
        departamentosComprados.append(lista)
      
        departamemtosDisponibles.pop(departamento -1)
  
        departamemtosDisponibles.insert(departamento -1, "X")

        return(departamentosComprados, departamemtosDisponibles)
  
    else:
  
      print("DEPARTAMENTO OCUPADO")
  
#MOSTRAR DEPARTAMENTOS DISPONIBLES

def verListadoCompradores():

  print(departamentosComprados)

#MENU 

def menu():
  
  
  print("""
  
             M   E   N   U
  
  [1]  COMPRAR DEPARTAMENTO
  
    [2]  MOSTRAR DEPARTAMENTO DISPONIBLE
  
       [3]  VER LISTADO DE COMPRADORES
  
          [4]  MOSTRAR GANANCIAS TOTALES
  
    [5]  SALIR
  
  """)


while flag:

  try:

    menu()
    
    opc = int(input("\nINGRESE LA OPCION DESEADA: "))

    if opc == 1:
      
      mostrarDepartamentosDisponibles()

      print("\nUSTED HA SELECCIONADO LA OPCION COMPRAR DEPARTAMENTO, SE LE ASIGNARA UN NUMERO")

      asignarDepartamento()

      comprarDepartamento()
      

    if opc == 2:

      print("\nUSTED HA SELECCIONADO LA OPCION COMPRAR MOSTRAR DEPARTAMENTOS DISPONIBLES: ")
      
      mostrarDepartamentosDisponibles()


    if opc == 3:

      print("\nUSTED HA SELECCIONADO LA OPCION MOSTRAR LISTADO DE COMPRADORES: ")

      verListadoCompradores()

    if opc == 5:

      break
    
  
  except ValueError:

    print("CARACTER NO VALIDO")


