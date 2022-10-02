memoria="------------------------------"
p_list=["A","B","C","D","E","F","G","H","I","j","K","L","M","N","O"];
p_possible={"A","B","C","D","E","F","G","H","I","j","K","L","M","N","O"}
choose = "1"

print("Asignación actual:\n"+memoria+"\n")


while(choose == "1"):
    choose1 = "2";
    choose1 = input("Asignar (0) o liberar (1): ")
    #asignar
    if (choose1 == "0"):
        current = 0;
        #Checa cual proceso esta disponible
        for x, process in enumerate(p_list):
            if(process in p_possible):
                current = process
                p_size = int(input("Tamaño del nuevo proceso ("+process+"):"))
                if p_size in range(2,16):
                    count2 = 0
                    #checa si el proceso cabe en el espacio total disponible
                    for char in memoria:
                        if char == '-': count2 += 1
                    entered = 0;
                    #checa si el proceso cabe en algun espacio disponible (mejor ajuste)
                    for y , char in enumerate(memoria):
                        count = 0
                        if char == '-':
                            start = y;
                            for char2 in memoria[start:]:
                                if char2 == '-': count += 1
                                else: break
                            #si el proceso cabe en el espacio lo asigna a este
                            if count >= p_size:
                                entered = 1;
                                aux=""
                                for y in range(0, p_size):
                                    aux=aux+process
                                memoria = memoria[0:start]+aux+memoria[(start+p_size):]
                                print("Asignación actual (primer ajuste):\n"+memoria+"\n")
                                p_list[x]=0
                                break
                    if entered == 0:
                        #compactación
                        if count2 >= p_size:
                            print("Compactación necesaria")
                            aux2=""
                            aux3=[]
                            aux4=""
                            for char in memoria:
                                if char in p_possible and char != aux2:
                                    aux2 = char
                                if char == aux2:
                                    aux4 = aux4 + char
                                if char == "-" and aux2 in p_possible:
                                    aux3.append(aux4)
                                    aux4=""
                                    aux2 =""
                            print(aux3)
                            compressed = ""
                            for process2 in aux3:
                                compressed = compressed + process2
                            c_size=len(compressed)
                            aux5=""
                            for x3 in range(0,30-c_size):
                                aux5=aux5+"-"
                            memoria = compressed + aux5
                            print("Asignación actual:\n"+memoria+"\nAsignando el proceso :")
                            #asigna el nuevo proceso a la memoria ya comprimida
                            aux=""
                            for x4 in range(0, p_size):
                                aux=aux+process
                            memoria=compressed+aux+memoria[(c_size+p_size):]
                            print("Asignación actual:\n"+memoria+"\n")
                            p_list[x]=0
                        if count2 <= p_size:
                            print("Espacio de memoria insuficiente")
                #print(p_list)
                else:
                    print("Tamaño incorrecto. El tamaño del proceso debe de estar entre 2 y 15 unidades")
                break
    if (choose1 == "1"):
        #liberar
        liberable=""
        for w in p_possible:
            if w not in p_list:
                liberable=liberable+w
        process = input("Proceso a liberar ("+liberable+"): ").upper()
        if (process in p_possible and process not in p_list):
            for x , char in enumerate(memoria):
                if char == process:
                    memoria = memoria[0:x]+"-"+memoria[(x+1):]
            index = p_list.index(0)
            p_list[index]=process
            print("Asignación actual:\n"+memoria+"\n")
        else:
            print("No elegiste un proceso liberable.")

    choose = input("\n¿Quieres continuar? NO(0) SI(1)")
