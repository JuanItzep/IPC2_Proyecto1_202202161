from celda_datos import celda_datos
from nodo import nodo

class lista_celdas:
    def __init__(self):
        self.primero=None
    def insertar(self,celda):
        nodo_nuevo= nodo(objeto=celda)
        if self.primero is None:
            self.primero = nodo_nuevo
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_nuevo

    def insertar_ordenado(self, celda):
        nodo_nuevo = nodo(objeto=celda)
        if self.primero is None:
            self.primero = nodo_nuevo
            return
        if celda.tiempo < self.primero.objeto.tiempo or (
                celda.tiempo == self.primero.objeto.tiempo and celda.amplitud <= self.primero.objeto.amplitud):
            nodo_nuevo.siguiente = self.primero
            self.primero = nodo_nuevo
            return
        actual = self.primero
        while actual.siguiente is not None and (
                celda.tiempo > actual.siguiente.objeto.tiempo or (
                        celda.tiempo == actual.siguiente.objeto.tiempo and celda.amplitud > actual.siguiente.objeto.amplitud)):
            actual = actual.siguiente
        nodo_nuevo.siguiente = actual.siguiente
        actual.siguiente = nodo_nuevo

    def crear_celdas_faltantes(self,tiempot, amplitudt):
        actual1= self.primero
        a=1
        b=1
        c= False
        if actual1.objeto.tiempo==a and actual1.objeto.amplitud==b:
            b=b+1
        else:
            nodo_nuevo= nodo(objeto =celda_datos(a,b,0))
            nodo_nuevo.siguiente=actual1
            self.primero=nodo_nuevo
            b=b+1
        actual1= self.primero
        while actual1.siguiente and c==False:
            while a!=tiempot+1:
                while b!=amplitudt+1:
                    if actual1.siguiente:
                        print(a,actual1.siguiente.objeto.tiempo,b,actual1.siguiente.objeto.amplitud)
                        if actual1.siguiente.objeto.tiempo==a and actual1.siguiente.objeto.amplitud==b:
                            actual1= actual1.siguiente
                        else:
                            c = True
                            break
                        b=b+1
                    else:
                        c = True
                        break
                if c:
                    break
                a=a+1
                b = 1
            if c:
                nodo_nuevo= nodo(celda_datos(a,b,0))
                nodo_nuevo.siguiente=actual1.siguiente
                actual1.siguiente = nodo_nuevo
                c= False

    def crear_generar_patrones(self,tiempot,amplitudt,lista_celdas_temporal):
        nodo_lista = lista_celdas_temporal.primero
        for tiempo in range(tiempot):
            for amplitud in range(amplitudt):
                    if nodo_lista.objeto.dato!= 0:
                        self.insertar(celda_datos(tiempo+1, amplitud+1, 1))
                        nodo_lista = nodo_lista.siguiente
                    else:
                        self.insertar(celda_datos(tiempo+1, amplitud+1, 0))
                        nodo_lista = nodo_lista.siguiente

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual=self.primero
        while actual !=None:
            print("tiempo:",actual.objeto.tiempo,"Amplitud:",actual.objeto.amplitud,
                "dato:",actual.objeto.dato)
            actual=actual.siguiente
        print("============================================================")