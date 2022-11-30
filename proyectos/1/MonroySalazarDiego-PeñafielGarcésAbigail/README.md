# **El Pumacafé**

Los estudiantes Diego y Abigail necesitan dinero para continuar con sus proyectos de la carrera. 
Así que ambos deciden poner una cafetería, al no poder contratar más personas ellos serán los dos meseros. 
Tampoco disponen de un espacio grande por lo que solo pueden atender a 10 personas de forma adecuada. 
Además de ofrecer el menú también preparan y entregan las bebidas, solo pueden hacer uno a la vez por supuesto. 
Los clientes piden su bebida, al recibirla la toman cuando la terminan pasan a caja y salen de la cafetería satisfechos con el servicio. 

Si otro cliente después del décimo quiere entrar debe esperar a que salga uno, queremos evitar ordene desde afuera. 
Queremos evitar que un mesero tome una nueva orden sin preparar la anterior. O que tome otra orden sin entregar la bebida.

No necesitamos el ordenamiento relativo en la salida de clientes mientras no esté en su máxima capacidad la cafetería. 
Mientras sean clientes diferentes pueden pedir y beber sus bebidas sin necesidad de ordenamiento.

## **Reglas**
- Hay 2 meseros.

- El café puede albergar 10 clientes máx.

- Un mesero no puede entregar bebidas, ofrecer un menú o preparar la bebida al mismo tiempo.

- Al terminar su bebida el cliente se va.

- El cliente tarda 2 segundos en pedir su bebida.

- La preparación de la bebida toma 5 segundos.

- El cliente debe tomar su bebida en 10 segundos.

## **Implementación**
Creamos un código en lenguaje python llamado proyectoSO.py . Nuestros puntos de sincronización son *creación de hilos, filtro y ordenar*.

### *Creación de hilos*
Creamos los hilos cliente y empleado. Procedemos a ejecutar el hilo de los meseros y hasta que dejen de venir 
clientes seguirán ejecutándose los hilos empleado y cliente.

![CreaHilos](https://user-images.githubusercontent.com/38671407/204729271-0bc70803-8380-4154-a859-0536e142d5b3.PNG)

### *Filtro*
Dentro de la creación de nuestro hilo cliente haremos nos cuente los clientes para mantener 
un control de los mismos y que no entren muchos si nuestro mesero está ocupado.

![Filtro](https://user-images.githubusercontent.com/38671407/204729410-70a285a0-ec27-4fe5-b463-faae5729eb19.PNG)

### *Ordenar*
Definimos pedir para determinar cómo se comportan nuestros clientes. Aquí vemos que en ciertas acciones debe esperar al mesero para pasar a la siguiente.

![Ordena](https://user-images.githubusercontent.com/38671407/204729571-f45f3dd2-db16-46e6-ba0f-e9cf5024b21b.PNG)

## **Descripción del entorno de desarrollo**
Utilizamos python versión 3.9.

Usamos las bibliotecas threading, time y random.

Lo desarrollamos en Visual Studio Code, para probarlo usamos la terminal del mismo. Nos enviamos el código cuando actualizamos algo en el.

## **Ejemplos de ejecución**
![Captura](https://user-images.githubusercontent.com/38671407/204729938-7c30f4a0-78a5-459e-a207-ae5def459c96.PNG)
![Captura1](https://user-images.githubusercontent.com/38671407/204729941-b423bf52-0e89-4a0c-95ef-b94a36ac0363.PNG)
![Captura2](https://user-images.githubusercontent.com/38671407/204729944-927f7c65-68f5-4d03-b3de-1c126886ecd6.PNG)
![Captura4](https://user-images.githubusercontent.com/38671407/204729946-4c784e8f-9cba-4ea9-9c71-b10f501720ba.PNG)

