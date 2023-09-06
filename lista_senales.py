from nodo import nodo
import xml.etree.ElementTree as ET
class lista_senales:
    def __init__(self):
        self.primero=None
        self.contador_senales=0

    #insertar
    def insertar(self,senal):
        nodo_nuevo= nodo(objeto=senal)
        if self.primero is None:
            self.primero = nodo_nuevo
            self.contador_senales=0
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_nuevo
        self.contador_senales=0

    def recorrer_lista_iden(self):
        print("------------------lista de indentificadores------------")
        actual=self.primero
        while actual!= None:
            actual.objeto.lista_matriz_reducida.recorrer()
            actual = actual.siguiente

    def recorrer_matriz_reducida(self):
        print("--------------------Matriz reducida-------------------")
        actual = self.primero
        while actual!= None:
            actual.objeto.lista_matriz_reducida.recorrerm()
            actual = actual.siguiente

    def recorrer_e_imprimir_lista_patrones(self):
        print("Total de senales almacenadas:",self.contador_senales+1)
        actual=self.primero
        print('**************lista patrones*********************')
        while actual != None:
            print("Nombre:",actual.objeto.nombre,"Tiempo:",actual.objeto.tiempot,
                "Amplitud:",actual.objeto.amplitudt)
            actual.objeto.lista_patrones.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("")
        print("")
        print("")
    
    def crear_xml(self):
        senales_reducidas= ET.Element("senalesReducidas")
        actual = self.primero
        while actual!=None:
            senal = ET.SubElement(senales_reducidas,"senal")
            senal.set("nombre",str(actual.objeto.nombre))
            senal.set("A",str(actual.objeto.amplitudt))
            g = 1
            actual2= actual.objeto.lista_matriz_reducida.primero
            while actual2!=None:
                grupo = ET.SubElement(senal,"grupo")
                grupo.set("g",str(g))
                tiempos= ET.SubElement(grupo,"tiempos")
                tiempos.text = str(actual2.objeto.grupo)
                datos_grupo= ET.SubElement(grupo,"datosGrupo")
                for amplitud in range(int(actual.objeto.amplitudt)):
                    dato = ET.SubElement(datos_grupo,"dato")
                    dato.set("A",str(actual2.objeto.amplitud))
                    dato.text= str(actual2.objeto.dato)
                    actual2=actual2.siguiente
                g = g+1
            actual=actual.siguiente
            my_data=ET.tostring(senales_reducidas)
            my_data=str(my_data)
            self.xml_arreglado(senales_reducidas)

            arbol_xml=ET.ElementTree(senales_reducidas)
            arbol_xml.write("./Proyecto1_ipc2/Reportes/salida.xml",encoding="UTF-8",xml_declaration=True)

    def xml_arreglado(self, element, indent='  '):
        queue = [(0, element)]  
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children

    def mostar_senales(self):
        actual = self.primero
        n = 1
        print("--------------Senales Guardadas")
        while actual!= None:
            print(n,actual.objeto.nombre)
            n+=1
            actual = actual.siguiente
        senal_elegida=input("Escriba el nombre de la senal a graficar: ")
        self.buscar_y_crear(senal_elegida)

    def buscar_y_crear(self,senal_elegida):
        actual = self.primero
        while actual!= None:
            if actual.objeto.nombre==senal_elegida:
                break
            actual=actual.siguiente
        if actual == None:
            print("No se encontro la senal con el nombre:",senal_elegida)
            return
        actual.objeto.lista_datos.crear_g_datos(actual.objeto.nombre,actual.objeto.tiempot,actual.objeto.amplitudt)
        actual.objeto.lista_matriz_reducida.crear_g_reducida(actual.objeto.nombre,actual.objeto.amplitudt)

    def eliminar_datos(self):
        self.primero = None