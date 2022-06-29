import os
from colorama import Fore
from Analist.Lexico import *
from HTML.Reportes import HTML


class Menu():

    def __init__(self):
        self.elementos = ''
        self.cargar = 1
        self.nombre_html = 2
        self.salir = 0

    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(Fore.CYAN, f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.cargar }) - Cargar Archivo 
    \t{self.nombre_html}) - Nombre del Archivo
    \t{self.salir}) - Salir\n''')

    def menu(self) -> None:
        name_html = ''
        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")

            try:
                opcionMenu = int(opcionMenu)

                os.system('cls')

                if opcionMenu == self.cargar:
                    carga = input("Inserta la ruta del archivo .cs: >> \n")

                    try:
                        archivo = open(carga, encoding="utf8").read()
                        archivo = archivo.lower()
                        print(Fore.LIGHTYELLOW_EX,
                              'Archivo Cargado con Exito!!!')
                        
                        # Build the lexer and try it out
                        lex = Lexico()
                        lex.build()  # Build the lexer
                        lex.test(archivo)  # Test it Lexer
                        # Build the parser and try it out
                        lex.build_S()  # Build the parser
                        lex.test_S(archivo)  # Test it parser       
                        self.elementos = lex.dict_elementos
                        
                        
                    except OSError as exception:
                        print(f"\n Error: {exception}")

                elif opcionMenu == self.nombre_html:
                    if self.elementos:
                        name_html = input(
                            "Ingresa nombre del archivo .html: >> \n")
                        html = HTML()
                        if self.elementos['tokens'] != '':
                            html.createHTMLToken(
                                name_html, self.elementos['tokens'])
                        if self.elementos['errores'] != '':
                            html.createHTMLError(
                                name_html, self.elementos['errores'])

                    else:
                        print(Fore.LIGHTYELLOW_EX,
                              'Necesitas Cargar Archivo antes')

                elif opcionMenu == self.salir:
                    print("\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW, 'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                opcionMenu = -1
                print(Fore.RED, f'Error: {error}')
                print(Fore.RED, 'El programa no permite carateres tipo Caracter')
                input('Presione la tecla para continuar@')
