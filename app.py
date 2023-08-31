import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from senal import senal
from celda_datos import celda_datos
from lista_celdas import lista_celdas
from lista_senales import lista_senales
if __name__=="__main__":
    lista_senales_guardadas=lista_senales() 
    lista_identificadores = lista_celdas()
    def procesar_archivo(ruta):
        tree = ET.parse(ruta)
        raiz=tree.getroot()
        for senal_temp in raiz.findall('senal'):
            print('Guardando Datos')
            nombre_senal = senal_temp.get('nombre')
            tiempot = senal_temp.get('t')
            amplitudt = senal_temp.get('A')
            if int(amplitudt)>0 and int(amplitudt)<=130 and int(tiempot)>0 and int(tiempot)<=3600:
                lista_celdas_temporal = lista_celdas()
                lista_patrones = lista_celdas()
                for celda_senal in senal_temp.findall('dato'):
                    tiempo = int(celda_senal.get('t'))
                    amplitud = int(celda_senal.get('A'))
                    dato = int(celda_senal.text)
                    if tiempo>=0 and amplitud>=0 and tiempo<=int(tiempot) and amplitud<=int(amplitudt):
                        nueva_celda = celda_datos(tiempo,amplitud,dato)
                        lista_celdas_temporal.insertar_ordenado(nueva_celda)
                print('Generando lista de Patrones')
                lista_celdas_temporal.crear_celdas_faltantes(int(tiempot),int(amplitudt))
                lista_patrones.crear_generar_patrones(int(tiempot),int(amplitudt),lista_celdas_temporal)
                lista_matriz_reducida=lista_celdas()
                lista_matriz_reducida.generar_matriz_reducida(lista_patrones,lista_celdas_temporal,int(amplitudt))
                lista_senales_guardadas.insertar(senal(nombre_senal,tiempot,amplitudt,lista_celdas_temporal,lista_patrones,lista_matriz_reducida))
        lista_senales_guardadas.recorrer_e_imprimir_lista()
        lista_senales_guardadas.recorrer_matriz_reducida()

    def iniciar_menu():
        ruta=''
        a = True
        while a:
            print("Menu Principal")
            print('   1. Cargar Archivo')
            print('   2. Procesar Arvhivo')
            print('   3. Escrbir Archivo Salida')
            print('   4. Mostrar Datos del Estudiante')
            print('   5. Generar Grafica')
            print('   6. Inicializar Sistema')
            print('   7. Salida')
            opcion = input('Eliga una opcion: ')
            if opcion == '1':
                ruta =askopenfilename()
                archivo= open(ruta,"r")
                archivo.close()
            elif opcion == '2':
                procesar_archivo(ruta)
            elif opcion == '3':
                print('opcion3')
                print('')
            elif opcion == '4':
                print('Juan Pascual Itzep Coguox')
                print('202202161')
                print('Introduccion a la Programacion y Coomputacion 2 seccion "D"')
                print('Ingenieria en Ciencias y Sistemas')
                print('4to Semestre')
                print('')
            elif opcion == '5':
                print('opcion5')
                print('')
            elif opcion == '6':
                print('opcion6')
                print('')
            elif opcion == '7':
                a = False
                print('-----------Saliendo------------')
                print('')
            else:
                print('ESTA OPCION NO EXISTE')
                print('')
    iniciar_menu()