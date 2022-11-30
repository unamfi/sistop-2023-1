#**Una situación cotidiana paralelizable**

##**Situación a modelar**
Se planea implementar una pizzeria con servicio a domicilio. En la pizzeria se realizan pedidos mediante llamadas telefónicas, estas llamadas son atendidas por dos recepcionistas, los clientes pediran sus pizzas (máximo 3) y estas serán hechas por los dos cocineros del local.
Cada repartidar debera esperar a tener 3 ordenes en su caja de reparto para poder salir a repartir. Se dira que no importa lo que sucede despues de salir de la pizzeria. 

##**¿Donde pueden verse las consecuencias nocivas de la concurrencia? ¿Qué eventos pueden ocurrir que queramos controlar?**
Un factor nocivo de la concurrencia puede ser el hecho de que se deberá esperar a tener 3 ordenes para repartir incluso si algunas tardan en salir.
Hay que controlar:
	- que las 2 recepcionistas no se saturen de trabajo
	- que los cocineros saquen pedidos completos al tiempo y no de diferentes ordenes
	- que el horno no se sobrepase la capacidad máxima de pizzas
	- que el repartidor solo reparta pedidos completos
	- que el repartidor solo pueda salir del local si se tienen 3 ordenes para aminorar el uso de gasolina
 
##** ¿Hay eventos concurrentes para los cuales el ordenamiento relativo no resulta importante?**
No interesa que las pizzas correspondientes a un mismo pedido entren separadas al horno y tampoco interesa cual orden es completada primero.