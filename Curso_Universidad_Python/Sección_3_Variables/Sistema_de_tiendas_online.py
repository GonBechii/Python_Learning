"""
Sistema de tienda Online

Crear el detalle de un producto de una tienda online

El detalle del producto debe tener:
   
   ° Nombre del producto.
   ° Precio del producto.
   ° Cantidad en el inventario.
   ° Indicar si está disponible.
   
Hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables.

"""


# Desarrollo proyecto
nombre_producto = "Cámara digital"
precio = 399.99
cantidad_inventario = 20
disponibilidad = True
print("*** SISTEMA DE TIENDA ONLINE ***",
      "\n", "Producto: ", nombre_producto,
      "\n", "Precio: ", precio,
      "\n", "Cantidad en el Inventario: ", cantidad_inventario,
      "\n", "Disponibilidad: ", disponibilidad)
print()

# cambios de variables
precio = 499.99
disponibilidad = False
print("*** SISTEMA DE TIENDA ONLINE ***",
      "\n", "Producto: ", nombre_producto,
      "\n", "Precio: ", precio,
      "\n", "Cantidad en el Inventario: ", cantidad_inventario,
      "\n", "Disponibilidad: ", disponibilidad)
