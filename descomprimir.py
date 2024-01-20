# importamos las librerias necesarias
import shutil
import os

# ceamos la clase para descomprimir archivos, usamos el shutil
class DescomprimirArchivos():

    def __init__(self):# creamos el constructor
        
        self.formatos = ['ZIP', 'TAR', 'GZTAR', 'BZTAR', 'XZTAR']

    def descomprimir(self, archivo, carpeta, formato_elegido):# creamos el métoodo para descomprimir

        shutil.unpack_archive(archivo, carpeta, formato_elegido) # usamos el shutil 

        print('\nEl archivo ha sido descomprimido con éxito') # informamos al usuario

def formatos_compresion(formatos):

    while True: # creamos el bucle

        print('\n') # imprimimos un salto de linea

        for n, formato in enumerate(formatos, start= 1): # con este bucle imprimimos la lista en opciones

            print(f'{n} - {formato}')

        elegir = input('\nQue formato deseas descomprimir, Elige una opción: ') # almacenamos la eleccion

        # con el bucle verificamos la eleccion
        while not int(elegir.isnumeric()):

            print('\nTu elección no es valida, intenta de nuevo')

            elegir = input('\nQue formato deseas descomprimir, Elige una opción: ')
        

        elegir = int(elegir)# transformamos la eleccion en un entero

        if 1 <= elegir <= len(formatos): # verificamos la eleccion

            formato_elegido = formatos[elegir -1].lower() # almacenamos el formato elegido

            archivo_completo = f'{archivo}.{formato_elegido}' # almacenamos el nombre completo del archivo

            if not os.path.isfile(archivo_completo): # verificamos si el archivo existe

                print('\nLa extensión elegida no es válida en ese archivo, intenta de nuevo') # informamos al usuario
                
                continue

            return archivo_completo, formato_elegido # retornamos el nombre y el formato
                    
        else:

            print('La eleccion no es correcta, intenta de nuevo') # informamos al usuario
        
# creamos las variables
            
archivo = input('\nIngresa el nombre del archivo a descomprimir: ') #almacenamos el nombre del archivo que el usuario ingresa

carpeta = input('\nIngresa el nombre de la carpeta en la que deseas guardar tu archivo descomprimido: ').title() # creamos la carpeta para guardar los archivos descomprimidps

archivo_completo, formato_elegido = None, None # inicamos las variables en None

while formato_elegido is None: # con el bucle comprobamos las variables

    archivo_completo, formato_elegido = formatos_compresion(DescomprimirArchivos().formatos) # a cada variable le almacenamos un valor

DescomprimirArchivos().descomprimir(archivo_completo, carpeta, formato_elegido) # llamos a la funcion y su metodo para descomprimir el archivo
