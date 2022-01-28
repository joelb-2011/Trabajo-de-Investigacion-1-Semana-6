from py_cargo import Cargo
from py_departamento import Departamento
from py_empleados import Empleado
from helpers import Helper

import os

def buscarCargo(cod):
  car = 0
  for pos in range (0, len(Cargo.cargos)):
    cargo = Cargo.cargos[pos]
    if cargo["cargo"] == cod:
      car = cargo["cargo"]
      break
  return car

def buscarDepartamento(dep):
  dept = 0
  for pos in range (0, len(Departamento.departamentos)):
    depar = Departamento.departamentos[pos]
    if depar["nombre"] == dep:
      dept = depar["nombre"]
      break
  return dept

helper = Helper()
lista = ["1) Cargo", "2) Departamento", "3) Empleados", "4) Salir del programa"]
opcion = ""

while opcion !="4":
  os.system("cls")
  opcion = helper.menu(lista, "Menú Principal")
  os.system("cls")
  if opcion == "1":
    opc1 = ""
    while opc1 != 3:
      os.system("cls")
      print("Mantenimiento De Cargos", "=" * 40)
      opc1 = helper.menu(["1) Ingreso", "2) Consulta", "3) Atrás"], "Menú Cargo")
      os.system("cls")
      if opc1 == "1":
        print("Ingreso De Cargos", "-" * 40)
        nombre = input("Nombre del cargo: ")
        val = len(nombre)
        while not val > 2 and val <= 20:
          nombre = input("Nombre del cargo: ")
          val = len(nombre)
        crg = Cargo(nombre)
        carg = crg.registro()
        Cargo.cargos.append(carg)
        input("\n"
          "Los datos han sido ingresados exitosamente. Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "2":
        print("Lista completa de Cargos", "-" * 40)
        print("Código"," "*5,"Descripción")
        print("=" * 60)
        for crg in Cargo.cargos:
          codi = crg ["codigo"]
          desc= crg ["cargo"]
          codig = buscarCargo(desc)
          print(" " * 2, codi, " " * 8, codig)
        print("-"*60)
        input("\n"
         "Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "3":
        input("Espere un momento, por favor." 
        "\n" "Presione cualquier tecla para continuar.")
        break

  elif opcion == "2":
    os.system("cls")
    opc1 = ""
    while opc1 != 3:
      os.system("cls")
      print("Mantenimiento De Departamentos", "=" * 40)
      opc1 = helper.menu(["1) Ingreso", "2) Consulta", "3) Atrás"], "Menú Departamento")
      os.system("cls")
      if opc1 == "1":
        print("Ingreso De Departamentos", "-" * 40)
        nombre = input("Nombre del departamento: ")
        val = len(nombre)
        while not val > 5 and val <= 20:
          nombre = input("Nombre del departamento: ")
          val = len(nombre)
        dpt = Departamento(nombre)
        depa = dpt.registro()
        Departamento.departamentos.append(depa)
        input("\n"
          "Los datos han sido ingresados exitosamente. Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "2":
        print("Lista completa de Departamentos", "-" * 40)
        print("Departamento", " " * 5, "Nombre") #," ")
        print("=" * 60)
        for dpt in Departamento.departamentos:
          depta = dpt ["departamento"]
          dnom = dpt ["nombre"]
          nomd = buscarDepartamento(dnom)
          print(" " * 4, depta, " " * 8, nomd)
        print("-" * 60)
        input(
        "\n" "Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "3":
        input("Espere un momento, por favor." 
        "\n" "Presione cualquier tecla para continuar.")
        break
        
  elif opcion == "3":
    os.system("cls")
    opc1 = ""
    while opc1 != 3:
      os.system("cls")
      print("Mantenimiento De Empleados", "=" * 40)
      opc1 = helper.menu(["1) Ingreso", "2) Consulta", "3) Atrás"], "Menú Empleados")
      os.system("cls")
      if opc1 == "1":
        print("Ingreso De Empleados", "-" * 40)
        nombre= input("Nombre del empleado: ")
        val = len(nombre)
        while not val >= 3 and val <= 20:
          print("El nombre ingresado es demasiado corto o largo. Por favor, inténtalo otra vez.")
          nombre = input("Nombre del empleado: ")
          val = len(nombre)
        cedula= input("Cédula del empleado: ")
        val = len(cedula)
        while val != 10:
          print("La cédula ingresada no es válida. Por favor, inténtalo otra vez.")
          cedula = input("Cédula del empleado: ")
          val = len(cedula)
        codCargo = input("Cargo del empleado: ")
        car = buscarCargo(codCargo)
        while car != codCargo:
          print("El cargo ingresado no existe o no ha sido añadido al sistema. Por favor, inténtalo otra vez.")
          codCargo = input("Cargo del empleado: ")
          car = buscarCargo(codCargo)
        codDepartamento = input("Departamento del empleado: ")
        dept = buscarDepartamento(codDepartamento)
        while dept != codDepartamento:
          print("El departamento ingresado no existe o no ha sido añadido al sistema. Por favor, inténtalo otra vez.")
          codDepartamento= input("Departamento del empleado: ")
          dept = buscarDepartamento(codDepartamento)
        sueldo = float(input("Sueldo del empleado: "))
        while sueldo %1 == 0:
          print("El sueldo ingresado no es válido. Por favor, inténtalo otra vez.")
          sueldo = float(input("Sueldo del empleado: "))
        empl = Empleado(nombre, cedula, codCargo, codDepartamento, sueldo)
        empleado = empl.registro()
        Empleado.Empleados.append(empleado)
        input("\n"
        "Los datos han sido ingresados exitosamente. Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "2":
        print("Lista completa de Empleados", "-" * 40)
        print("Código", " " * 6, "Nombre", " " * 6, "Cédula", " " * 6, "Cargo", " " * 6, "Departamento", " " * 6, "Sueldo")
        print("=" * 90)
        for empl in Empleado.Empleados:
          codigo = empl["codigo"]
          desno = empl["nombre"]
          ced = empl["cedula"] 
          cgo = empl["cargo"]
          bcg = buscarCargo(cgo)
          detm = empl["departamento"]
          bdp = buscarDepartamento(detm)
          suel = empl["sueldo"]
          print(" " * 2, codigo, " " * 8, desno, " " * (10-len(desno)), ced, " " * (14-len(ced)), bcg," " * (11-len(bcg)), bdp, " " * (18-len(bdp)), suel)
        print("-" * 90)
        input("\n"
          "Por favor, presione cualquier tecla para continuar.")
      elif opc1 == "3":
        input("Saliendo... Un momento, por favor." 
        "\n" "Presione cualquier tecla para continuar.")
        break
  elif opcion == "4":
    print("¡Muchas gracias! ¡Vuelva pronto!")