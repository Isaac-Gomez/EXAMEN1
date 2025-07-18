productos={
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
   'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca(marca):
    for modelo, datos in productos.items():
        if datos[0].lower()== marca.lower():
            total+=stock.get(modelo,[0,0])[1]
    print(f"el stock es:{total}")

def buscar_por_precio(p_min,p_max):
    try:
        p_min=int(p_min)
        p_max=int(p_max)
    except ValueError:
        print("los precios deben ser numeros enteros")
        return
    disponibles=[]
    for modelo, datos in stock.items():
        precio,cantidad=datos
        if p_min <= precio <= p_max and cantidad > 0:
            marca=productos[modelo][0]
            disponibles.append(f"{marca}--{modelo}")
    
    if disponibles:
        print("productos disponibles:", sorted(disponibles))
    else:
        print("no hay productos disponibles en ese rango de precios")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0]= nuevo_precio
        return True
    else:
        return False
    
def menu():
    while True:
        print("\***MENU PRINCIPAL***")
        print("1. stock por marca")
        print("2. buscar por precio")
        print("3. actualizar precio")
        print("4. salir")
        opcion=input("ingrese una opcion:").strip()

        if opcion == "1":
            marca=input("ingrese marca a consultar:").strip()
            stock_marca(marca)
        elif opcion =="2":
            p_min=input("ingrese precio minimo:").strip()
            p_max=input("ingrese precio maximo:").strip()
            buscar_por_precio(p_min, p_max)
        elif opcion == "3":
            while True:
                modelo=input("ingrese modelo a actualizar:").strip().upper()
                try:
                    nuevo_precio=int(input("ingrese nuevo precio:").strip())
                except ValueError:
                    print("el precio debe ser un numero entero")
                    continue
                if actualizar_precio(modelo, nuevo_precio):
                    print("precio actualizado correctamente")
                else:
                    print("modelo no encontrado")
                seguir=input("desea actualizar otro modelo? (s/n):").strip().lower()
                if seguir != "s":
                    break
        elif opcion == "4":
            print("programa finalizado. gracias por usarlo")
            break
        else:
            print("debe seleccionar una opcion valida. intente nuevamente")

if __name__=="__main__":
    print("BIENVENIDO AL SISTEMA DE GESTION DE STOCK")
    menu()