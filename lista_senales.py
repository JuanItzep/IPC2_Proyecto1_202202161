from nodo import nodo

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
    def recorrer_e_imprimir_lista(self):
        print("Total de senales almacenadas:",self.contador_senales+1)
        print("")
        print("")
        print("")
        print("******************************************************************")
        actual=self.primero
        while actual != None:
            print("Nombre:",actual.objeto.nombre,"Tiempo:",actual.objeto.tiempot,
                "Amplitud:",actual.objeto.amplitudt)
            actual.objeto.lista_datos.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            print("")
            print("")
            print("")
        print("******************************************************************")
        print("******************************************************************")
        actual=self.primero
        print('lista patrones')
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