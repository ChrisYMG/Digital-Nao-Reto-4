saldo = 10.00  # Saldo inicial

def menu_principal():
    print("\nBienvenido al Menú USSD")
    print("1. Saldo")
    print("2. Recargar")
    print("3. Paquetes")
    print("0. Salir")

def submenu_paquetes():
    print("\nPaquetes Disponibles")
    print("1. Internet")
    print("2. Voz")
    print("3. SMS")
    print("0. Regresar al menú principal")

def consultar_saldo():
    global saldo
    print(f"\nSu saldo actual es de ${saldo:.2f}")

def recargar_saldo():
    global saldo
    codigo = input("\nIngrese el código de recarga: ")
    # Supongamos que cada código añade $5 al saldo
    if codigo.isnumeric():  # Simulación básica de validación
        saldo += 5.00
        print("Recarga exitosa.")
        print(f"Su nuevo saldo es de ${saldo:.2f}")
    else:
        print("Código de recarga inválido.")

def main():
    global saldo
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            recargar_saldo()
        elif opcion == "3":
            while True:
                submenu_paquetes()
                opcion_paquetes = input("Seleccione un paquete: ")
                
                if opcion_paquetes == "1":
                    print("\nPaquetes de Internet...")
                elif opcion_paquetes == "2":
                    print("\nPaquetes de Voz...")
                elif opcion_paquetes == "3":
                    print("\nPaquetes de SMS...")
                elif opcion_paquetes == "0":
                    break
                else:
                    print("\nOpción inválida, intente de nuevo.")
        elif opcion == "0":
            print("\nGracias por usar nuestro servicio USSD.")
            break
        else:
            print("\nOpción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()