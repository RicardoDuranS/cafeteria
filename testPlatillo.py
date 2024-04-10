from Modelo.Platillo import Platillo
from Controller.PlatilloController import PlatilloController

plati = Platillo(
    nombre: Pasta 
    id: "1",
    descripcion: "Pasta hervida a su punto, con albóndigas", 
    foto: ""
)

plati2 = Platillo(
    nombre: Pizza,
    descripcion: "Deliciosa masa hecha en casa, con nuestra muy especial salsa de jitomate", 
    foto: ""
)

controller =  platilloController().guardar(plati2)
print(plati2)

controller =  platilloController().mostrar(plati)
print(plati)
