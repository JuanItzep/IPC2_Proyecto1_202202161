from celda_datos import celda_datos
from identificador_patron import identificador_patron
from nodo import nodo
from celda_matriz_reducida import celda_matriz_reducida
import os

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
                        self.insertar(celda_datos(tiempo+1, amplitud+1, '1'))
                        nodo_lista = nodo_lista.siguiente
                    else:
                        self.insertar(celda_datos(tiempo+1, amplitud+1, '0'))
                        nodo_lista = nodo_lista.siguiente

    def generar_matriz_reducida(self,lista_patrones,lista_celdas_temporal,amplitudt):
        actual = lista_patrones.primero
        lista_identificadores=lista_celdas()
        cadena_patron=''
        while actual:
            if actual.siguiente:
                if actual.objeto.tiempo==actual.siguiente.objeto.tiempo:
                    cadena_patron=cadena_patron+actual.objeto.dato
                    actual = actual.siguiente
                else:
                    cadena_patron=cadena_patron+actual.objeto.dato
                    lista_identificadores.insertar(identificador_patron(actual.objeto.tiempo,cadena_patron))
                    cadena_patron=''
                    actual = actual.siguiente
            else:
                cadena_patron= cadena_patron+actual.objeto.dato
                lista_identificadores.insertar(identificador_patron(actual.objeto.tiempo,cadena_patron))
                actual = actual.siguiente
        actual2= lista_identificadores.primero
        while actual2!= None:
            actual3=lista_identificadores.primero.siguiente
            c=0
            a = True
            while actual3!=None:
                if actual2.objeto.cadena_patron==actual3.objeto.cadena_patron:
                    if c== 0:
                        a = False
                        c=1
                        for amplitud in range(amplitudt):
                            dato1=lista_celdas_temporal.obtener(actual2.objeto.fila_tiempo,amplitud+1)
                            dato2=lista_celdas_temporal.obtener(actual3.objeto.fila_tiempo,amplitud+1)
                            dato = dato1+dato2
                            nombre_filas_concatenadas=str(actual2.objeto.fila_tiempo)+","+str(actual3.objeto.fila_tiempo)
                            self.insertar(celda_matriz_reducida(nombre_filas_concatenadas,dato,actual2.objeto.cadena_patron,amplitud+1,2,actual2.objeto.fila_tiempo))
                            lista_identificadores.eliminar(actual3.objeto.fila_tiempo,actual3.objeto.cadena_patron)
                    else:
                        for amplitud in range(amplitudt):
                            dato_a_sumar = lista_celdas_temporal.obtener(actual3.objeto.fila_tiempo,amplitud+1)
                            nombre_fila_concatenar = str(actual3.objeto.fila_tiempo)
                            self.sumar(dato_a_sumar,nombre_fila_concatenar,actual3.objeto.cadena_patron,amplitud+1)
                            lista_identificadores.eliminar(actual3.objeto.fila_tiempo,actual3.objeto.cadena_patron)
                actual3= actual3.siguiente
            if a:
                for amplitud in range(amplitudt):
                    dato1=lista_celdas_temporal.obtener(actual2.objeto.fila_tiempo,amplitud+1)
                    self.insertar(celda_matriz_reducida(actual2.objeto.fila_tiempo,dato1,actual2.objeto.cadena_patron,amplitud+1,1,actual2.objeto.fila_tiempo))
            lista_identificadores.eliminar(actual2.objeto.fila_tiempo,actual2.objeto.cadena_patron)
            actual2= lista_identificadores.primero
        self.ordenar_matriz_reducida(amplitudt)

    def ordenar_matriz_reducida(self,amplitudt):
        actual = self.primero
        lista_minilistas= lista_celdas()
        while actual!= None:
            minilista=lista_celdas()
            for amplitud in range(amplitudt):
                minilista.insertar(actual.objeto)
                actual = actual.siguiente
            lista_minilistas.insertar_ordenado2(minilista)
        nueva_lista_matriz_ordenada = lista_celdas()
        actual1 = lista_minilistas.primero
        while actual1!= None:
            actual2= actual1.objeto.primero
            while actual2!= None:
                nueva_lista_matriz_ordenada.insertar(actual2.objeto)
                actual2= actual2.siguiente
            actual1 = actual1.siguiente
        self.primero= nueva_lista_matriz_ordenada.primero 
        
    def insertar_ordenado2(self,minilista):
        nodo_nuevo = nodo(objeto =minilista)
        if self.primero is None:
            self.primero = nodo_nuevo
            return
        if minilista.primero.objeto.num_filas>self.primero.objeto.primero.objeto.num_filas:
            nodo_nuevo.siguiente = self.primero
            self.primero = nodo_nuevo
            return
        actual = self.primero
        while actual.siguiente!=None and (actual.siguiente.objeto.primero.objeto.num_filas>=minilista.primero.objeto.num_filas and 
                                actual.siguiente.objeto.primero.objeto.tiempo_smaller<minilista.primero.objeto.tiempo_smaller):
                actual = actual.siguiente
        nodo_nuevo.siguiente= actual.siguiente
        actual.siguiente = nodo_nuevo



    def eliminar2(self,objeto):
        actual = self.primero
        if actual.objeto == objeto:
            print("entraif")
            self.primero = actual.siguiente
        while actual!=None:
            if actual.siguiente:
                if actual.siguiente.objeto == objeto:
                    aux = actual.siguiente
                    actual.siguiente = aux.siguiente
            actual = actual.siguiente

    def eliminar(self,fila_tiempo,cadena_patron):
        actual = self.primero
        if actual.objeto.fila_tiempo == fila_tiempo and actual.objeto.cadena_patron==cadena_patron:
            self.primero = actual.siguiente
        while actual!=None:
            if actual.siguiente:
                if actual.siguiente.objeto.fila_tiempo == fila_tiempo and actual.siguiente.objeto.cadena_patron==cadena_patron:
                    aux = actual.siguiente
                    actual.siguiente = aux.siguiente
            actual = actual.siguiente

    def sumar(self,dato_a_sumar,nombmre_fila_concatenar,cadena_patron,amplitud):
        actual = self.primero
        while actual!= None:
            if actual.objeto.cadena_patron==cadena_patron and actual.objeto.amplitud==amplitud:
                actual.objeto.dato= actual.objeto.dato+dato_a_sumar
                actual.objeto.grupo=actual.objeto.grupo+","+nombmre_fila_concatenar
                actual.objeto.num_filas= actual.objeto.num_filas+1
            actual = actual.siguiente

    def obtener(self,tiempo,amplitud):
        actual = self.primero
        while actual!=None:
            if actual.objeto.tiempo==tiempo and actual.objeto.amplitud==amplitud:
                return actual.objeto.dato
            actual = actual.siguiente

    def recorrerm(self):
        actual = self.primero
        print("-------------------Matriz reducida---------------------")
        while actual != None:
            print("grupo:",actual.objeto.grupo,"amplitud:",actual.objeto.amplitud,"dato:",actual.objeto.dato,
                  "cadena_patron:",actual.objeto.cadena_patron,"num_filas",actual.objeto.num_filas)
            actual=actual.siguiente

    def recorrer(self):
        actual = self.primero
        print('---------------------Identificadores Patrones-------------------')
        while actual != None:
            print('fila_tiempo:',actual.objeto.fila_tiempo,'cadena_patron:',actual.objeto.cadena_patron)
            actual=actual.siguiente

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual=self.primero
        while actual !=None:
            print("tiempo:",actual.objeto.tiempo,"Amplitud:",actual.objeto.amplitud,
                "dato:",actual.objeto.dato)
            actual=actual.siguiente
        print("============================================================")
    
    def crear_g_datos(self,nombre_senal,tiempot,amplitudt):
        imagen =open('bb.dot','w',encoding="UTF-8")
        texto = """digraph G{fontname="Helvetica,Arial,sans-serif"node [fontname="Helvetica,Arial,sans-serif"]edge [fontname="Helvetica,Arial,sans-serif"]"""
        texto+="""start[label=\""""+nombre_senal+"""\"]"""
        texto+="""tiempo[label=\"t="""+tiempot+"""\"]"""
        texto+="""amplitud[label=\"A="""+amplitudt+"""\"]"""
        texto+="""start->tiempo;"""
        texto+="""start->amplitud;"""
        actual = self.primero
        contador= 1
        while actual != None:
            if contador<=int(amplitudt):
                texto+=str(contador)+"""[label=\""""+str(actual.objeto.dato)+"""\"]"""
                texto+="""start->"""+str(contador)+""";"""
            else:
                texto+=str(contador)+"""[label=\""""+str(actual.objeto.dato)+"""\"]"""
                texto+=str(contador-int(amplitudt))+"""->"""+str(contador)+""";"""
            contador+=1
            actual = actual.siguiente
        texto+="""}"""
        imagen.write(texto)
        imagen.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Senal_audio.png')
    
    def crear_g_reducida(self,nombre_senal,amplitudt):
        imagen =open('bb.dot','w',encoding="UTF-8")
        texto = """digraph G{fontname="Helvetica,Arial,sans-serif"node [fontname="Helvetica,Arial,sans-serif"]edge [fontname="Helvetica,Arial,sans-serif"]"""
        texto+="""start[label=\""""+nombre_senal+"""\"]"""
        texto+="""amplitud[label=\"A="""+amplitudt+"""\"]"""
        texto+="""start->amplitud;"""
        actual = self.primero
        contador= 1
        centinela_grupo= actual.objeto.grupo
        while actual!= None:
            if contador==1:
                texto+="""a"""+str(contador)+"""[label=\"g="""+str(contador)+""" (t="""+str(actual.objeto.grupo)+""")\"]"""
                texto+= """start->a"""+str(contador)+""";"""
                contador+= 1
            else:
                if centinela_grupo!=actual.objeto.grupo:
                    texto+="""a"""+str(contador)+"""[label=\"g="""+str(contador)+""" (t="""+str(actual.objeto.grupo)+""")\"]"""
                    texto+= """a"""+str(contador-1)+"""->a"""+str(contador)+""";"""           
                    contador+= 1
                    centinela_grupo=actual.objeto.grupo
            actual = actual.siguiente
        actual2 = self.primero
        contador= 1
        while actual2 != None:
            if contador<=int(amplitudt):
                texto+=str(contador)+"""[label=\""""+str(actual2.objeto.dato)+"""\"]"""
                texto+="""start->"""+str(contador)+""";"""
            else:
                texto+=str(contador)+"""[label=\""""+str(actual2.objeto.dato)+"""\"]"""
                texto+=str(contador-int(amplitudt))+"""->"""+str(contador)+""";"""
            contador+=1
            actual2 = actual2.siguiente
        texto+="""}"""
        imagen.write(texto)
        imagen.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Senal_audio_reducida.png')
