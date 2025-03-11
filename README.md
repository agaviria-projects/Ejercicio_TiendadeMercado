Gestión de Productos
Este programa en Python permite gestionar una lista de productos mediante un menú interactivo. Los usuarios pueden agregar productos, ver la lista de productos almacenados y salir del programa.

Estructura del Código
Datos de Entrada
Se utiliza una lista productos para almacenar los productos.
La variable contador_id se usa para asignar un ID único a cada producto.
⚙️ Procesos
agregar_producto()

Solicita al usuario que ingrese el nombre, cantidad, precio y presentación del producto.
Guarda la información en un diccionario dentro de la lista productos.
Asigna un ID único automáticamente a cada producto.
ver_producto()

Muestra la lista de productos almacenados en la lista productos.
Si no hay productos, muestra un mensaje indicando que la lista está vacía.
📤 Datos de Salida
Se implementa un menú interactivo con las siguientes opciones:
1️⃣ Agregar un producto
2️⃣ Ver la lista de productos
3️⃣ (No implementado aún) Editar un producto
4️⃣ (No implementado aún) Eliminar un producto
5️⃣ Salir del programa
El programa se ejecuta en un bucle while hasta que el usuario elija la opción de salir (5).

Ejemplo de Uso

1. Agregar productos
Ingrese el nombre del producto: Leche
Ingrese la cantidad que llevará: 2
Ingrese su precio: 5000
¿Cuál es la presentación del producto?: Litros

2. Ver la lista de productos
Lista de Productos:
1. Leche - 2 unidades - $5000 - Litros
Este código es una base para seguir ampliándolo con más funcionalidades. ¡Sigue practicando! 🚀

Dijiste:
adicional explicame estas lineas
contador_id=1

#Procesos
def agregar_producto():
    global contador_id
ChatGPT dijo:
Vamos a desglosar estas líneas paso a paso para que lo entiendas con claridad.
 Explicación de contador_id = 1
Esta línea de código:
contador_id = 1
Declara una variable global llamada contador_id con un valor inicial de 1.
Se usa para asignar un ID único y consecutivo a cada producto cuando se agrega a la lista.
Como está fuera de cualquier función, su valor se mantiene en todo el programa.
💡 Ejemplo:
Si agregas un primer producto, tendrá id = 1; si agregas otro, tendrá id = 2, y así sucesivamente.

Explicación de global contador_id dentro de la función
python
Copiar
Editar
def agregar_producto():
    global contador_id
Aquí pasa algo importante:

1️⃣ global contador_id significa que dentro de la función agregar_producto() queremos usar y modificar la variable contador_id que se definió fuera de la función.
2️⃣ Si no ponemos global contador_id, Python creería que contador_id es una variable local dentro de la función y daría error si intentamos modificarla.


Ejemplo del problema sin global contador_id:
contador_id = 1  
def agregar_producto():
    contador_id += 1  # Intentamos modificar la variable global
    print(contador_id)

agregar_producto()  
Esto generará un error porque Python cree que contador_id es una variable nueva dentro de la función, no la que definimos fuera.

Solución correcta con global:
contador_id = 1  

def agregar_producto():
    global contador_id  # Indicamos que queremos modificar la variable global
    contador_id += 1
    print(contador_id)

agregar_producto()  # Ahora sí funciona sin errores
Resumen
contador_id = 1 → Declara la variable global y la inicia en 1.
global contador_id dentro de una función → Permite modificar la variable global dentro de la función sin generar errores.
Se usa para asignar IDs consecutivos a los productos en la lista.
Ejemplo práctico en el código
Si ejecutas el programa y agregas dos productos:

Ingrese el nombre del producto: Pan
Ingrese la cantidad que llevará: 1
Ingrese su precio: 2500
¿Cuál es la presentación del producto?: Bolsa

Ingrese el nombre del producto: Jugo
Ingrese la cantidad que llevará: 2
Ingrese su precio: 3000
¿Cuál es la presentación del producto?: Botella
La lista de productos quedará así:

Lista de Productos:
1. Pan - 1 unidad - $2500 - Bolsa
2. Jugo - 2 unidades - $3000 - Botella
Como ves, el contador_id aumenta con cada producto nuevo porque usamos global contador_id para actualizarlo.
