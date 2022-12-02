import threading 
import sys
import random
import time

##Funciones para imprimir mensajes en diferentes colores: Rojo cuando el amigo se enoja y logran que regrese, 
#Verde  para saber quienes estan disponibles, rosa informa en que tarea se encuentra

def print_fail(message, end = '\n'):
    sys.stderr.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

def print_pass(message, end = '\n'):
    sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

def print_info(message, end = '\n'):
    sys.stdout.write('\x1b[1;35m' + message.strip() + '\x1b[0m' + end)

## Lista de empleados y diccionario que nos permite identificar 
empleados = ['Chef','Pastelero','Bartneder','Mesero','Cajero','Recepcionista','Seguridad']
Diccionario = {1:['Limpiar la mesa','Lavar el baño','Trapear','Barrer'],
               2:['Lavar baño','Sacar basura'],
               3:['Ordenar la bodega']}

##Mutex para tenerlos en las clases tarea, persona y Casa
mutexTarea = threading.Semaphore(1)
mutexEmpleado = threading.Semaphore(1)
empleadoDisponible =[]
listaDeTareas =[]

#El numero va cambiando
cantidad_empleados = 5
tareasdelDia = 5

## Multiplex evitar que se usen más personsa o tareas de los establecidos 
tareas = threading.Semaphore(tareasdelDia)
empleadosN = threading.Semaphore(cantidad_empleados)

#CuentaListos para la barrera
cuentaListos = 0


mutexListos = threading.Semaphore(1)
barreraListos = threading.Semaphore(0)
desertor = threading.Semaphore(1)

class Tarea:
    def __init__(self,numero,requeridosParaUnaTarea,nombreTarea):
        self.numero = numero
        self.requeridosParaUnaTarea = requeridosParaUnaTarea
        self.nombreTarea = nombreTarea
        self.barrera = threading.Semaphore(0)
        self.identificarTarea()


    def identificarTarea(self):
        global empleadosN, mutexTarea, listaDeTareas
        mutexTarea.acquire()
        if cuentaListos == cantidad_empleados:
                barreraListos.release()
        listaDeTareas.pop(0)
        self.realizarse(self.numero,self.nombreTarea,self.requeridosParaUnaTarea)
        #Sacamos una por una las tareas en el orden en que llegaron a listaDeTareas.append(threading.Thread(target = Tarea, args= [y, requeridosParalaTarea,nombreTarea]).start())
        mutexTarea.release()

    def realizarse(self,numero,nombreTarea,requeridosParalaTarea):
        global empleadosN, empleadoDisponible, cantidad_empleados
        requeridos = []
        for i in range(requeridosParalaTarea):
            empleadosN.acquire()
            mutexEmpleado.acquire()
            # Sacamos algunos de los empleados requeridos que estén disponibles para hacer la tarea
            requeridos.append(empleadoDisponible.pop(random.randrange(len(empleadoDisponible))))
            mutexEmpleado.release()
            mutexEmpleado.acquire()
            mutexEmpleado.release()
        for i in requeridos: ## A éstos los ponemos a trabajar
            i.Trabajar(nombreTarea)
        while True:
            if all(elem in empleadoDisponible for elem in requeridos): 
                ##Hasta que todos hayan terminado la tarea, se dará por concluída la tarea y quitamos la barrera
                print('\n\t',requeridosParalaTarea,'ha(n) terminado la tarea:',nombreTarea,'\n')
                self.barrera.release()
                self.barrera.acquire()
                self.barrera.release()
                break
        for i in range(requeridosParalaTarea): 
            #Liberamos los mutex para evitar que se usen más de las personas necesarias
            empleadosN.release()

class Persona:
    def __init__(self,numero,empleados):
        self.numero = numero 
        self.empleados = empleados
        self.descanso = threading.Semaphore(0)
        self.entrarDisponible('vacio')

    def entrarDisponible(self,nombreTarea):
        global cuentaListos,barreraListos,mutexListos
        if nombreTarea == 'vacio': 
            mutexEmpleado.acquire()
            cuentaListos = cuentaListos + 1
            print_pass(str(self.empleados)+str(self.numero)+' "preparado para limpiar"')
            mutexEmpleado.release()
            mutexEmpleado.acquire()# Para que pase uno por uno
            mutexEmpleado.release()
            empleadoDisponible.append(self)
            barreraListos.acquire()## Barrera  para verificar que todos estén listos para iniciar
            if cuentaListos == cantidad_empleados:
                barreraListos.release() #Liberamos la barrera
           
        else:
            mutexEmpleado.acquire()
            if random.random() < 0.1: # Si llega un 
                print_fail(self.empleados+str(self.numero)+" ¡¡Me voy!! ")
                print("\n")
                print("     !!! INTERVENCION !!!     ")
                print("\n")
                desertor.acquire()
                time.sleep(0.5)# Si hay alguien enojado paramos todo
                desertor.release()
                print_fail(self.empleados+str(self.numero)+" ¡Nunca me fui! ")
                empleadoDisponible.append(self)
                mutexEmpleado.release()
            else:
                empleadoDisponible.append(self)
                mutexEmpleado.release()

    def Trabajar(self,nombreTarea):
        global mutexTarea, empleadoDisponible 
        self.descanso.release()## Lo sacamos del descanso
        print_info(self.empleados+str(self.numero)+" está trabajando en "+nombreTarea)
        time.sleep(random.random()) ## Tiempo en que tarda hacer una tarea una persona
        print(self.empleados,self.numero,'dejó de trabajar en',nombreTarea)
        self.entrarDisponible(nombreTarea)



class restaurante:
    def __init__(self, cantidad_empleados, tareasdelDia):
        global listaDeTareas, empleadoDisponible 
        for x in range(cantidad_empleados):
            ## Lanzamos todos los hilos de personas para que se enlisten a personas listas, con random hacemos que sean aleatorios los empleados
            threading.Thread(target = Persona, args=[x,empleados[random.randrange(7)]]).start()
        
        for y in range(tareasdelDia):
            requeridosParalaTarea = random.randrange(1,4)
            posibilidad = Diccionario[requeridosParalaTarea]
            ## Damos tareas aleatorias del diccionario por lo que pueden repetirse, al igual que algunas ocupan 1,2 o 3 personas para realizarse
            nombreTarea = random.choice(posibilidad)
            mutexTarea.acquire()          
            listaDeTareas.append(threading.Thread(target = Tarea, args= [y, requeridosParalaTarea,nombreTarea]).start())
            mutexTarea.release()
            mutexTarea.acquire()
            mutexTarea.release()


if __name__ == '__main__':
    print("\n")
    print("Estamos preparados para limpiar")
    
    print("\n")
    cantidad_empleados = int(input("¿Cuántos amigos disponibles para limpiar?: "))
    tareasdelDia = int(input("¿Cuantas tareas realizaremos tenemos hoy?: "))
    friends = restaurante(cantidad_empleados,tareasdelDia)