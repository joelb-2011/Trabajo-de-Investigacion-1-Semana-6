from py_cargo import Cargo


class Empleado:
  secuencia=2             
  empleados = [ {"codigo":1,"nombre":"Maria","cedula":"0914192182","cargo":1,"departamento":1,"sueldo":500.50},
                {"codigo":2,"nombre":"Andy","cedula":"0985746875","cargo":2,"departamento":2,"sueldo":450.00}
              ]

  def __init__(self,nombre,cedula,codCargo,codDepartamento,sueldo):
    Empleado.secuencia +=1
    self.codigo=Empleado.secuencia
    self.nombre=nombre
    self.cedula=cedula
    self.cargo=codCargo
    self.departamento=codDepartamento
    self.sueldo=sueldo
  
    
  #def mostrar(self):
  #  print("{} - {} - {} - {} - {} ".format(self.codigo,self.descripcion,self.categoria,self.precio,self.stock))

  def registro(self):
    return [{"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento, "sueldo":self.sueldo}]
#print(Articulo.articulos)

# art = Articulo("Pepsi",2,1.5,100)
# #art.mostrar()
# articulo = art.registro()
# #print(articulo)
# Articulo.articulos.append(articulo)
# print(Articulo.articulos)