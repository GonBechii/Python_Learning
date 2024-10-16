# Ejercicio de sistema de reserva de hoteles interactivo
print("*** SISTEMA DE RESERVA DE HOTELES ***")
nombre_cliente = input("Inserte su nombre: ")
dias_estancia = int(input("Inserte el numero de días de estancia: "))
print("La tarifa es de $1500.00 por dia")
tarifa_diaria = 1500.00

habitacion_vista_mar = input("¿Desea una habitación con vista al mar? (s/n): ")
if habitacion_vista_mar == "s":
    habitacion_vista_mar = True
else:
    habitacion_vista_mar = False


print("\n", "*** SISTEMA DE RESERVA DE HOTELES ***",
      "\n",
      "Cliente: ", nombre_cliente,
      "\n",
      "Días de estancia: ", dias_estancia,
      "\n",
      "Tarifa por dia: ", (tarifa_diaria * dias_estancia),
      "\n",
      "Habitacion con vista al mar: ", habitacion_vista_mar)
