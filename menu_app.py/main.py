def agregar_compra(compras):
    cantidad_compra = int(input("Ingrese el monto de la compra: "))
    compras.append(cantidad_compra)
    print("Compra agregada correctamente.")

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for compra, cantidad in enumerate(compras,1):
            print(f"Compra N° {compra}: ${cantidad:.2f}")

def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("Menú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = int(input("Seleccione una opción:"))

        if opcion == 1:
            agregar_compra(compras)
        if opcion == 2:
            mostrar_compras(compras)
        if opcion == 3:
            mostrar_total(compras)
        if opcion == 4:
            print("¡Hasta Luego!")
            exit()

if __name__ == "__main__":
    main()