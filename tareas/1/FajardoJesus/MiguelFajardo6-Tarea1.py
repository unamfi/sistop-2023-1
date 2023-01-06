#Simulación de proceso por peor ajuste
#Fajardo Suárez Jesús Miguel      Tarea 1      Sistemas Operativos
class Proceso: #Definición de la clase proceso
    def __init__(self, nombre, espacio, tiempo):
        self.nombre = nombre
        self.espacio = espacio
        self.tiempo = tiempo

process = []
Memoria = []
Cola = []
borrar=[]
Elim=[]
libre = []
#Procesos a agregar
p1 = Proceso('A', 5, 4)
p2 = Proceso('B', 3, 8)
p3 = Proceso('C', 10, 4)
p4 = Proceso('D', 9, 11)
p5 = Proceso('E', 8, 2)
p6 = Proceso('F', 7, 5)
#Agregado de procesos
process.append(p1)
process.append(p2)
process.append(p3)
process.append(p4)
process.append(p5)
process.append(p6)
Espa = 0 
#Se guardan los primeros procesos
def Guardar():
    global Espa
    for x in range(len(process)):
        if Espa + process[x].espacio < 30: #Si hay espacio suficiente se guarda el proceso en la memoria
            Espa = Espa + process[x].espacio
            for n in range(process[x].espacio):
                    Memoria.append(process[x].nombre)
        else: #En caso contrario se agrega el proceso a la cola
            Cola.append(process[x])
            print("No se puede agregar el proceso " + process[x].nombre + " Memoria llena")
    for x in range(30-Espa): #Se rellenan espacios vacios con guiones 
        Memoria.append("-")
    libre.append((29,Espa)) #Se marcan espaciós libres
    for x in range(len(Cola)): #Se eliminan elementos que no entraron a la memoria
        process.pop()
    print("Memoria llenada")
    print(Memoria)
    proceso()
    
    return 0
        
def proceso ():
    global Espa
    m=0
    comp = process[0].tiempo
    for x in range(len(process)): #Aqui se hara la simulacion del tiempo que ocupa cada proceso
        if comp > process[x].tiempo: #Se busca el que tenga menor tiempo
            comp = process[x].tiempo
    for x in range(len(process)):
        process[x].tiempo = process[x].tiempo - comp
        if process[x].tiempo == 0: #El proceso que ya termino de realizarce es decir el que menos tiempo tiene
            Elim.append(x)         #se elimina y se agrega a la memoria
            A= str(process[x].nombre)
            for n in range(len(Memoria)):
                if Memoria[n] == A:
                    Memoria[n] = "-"
                    Espa = Espa - 1
                    m=n
            libre.append((m,m-process[x].espacio+1))
            print("Proceso " + process[x].nombre + " terminado")
            print(Memoria)
    for x in range(len(Elim)):
        process.pop(Elim[x])
    Elim.clear()
    if Cola:  #Si hay algo encolado se buscara si entra un nuevo proceso ya que hay espacio
        Encolado()
   
              
def Encolado():
    libElim=[]
    global Espa
    for x in range(len(libre)):
        a = libre[x][1]
        b = libre[x][0]
        c = b-a
        for n in range(len(Cola)): #Se recorre la cola
            if c >= Cola[n].espacio: #Y si ese elemento cabe en el espacio seleccionado se agrega a la memoria
                libElim.append(x)
                Elim.append(n)
                for k in range(Cola[n].espacio):
                    Memoria[a] = Cola[n].nombre
                    a=a+1
                    Espa=Espa+1
                print(Cola[n].nombre + " Agregado por peor ajuste\n")
                print(Memoria)
            break
    for x in range(len(Elim)):
        Cola.pop(Elim[x])
        libre.pop(libElim[x])
    Elim.clear()
    libElim.clear()
                
    if Cola: #Si hay elementos encolados se solicita un ajuste de memoria
        Ajuste()
    else:   #De lo contrario se hace simulacion del tiempo
        proceso()

def Ajuste(): #Aqui simplemente se toman todos los guiones y se reajustan los espacios libres
    global Espa #Se ajusta el espacio y se regresa a la entrada de cola
    libre.clear()
    c=0
    for x in range(Memoria.count("-")):
        Memoria.remove("-")
        Espa = Espa - 1
        c = c+1
    b = 29-Espa
    libre.append((29,30-c))
    for x in range(29-b):
        Memoria.append("-")
    print("Compactación de memoria")
    print(Memoria)
    Encolado()
Guardar()

