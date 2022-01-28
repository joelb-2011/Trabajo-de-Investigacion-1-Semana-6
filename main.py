from helpers import Helper
from py_departamento import Departamento
from py_empleado import Empleado
from py_cargo import Cargo
import os
  
def buscategoria(cod):
  cat = 0     
  for pos in range(0,len(Cargo.cargos)):
    categoria = Cargo.cargos[pos]
    if categoria["codigo"] == cod:
       cat = categoria["descripcion"]
       break
  return cat    
helper = Helper()
lista = ["1) Cargos","2) Departamentos","3) Empleados","4) Salir del programa"]
opcion=""
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,"Menu Principal")
  
  if opcion == "1":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Atras"],"Menu Cargos")
      os.system("cls")
      if opc1 == "1":
        print("Ingreso de Cargo")
        nombre= input("Nombre del Cargo: ")
        cat = Cargo(nombre)
        cate = cat.registro()
        Cargo.cargos.append(cat)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("Consulta de Cargo")
        print("Codigo"," "*5,"Descripcion")
        for emp in Cargo.cargos:
          cod = emp["codigo"]
          des = emp["des"]
          print(" "*2,cod," "*8,nom," "*(15-len(des)))
        input("Presione una tecla para continuar...")
        
  
  elif opcion == "2":
    print("Mantenimiento de Departamentos")
    if opc1 == "1":
      print("Ingreso de Departamento")
      nombre= input("Nombre del Departamento: ")
      cat = Departamento(nombre)
      cate = cat.registro()
      Departamento.cargos.append(cat)
      input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
  
  elif opcion == "3":
    
      print("Menu de Empleados")
      if opc1 == "1":
        print("Ingreso de Empleados")
        nombre= input("Nombre del Empleado: ")
        cedula= int(input("Cedula del Empleado: "))
        cargo= int(input("Cargo del Empleado: "))
        departamento= input("Departamento del Empleado: ")
        sueldo= float(input("Sueldo del Empleado: "))
        emp = Empleado(nombre,cedula,cargo,departamento,sueldo)
        empleado = emp.registro()
        Empleado.empleados.append(empleado)
        input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      elif opc1 == "2":
        print("="*20,"Consulta de Empleados","="*20)
        print("Codigo"," "*5,"Nombre"," "*5,"Cedula","     Cargo   ","  Departamento", " "*5, "Sueldo")
        for emp in Empleado.empleados:
          cod = emp["codigo"]
          nom = emp["nombre"]
          ced = emp["cedula"]
          cedd = buscategoria(ced)
          car = emp["cargo"] 
          dep = emp["departamento"] 
          sue = emp["sueldo"] 
          print(" "*2,cod," "*8,nom," "*(15-len(nom)),cedd," "*(15-len(cedd)),car," "*(8-len(str(car))),dep,sue)
        input("Presione una tecla para continuar...")
  
  elif opcion == "4":
    print("Salir")
        
print("Gracias por visitarnos")  
#print(Articulo.articulos)

