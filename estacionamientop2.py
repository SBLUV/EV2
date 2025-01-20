estacionamientos = {
    "auto": 2000,
    "camioneta": 3000,
    "camion": 4000,
    "motocicleta": 890
}

fondo_cambio = 40000
dinero_ingresado = 0
descuentos_acumulados = 0

while True:
    print ("maquina de estacionamiento")
    print ("1.ver catalogo de precios")
    print ("2.ingresar correo")
    print ("3.ingresar dinero")
    print ("4.selccionar vehiculo")
    print ("cerrar operacion")
    opcion = input ("sleccione una opcion")

    if opcion == "1":
        print ("catalogo de precios:")
        for vehiculo, precio in estacionamientos.items():
            print (f"{vehjiculo}: ${precio}")

    elif opcion == "2":
        correo = input ("ingrese su correo:")
        if 8 <= len(correo) <= 30:

            antes_del_arroba = correo.split ('@') [0]
            descuento = 0
            for char in antes_del_arroba:
                if char in "A": descuento += 0.01
                elif char in "B": descuento += 0.03
                elif char in "C": descuento += 0.02
                elif char in "D": descuento += 0.07
                elif char in "E": descuento += 0.06

            print (f"descuento calculado: {descuento*100:2.f}%")
        else:
            print ("correo invalido, debe tener entre 8 y 30 caracteres")

    elif opcion == "3":
        try:
            monto = int (input("ingrese dinero (entre $1 y 10000):"))
            if 1 <= monto <= 10000:
                dinero_ingresado += monto
                print (f"dinero ingresado: ${dinero_ingresado}")
            else:
                print ("monto fuera de rango")
        except ValueError:
                print ("ingrese un monto valido")

    elif opcion == "4"
        print ("seleccione un vehiculo:")
        for idx, vehiculo in enumerate(estacionamientos.keys()):
            print (f"{idx+1}. {vehiculo}")
        try:
            seleccion = int (input("seleccione el numero correspondiente:"))
            vehiculos_lista = list (estacionamientos.keys())
            if 1 <= seleccion <= len(vehiculos_lista):
                vehiculo_elegido = vehiculos_lista[seleccion -1]
                precio = estacionamientos [vehiculo_elegido]


                total_a_pagar = precio * ( 1 -descuento) if descuento > 0 else precio

                if total_a_pagar <= dinero_ingresado:
                    dinero_ingresado -= total_a_pagar
                    fondo_cambio += total_a_pagar
                    descuentos_acumulados += descuento * precio
                    print (f"pago realizado: vehiculo: {vehiculo_elegido}, precio final: ${total_a_pagar:.0f}")
                else:
                    print ("dinero insuficiente")
            else:
                print ("seleccion invalida")
        except  (ValueError, IndexError):
            print ("seleccion invalida")

    elif opcion == "5":
        codigo_secreto = input ("ingrese el codigo secreto de administrador:")
        if codigo_secreto == "3312":
            print ("resumen de la operacion")
            print (f"dinero recaudado: ${fondo_cambio}")
            print (f"descuentos otorgados: ${descuentos_acumulados:.0f}")
            print (f"dinero restante del cliente: ${dinero_ingresado}")
            print ("gracias por usar la maquina, operacion finalizada")
            break
        else:
            print ("codigo incorrecto, operacion sin finalizar")
    else:
        print ("opcion no valida, intente denuevo")