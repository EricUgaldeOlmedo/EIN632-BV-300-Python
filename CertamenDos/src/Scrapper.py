import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def scrapperWebPage(url, coin):
    """
        Descripción: Función para redirigir a las distintas funciones especificas a usar por URL
        Parametros: url /String y coin / String
    """    
    # Soup es un objeto con multiples atributos, sin ninguno, el print muestra una página HTML5.
    # Find_All permite adquirir todos los tags de cierto tipo del HTML para guardarlos como array, también se puede agregar filtro por Class o ID
    # 1º Problema de un WebScrapper es que se la estructura de una página puede cambiar o hay que hacerlo especifico para cada una
    # 2º Problema es que hay páginas que por proteccion de contenido no permiten la revisión de lo que hay en ellos Ej: https://cointext.com/es/noticias/feed/ arroja error 403
    # 3º Problema corresponde a que muchas páginas e incluso XML tienen estructuras como CData por lo que ciertos parsers tienen problemas con como trabajar esas estructuras
    if url == "https://es.cointelegraph.com/rss/tag/altcoin":
        scrapperCoinTelegraph(coin)
    elif url == "https://www.criptonoticias.com/feed/":
        scrapperCriptoNoticias(coin)
    elif url == "https://www.coingecko.com/es/news":
        scrapperCoinGecko(coin)
    else:
        scrapperWebPage(url, coin)

def scrapperCoinTelegraph(coin):
    """
        Descripción: Función de WebScrapping sobre la web cointelegraph.com/rss/tag/altcoin (RSS)
        Parametros: coin / String
    """
    import html5lib
    pagina = requests.get("https://es.cointelegraph.com/rss/tag/altcoin")
    soup = BeautifulSoup(pagina.content, "html5lib", from_encoding = "utf-8")
    articulos = soup.find_all("item")
    noticiasFiltradas = pd.DataFrame()
    for articulo in articulos:
        if re.search(coin, articulo.get_text()) is not None and len(noticiasFiltradas.index) < 3:
            datosArticulo = {"titulo" : articulo.find("title").text, "descripcion": articulo.find("description").text, "fecha": articulo.find("pubdate").text, "categoria": " ".join(str(categoria) for categoria in articulo.find_all("category"))}
            noticiasFiltradas = noticiasFiltradas.append(datosArticulo, ignore_index = True)
    if len(noticiasFiltradas.index) < 1:
        print("No se encontraron noticias asociadas a este tipo de Criptomoneda")
    else:
        scrapperLimpiarCampos(noticiasFiltradas)
        scrapperGeneraCSV(noticiasFiltradas)

def scrapperCoinGecko(coin):
    """
        Descripción: Función de WebScrapping sobre la web coingecko.com/es/news (HTML)
        Parametros: coin / String
    """
    import html5lib
    pagina = requests.get("https://www.coingecko.com/es/news")
    soup = BeautifulSoup(pagina.content, "html5lib", from_encoding = "utf-8")
    articulos = soup.find_all("article")
    noticiasFiltradas = pd.DataFrame()
    for articulo in articulos:
        if re.search(coin, articulo.get_text()) is not None and len(noticiasFiltradas.index) < 3:
            datosArticulo = {"titulo" : articulo.find("div", {"class": "tw-text-xl"}).text, "descripcion": articulo.find("div", {"class": "post-body"}).text, "fecha": articulo.find_all("span")[1].get_text()}
            noticiasFiltradas = noticiasFiltradas.append(datosArticulo, ignore_index = True)
    if len(noticiasFiltradas.index) < 1:
        print("No se encontraron noticias asociadas a este tipo de Criptomoneda")
    else:
        scrapperLimpiarCampos(noticiasFiltradas)
        scrapperGeneraCSV(noticiasFiltradas)
    
def scrapperCriptoNoticias(coin):
    """
        Descripción: Función de WebScrapping sobre la web criptonoticias.com/feed (RSS)
        Parametros: coin / String
    """
    import html5lib
    pagina = requests.get("https://www.criptonoticias.com/feed/")
    soup = BeautifulSoup(pagina.content, "html5lib", from_encoding = "utf-8")
    articulos = soup.find_all("item")
    noticiasFiltradas = pd.DataFrame()
    for articulo in articulos:
        if re.search(coin, articulo.get_text()) is not None and len(noticiasFiltradas.index) < 3:            
            datosArticulo = {"titulo" : articulo.find("title").text, "descripcion": articulo.find("description").text, "fecha": articulo.find("pubdate").text, "categoria": " ".join(str(categoria) for categoria in articulo.find_all("category"))}
            noticiasFiltradas = noticiasFiltradas.append(datosArticulo, ignore_index = True)
    if len(noticiasFiltradas.index) < 1:
        print("No se encontraron noticias asociadas a este tipo de Criptomoneda")
    else:
        scrapperLimpiarCampos(noticiasFiltradas)
        scrapperGeneraCSV(noticiasFiltradas)

