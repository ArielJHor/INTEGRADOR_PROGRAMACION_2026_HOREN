stock_productos={'enlatados':["Atun", "Salsa de tomate"],'frutas':["Manzana", "Pera"],'congelados':["Carne", "Pollo"],'panaderia':["Pan", "Tortas"]}
stock_cantidades={'enlatados':[5, 10],'frutas':[2, 8],'congelados':[8, 5],'panaderia':[10, 2]}
def inicializar():
    for categoria in stock_productos:
        stock_productos=[]
    for categoria in stock_cantidades:
        stock_cantidades=[]
def cargar_stock():
    categ=input("categoria: ")
    prod=input("producto: ")
    cant=input("cantidad: ")
    stock_productos[categ].append(prod)
    stock_cantidades[categ].append(cant)
def mostrar_stock():
    for categ in stock_productos:
        print(categ)
        print(stock_productos[categ])
        print(stock_cantidades[categ])
def contar(lista_productos):
    print("cantidad:",len(lista_productos))