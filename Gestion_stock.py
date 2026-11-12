stock_productos={'enlatados':[],'frutas':[],'congelados':[],'panaderia':[]}
stock_cantidades={'enlatados':[],'frutas':[],'congelados':[],'panaderia':[]}
def inicializar():
    for categ in stock_productos:
        stock_productos=[]
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