def scrapperRandomWebPage(url, coin):
    """
        Descripción: Función (No testeada) para realizar un WebScrapping de una Web permitiendo trabajar cada uno de los parametros como ingreso de datos
        Parametros: url / String y coin / String
    """
    pagina = requests.get(url)
    print("Seleccione entre las siguientes opciones para parsear la página:")
    print("1.- HTML5Lib")
    print("2.- LXML (Se pierde el contenido de bloques CDATA)")
    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Se ha seleccionado un caracter invalido")
        scrapperRandomWebPage(url, coin)
    if opcion == 1:
        import html5lib
        soup = BeautifulSoup(pagina.content, "html5lib", from_encoding = "utf-8")
    elif opcion == 2:
        import lxml
        soup = BeautifulSoup(pagina.content, "lxml", from_encoding = "utf-8")
    else:
        print("Se ha seleccionado una opción no valida")
        scrapperRandomWebPage(url, coin)
    noticiasFiltradas = pd.DataFrame()
    formatoArticulo = input("Esbriba el tipo de objeto donde se contienen los articulos: ")
    articulos = soup.find_all(formatoArticulo)
    formatoTitulo = input("Esbriba el tipo de objeto donde se contiene el titulo: ")
    formatoResumen = input("Esbriba el tipo de objeto donde se contiene el resumen: ")
    formatoFecha = input("Esbriba el tipo de objeto donde se contiene la fecha: ")
    for articulo in articulos:
        if re.search(coin, articulo.get_text()) is not None and len(noticiasFiltradas.index) < 3:            
            datosArticulo = {"titulo" : articulo.find(formatoTitulo).text, "descripcion": articulo.find(formatoResumen).text, "fecha": articulo.find(formatoFecha).text}
            noticiasFiltradas = noticiasFiltradas.append(datosArticulo, ignore_index = True)
    if len(noticiasFiltradas.index) < 1:
        print("No se encontraron noticias asociadas a este tipo de Criptomoneda")
    else :
        scrapperLimpiarCampos(noticiasFiltradas)
        scrapperGeneraCSV(noticiasFiltradas)

def scrapperLimpiarCampos(noticias):
    """
        Descripción: Función para realizar limpieza campo a campo de un DataFrame, con tal de remover caracteres invalidos
        Parametros: noticias / DataFrame
    """
    # Debido a que en este punto ya se esta trabajando con dataframes y cada campo es una serie
    # para limpiar los campos se debe hacer con funciones lambda (Aplicación de función en 1 linea y ejecución con .map del DataFrame)
    # ademas, por la forma de trabajar de Python se pueden realizar multiples strip dependiendo de que se ha visualizado en los parseos
    noticias["titulo"] = noticias["titulo"].map(lambda campo: campo.replace("<!--[CDATA[", "").replace("<![CDATA[", "").replace("]]-->", "").replace("]]>", "").replace('Leer más"', "").replace("\n", "").strip())
    print(noticias["descripcion"])
    noticias["descripcion"] = noticias["descripcion"].map(lambda campo: campo.replace("<!--[CDATA[", "").replace("<![CDATA[", "").replace("]]-->", "").replace("]]>", "").replace('Leer más"', "").replace("\n", "").strip())
    print(noticias["descripcion"])
    noticias["fecha"] = noticias["fecha"].map(lambda campo: campo.replace("<!--[CDATA[", "").replace("<![CDATA[", "").replace("]]-->", "").replace("]]>", "").replace('Leer más"', "").replace("\n", "").strip())
    # Revisión de la exitencia de columna categoria en el dataframe
    if "categoria" in noticias.columns:
        noticias["categoria"] = noticias["categoria"].map(lambda campo: campo.replace("<!--[CDATA[", "").replace("<![CDATA[", "").replace("]]-->", "").replace("]]>", "").replace('Leer más"', "").replace("\n", "").replace("<category>", "").replace("</category>", "").strip())
    
def scrapperGeneraCSV(noticias):
    """
        Descripción: Función para exportar un dataframe a CSV
        Parametros: noticias / DataFrame
    """
    import os
    from datetime import datetime
    directorio = os.path.dirname(__file__)
    nombreArchivo = directorio + "/Noticias" + datetime.now().strftime("%d%m%Y-%H%M") + ".csv"
    noticias.to_csv(nombreArchivo, index = False, encoding = "utf-8", sep = "|")
    print("Se ha generado el archivo", nombreArchivo)