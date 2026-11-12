import Menu
import Gestion_stock
def main():
    Gestion_stock.inicializar()
    opcion=Menu.mostrar_menu()
    if opcion==1:
        Gestion_stock.cargar_stock()
    elif opcion==2:
        Gestion_stock.mostrar_stock()
    elif opcion==3:
        categ=input("categoria a contar: ")
        Gestion_stock.contar(categ)
if __name__ == "__main__":
    main()