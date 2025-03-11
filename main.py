#Datos de Entrada
productos=[]
contador_id=1

#Procesos
def agregar_producto():
    global contador_id
    nombre=input("Ingrese el nombre del producto: ")
    cantidad=int(input("Ingrese la cantidad que llevara: "))
    precio=int(input("Ingrese su precio: "))
    presentacion=input("Cual es la presentación del producto: ")
    productos.append({"id":contador_id,"nombre":nombre,"cantidad":cantidad,"precio":precio,"presentacion":presentacion})
    contador_id+=1

def ver_producto():
    print("\n Lista de Productos: ")
    if len(productos)==0:
        print("No hay productos agregados")
    else:
        for producto in productos:
            print(f"{producto['id']}.{producto['nombre']}-{producto['cantidad']}-${producto['precio']}-{producto['presentacion']}")    

#Datos de salida
opcion=0
while opcion !=5:
    print("\n1. Agregar productos\n2. Ver la lista de productos\n3. Editar el producto\n4. Eliminar un producto\n5. Salir")
    opcion=int(input("Elija una opción: "))
    if opcion==1:
        agregar_producto()
    elif opcion==2:
        ver_producto()
    elif opcion==5:
        print("Salir del programa")
    else:
        print("Opción inválida")    
                    
            



