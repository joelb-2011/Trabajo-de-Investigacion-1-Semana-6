from py_cargo import Cargo

class Empleado:
  secuencia = 1
  Empleados = [{"codigo":1, "nombre":"Carlos", "cedula":"0975342713", "cargo":"Jefe", "departamento":"Vivienda Segura", "sueldo":3075.50}]
  
  def __init__(self, nombre, cedula, codCargo, codDepartamento, sueldo):
    Empleado.secuencia += 1
    self.codigo = Empleado.secuencia
    self.nombre = nombre
    self.cedula= cedula
    self.cargo = codCargo
    self.departamento = codDepartamento
    self.sueldo = sueldo
    
  def registro(self):
    return {"codigo": self.codigo, "nombre": self.nombre, "cedula": self.cedula, "cargo": self.cargo, "departamento": self.departamento, "sueldo": self.sueldo}