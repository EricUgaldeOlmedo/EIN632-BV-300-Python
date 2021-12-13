def menuScrapper():
    """
        Descripción: Menu inicial del programa, cada opción esta mapeada para trabajar con otra
        Parametros: Ninguno
    """    
    print("Scrapper UTFSM: Certamen 2 - Eric Ugalde Olmedo - 06Dec2021")
    print("Menu inicial")
    print("Seleccione entre las siguientes opciones:")
    print("1.- Página Aleatoria")
    print("2.- Página predeterminada a escojer")
    print("3.- Salir")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Se ha seleccionado un caracter invalido")
        menuScrapper()
    if opcion == 1:
        menuPaginaAletoria()
    elif opcion == 2:
        menuPaginaPredeterminada()
    elif opcion == 3:
        print("Se ha seleccionado salir, se cerrará la consola")
    else:
        print("Se ha seleccionado una opción no valida")
        menuScrapper()        

def menuPaginaAletoria():
    """
        Descripción: Menu que se invoca al seleccion la opción de página aleatoria, se requiere ingregar todos los parametros necesarios para trabajar el WebScrapper
        Parametros: Ninguno
    """    
    print("Seleccione entre las siguientes opciones:")
    print("1.- Ingresar URL y moneda")
    print("2.- Volver")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Se ha seleccionado un caracter invalido")
        menuPaginaPredeterminada()
    if opcion == 1:
        pagina = input("Esbriba la página a buscar: ")
        moneda = input("Esbriba la moneda a buscar (Formato Regex): ")
        import Scrapper
        Scrapper.scrapperWebPage(pagina, moneda)
    elif opcion == 2:
        print("Se ha seleccionado volver, se regresará al menú principal")
        menuScrapper()
    else:
        print("Se ha seleccionado una opción no valida")
        menuPaginaAletoria()
    

def menuPaginaPredeterminada():
    """
        Descripción: Menu que tiene distintas web mapeadas para trabajar el WebScrapper, cada opción luego utiliza el menú de seleccion de CriptoMonedas
        Parametros: Ninguno
    """    
    print("Seleccione entre las siguientes opciones:")
    print("1.- CoinTelegraph")
    print("2.- CriptoNoticias")
    print("3.- CoinGecko")
    print("4.- Volver")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Se ha seleccionado un caracter invalido")
        menuPaginaPredeterminada()
    if opcion == 1:
        menuIngresoCriptoMoneda("https://es.cointelegraph.com/rss/tag/altcoin")
    elif opcion == 2:
        menuIngresoCriptoMoneda("https://www.criptonoticias.com/feed/")
    elif opcion == 3:
        menuIngresoCriptoMoneda("https://www.coingecko.com/es/news")
    elif opcion == 4:
        print("Se ha seleccionado volver, se regresará al menú principal")
        menuScrapper()
    else:
        print("Se ha seleccionado una opción no valida")
        menuPaginaPredeterminada()

def menuIngresoCriptoMoneda(paginaOrigen):
    """
        Descripción: Menu mapeado con distintas REGEX para cada moneda que se utilizará en búsqueda y filtrado de noticias
        Parametros: paginaOrigen / String
    """    
    import Scrapper as sc
    print("Seleccione entre las siguientes opciones:")
    print("1.- BitCoin")
    print("2.- Ethereum")
    print("3.- Shiba Inu")
    print("4.- Ingreso por usuario (Formato Regex)")
    print("5.- Volver")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Se ha seleccionado un caracter invalido")
        menuIngresoCriptoMoneda(paginaOrigen)
    if opcion == 1:
        sc.scrapperWebPage(paginaOrigen, "(?i)(bitcoin|btc)")
    elif opcion == 2:
        sc.scrapperWebPage(paginaOrigen, "(?i)(Ethereum|ETH)")
    elif opcion == 3:
        sc.scrapperWebPage(paginaOrigen, "(?i)(SHIB|INU)")
    elif opcion == 4:
        moneda = str(input("Moneda (Formato Regex): "))
        sc.scrapperWebPage(paginaOrigen, moneda)
    elif opcion == 5:
        print("Se ha seleccionado volver, se regresará al menú de selección de página")
        menuPaginaPredeterminada()
    else:
        print("Se ha seleccionado una opción no valida")
        menuIngresoCriptoMoneda(paginaOrigen)

if __name__ == "__main__":
    menuScrapper()
