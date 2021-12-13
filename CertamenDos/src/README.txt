Certamen 2 - EIN632-BV-300 2021-02 UTFSM - Eric Ugalde Olmedo

Requerimientos básicos:
1.- Tener instalado Python 3 (Versión actual 3.10.1 https://www.python.org/downloads/)
2.- Agregar Python al PATH de Windows durante la instalación o realizarlo de forma manual
3.- Abrir una linea de comandos para ejecutar a través de ella la instalación de paquetes de librerias de python
    3.1.- Ejecutar las siguientes lineas de comandos:
        3.1.1.- python -m pip install requests
        3.1.2.- python -m pip install html5lib
        3.1.3.- python -m pip install beautifulsoup4
        3.1.4.- python -m pip install lxml
    3.2.- Estas librerias son utilizadas con los siguientes usos:
        3.2.1.- Requests será usada para que cuando se ingrese una URL, su contenido sea trabajado como un objeto en Python
        3.2.2.- HTML5Lib transformará el objeto a un formato HTML5 válido, de forma de poder leer el contenido previamente adquirido
        3.2.3.- LXML es otra libreria que servirá para parsear el contenido de una página, en este caso, desde un XML (Formato usado en RSS Feed)
        3.2.4.- BeautifulSoup permite extraer datos desde un objeto HTML pero para ello debe transformarlo a uno válido, por tanto, se usa en conjunto con HTML5Lib

Modo de uso:
1.- Todos los archivos deben encontrarse en la misma carpeta (Menu.py, README.txt y Scrapper.py)
2.- Ejecutar Menu.py
    2.1.- Acá aparecerá la ventana del menú principal, esta indica los paso a paso a seguir.
        2.1.1.- Menu Página Aleatoria: Solicita el ingreso de una URL y una expresión REGEX para la búsqueda en el contenido de la web
                posteriormente solicita seleccionar un Parser y dar la estructura básica de contenido para poder trabajar
        2.1.2.- Menu Pagina Predeterminada: Cada una de las opciones trabaja con una URL especifica o volver al menú principal
            2.1.2.1.- Menu Moneda: Cada opcion corresponde a una REGEX predefinida, en caso de seleccionar el ingreso de una por el usuario, debe ser en formato REGEX.
                      También existe la opción de volver al menú de selección de página
        2.1.3.- La opción de salir simplemente cierra la consola de trabajo.
3.- Si se realizó el trabajo completo de alguna de las opciones distinto a salir
    3.1.- En caso que no existiesen noticias se entrega un mensaje informativo y se cierra la consola 
    3.2.- Se generá un archivo CSV con máximo 3 noticias provinientes de la URL y Criptomoneda buscada, el nombre de estos es: NoticiasDDmmYYYY-HHMM.csv

