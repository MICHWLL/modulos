def saludar():
    print("hola perry,el ornitorrinco  ");

def saludarNombre(nombre):
    print(f"hola,{nombre}!")


# recorrer un iterable sin usar while o for , hacemos uso de las funciones iter () y next()

frutas=("pera")

frutas = iter(frutas)
print(next(frutas))
print(next(frutas))
print(next(frutas))
print(next(frutas))


#si el arreglo en la posicion 4 esta vacia, manda un error 
