#include<stdio.h>
#include<stdlib.h>
#define pf printf
#define sf scanf
#define espacio pf("\n")
#define limpiar system("cls")
int Verifica(int num[], int n,  int na);
int mate(int num[], int n);
int esp(int num[], int n);
int histM(int num[], int n);
int hist(int num[], int n);
int fis(int num[], int n);
int formacion(int num[], int n);
int habM(int num[], int n);
int quim(int num[], int n);
int bio(int num[], int n);
int habV(int num[], int n);
int geo(int num[], int n);
void general();
void portada();
int main()
{
    inicio://Esto englobara todo lo que esta adentro del int main para que se regrese hasta este punto y se creen nuevo num aleatorios
    {
        portada();//Portada del programa
        system("color F0");//Pone un fondo de color
        int numero[12],nA, i, opc;                  //***Todo esto engloba el proceso para obtener numeros al
        srand(time(NULL));                          //azar y guardarlos en un vector***
        for(i=0;i<12;i++)
        {
            nA=rand()%24+1;
            while(Verifica(numero, 12, nA)==1)//Verifica que el numero aleatorio no se haya usado ya
            {
                nA=rand()%24+1;//da un numero aleatorio en cierto rango(1-24)
            }
            numero[i]=nA;                           //***Aqui termina el proceso para obtener numeros aleatorios***
        }
        //Menu
        pf("Bienvenido al SEIB\n");
        espacio;
        pf("Elige un examen\n");
        pf("1)Matem%cticas\n2)Espa%col\n3)Historia de M%cxico\n4)Historia universal\n5)F%csica\n6)Formaci%cn c%cvica y %ctica\n7)Habilidad Matem%ctica\n8)Qu%cmica\n9)Biolog%ca\n",160,164,130,161,162,161,130,160,161,161);
        pf("10)Habilidad verbal\n11)Geograf%ca\n12)Examen general\n",161);
        sf("%i", &opc);
        limpiar;
        switch(opc)//Estructura de seleccion para el tipo de examen
        {
            case 1:
                mate(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 2:
                esp(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 3:
                histM(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 4:
                hist(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 5:
                fis(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 6:
                formacion(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 7:
                habM(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 8:
                quim(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 9:
                bio(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 10:
                habV(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 11:
                geo(numero, 12);
                limpiar;
                goto inicio;
            break;
            case 12:
                general://Para abarcar todo el case 12
                {
                    FILE *datos;
                    char res[4]={'\0'};
                    int sel, nI=1, i=0, n;
                    pf("Conocimientos generales\n\n");
                    pf("Elige\n");
                    pf("1)Hacer examen\n2)Ver resultados anteriores\n");
                    sf("%i", &sel);
                    switch(sel)
                    {
                        case 1:
                            general(numero, 12);
                            limpiar;
                            goto inicio;
                        break;
                        case 2:
                            datos=fopen("DatosUsuario.txt", "r");
                            if(datos==NULL)
                            {
                                pf("Aun no hay datos guardados\n");
                                system("pause");
                                limpiar;
                                goto inicio;
                            }
                            else
                            {
                                limpiar;
                                pf("Resultados anteriores\n\n");
                                while(!feof(datos))
                                {
                                    if(fgetc(datos)!='\n' && !feof(datos))
                                    {
                                        fseek(datos, -1, SEEK_CUR);
                                        res[i]=fgetc(datos);
                                        i++;
                                    }
                                    else
                                    {
                                        printf("Examen %i: %s\n",nI, res);
                                        for(i=0;i<3;i++)
                                        {
                                            res[i]='\0';
                                        }
                                        i=0;
                                        nI++;
                                    }
                                }
                                system("pause");
                                limpiar;
                                goto inicio;
                            }
                        break;
                        default:
                            pf("Selecciona una opcion valida\n");
                            system("pause");
                            limpiar;
                            goto general;
                        break;
                    }
                }
            break;
            default:
                pf("Selecciona una opcion valida\n");
                system("pause");
                limpiar;
                goto inicio;
            break;
        }
    }
}
int Verifica(int num[], int n,  int na)
{
    int i;
    for(i=0;i<n;i++)//Ciclo para comparar los espacios del vector num con el numero aleatorio obtenido
    {
        if(na==num[i])
        {
            return 1;
        }
    }
    return 0;
}
int  mate(int num[], int n)
{
    int i, aci=0, nP;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])//Seleciona una pregunta aleatoriamente
        {
            case 1:
                pf("%i.-Resuelve x+2=(3/4)+5x\n", nP);
                pf("a)x=0.312\nb)x=2.321\nc)x=0.342\nd)x=1/5\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)x=0.312\n");
                system("pause");
                limpiar;
            break;
            case 2:
                pf("%i.-Resuelve (1/x)=(4/3)-1\n", nP);
                pf("a)x=1/3\nb)x=3\nc)x=2\nd)No hay soluci%cn\n",162);
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='b' || opc=='B')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)x=3\n");
                system("pause");
                limpiar;
            break;
            case 3:
                pf("%i.-Resuelve x(x)=4\n", nP);
                pf("a)x=2\nb)x=4\nc)x=-2\nd)x=2 y x=-2\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='d' || opc=='D')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: d)x=2 y x=-2\n");
                system("pause");
                limpiar;
            break;
            case 4:
                pf("%i.-%cQu%c n%cmero es n en la siguiente sucesi%cn?\n", nP,168,130,163,162);
                pf("1,2,4,8,16,n\n");
                pf("a)0\nb)2\nc)20\nd)32\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='d' || opc=='D')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: d)32\n");
                system("pause");
                limpiar;
            break;
            case 5:
                pf("%i.-%cCu%cl es el s%cptimo elemento de la siguiente sucesi%cn?\n", nP, 168,160,130, 162);
                pf("10,5,5/2,5/4,5/8,...\n ");
                pf("a)x=5/16\nb)x=0\nc)x=-1\nd)x=5/32\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='d' || opc=='D')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: d)5/32\n");
                system("pause");
                limpiar;
            break;
            case 6:
                pf("%i.-%cCu%cl n%cmero es n en la siguiente sucesi%cn?\n", nP,168, 160,163, 162);
                pf("1,3/2,9/4,27/6,n\n");
                pf("a)9/32\nb)81/8\nc)27/128\nd)Ninguna de las anteriores\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='b' || opc=='B')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)81/8\n");
                system("pause");
                limpiar;
            break;
            case 7:
                pf("%i.-%cQu%c es igual a seno?\n", nP,168,130);
                pf("a)C.O/H\nb)H/C.O\nc)C.A/H\nd)C.A/C.O\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)C.O/H\n");

                system("pause");
                limpiar;
            break;
            case 8:
                pf("%i.-%cCu%cl es el seno  del siguiente tri%cngulo?\n", nP,168,160, 160);
                pf("C.O=1, H=2\n");
                pf("a)0\nb)1/2\nc)2\nd)1\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='b' || opc=='B')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)1/2\n");
                system("pause");
                limpiar;
            break;
            case 9:
                pf("%i.-Resuelve |[|-4|+(2/5)-1]|\n", nP);
                pf("a)5\nb)17\nc)17/5\nd)Ninguna de las anteriores\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)17/5\n");
                system("pause");
                limpiar;
            break;
            case 10:
                pf("%i.-Si entre pablo, diego y yo tenemos 24 canicas, y pablo tiene 2 veces las canicas que yo tengo y diego tiene 6 canicas %cCu%cntas canicas tengo yo?\n", nP,168,160);
                pf("a)10\nb)12\nc)6\nd)9\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='d' || opc=='D')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: d)9\n");
                system("pause");
                limpiar;
            break;
            case 11:
                pf("%i.-Resuelve: x+2=2x-2\n", nP);
                pf("a)x=10\nb)x=5\nc)x=4\nd)x=2\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)x=4\n");
                system("pause");
                limpiar;
            break;
            case 12:
                pf("%i.-%cCu%cnto es 0 entre 0?\n", nP,168,160);
                pf("a)0\nb)2\nc)No existe\nd)1\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)No existe\n");
                system("pause");
                limpiar;
            break;
            case 13:
                pf("%i.-%cCu%cl de estos NO es un n%cmero primo?\n", nP,168,160,163);
                pf("a)1\nb)2\nc)3\nd)5\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)1\n");
                system("pause");
                limpiar;
            break;
            case 14:
                pf("%i.-%cCu%cl de estos n%cmeros es m%cltiplo de 3?\n", nP,168,160,163,163);
                pf("a)1\nb)72\nc)7\nd)10\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='b' || opc=='B')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)72\n");
                system("pause");
                limpiar;
            break;
            case 15:
                pf("%i.-En la fraccion (10/5)=2\n", nP);
                pf("Cual es el cociente?\n");
                pf("a)10\nb)5\nc)2\nd)No hay cociente\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)2\n");
                system("pause");
                limpiar;
            break;
            case 16:
                pf("%i.-Residuo entero de 10/3\n", nP);
                pf("a)1\nb)2\nc)3\nd)4\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)1\n");
                system("pause");
                limpiar;
            break;
            case 17:
                pf("%i.-%cCu%cntos grados suman los %cngulos interiores de un tri%cngulo?\n", nP,168,160,160,160);
                pf("a)120\nb)100\nc)180\nd)360\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)180\n");
                system("pause");
                limpiar;
            break;
            case 18:
                pf("%i.-%cCu%cnto es 2 a la  potencia 0?\n", nP,168,160);
                pf("a)2\nb)1\nc)0\nd)No existe\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='b' || opc=='B')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)1\n");
                system("pause");
                limpiar;
            break;
            case 19:
                pf("%i.-Sea el tri%cngulo con %cngulos interiores:\n", nP,160,160);
                pf("\na=100 grados, b=20 grados, c= x grados\n");
                pf("Cuanto vale x?\n");
                pf("a)60\nb)40\nc)200\nd)180\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)60\n");
                system("pause");
                limpiar;
            break;
            case 20:
                pf("%i.-%cQu%c es igual a coseno?\n", nP,168,130);
                pf("a)C.O/H\nb)C.A/H\nc)H/C.O\nd)C.O/C.A\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='d' || opc=='D')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: d)C.O/C.A\n");
                system("pause");
                limpiar;
            break;
            case 21:
                pf("%i.-%cQu%c es igual a coseno?\n", nP,168,130);
                pf("a)C.O/C.A\nb)C.A/H\nc)C.A/C.O\nd)H/C.O\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: b)C.A/H\n");
                system("pause");
                limpiar;
            break;
            case 22:
                pf("%i.-Si el lado de un cuadrado es igual a 5 unidades\n", nP);
                pf("%cCu%cl es su %crea en unidades cuadradas?\n",168,160,160);
                pf("a)25\nb)50\nc)5\nd)20\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='a' || opc=='A')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: a)25\n");
                system("pause");
                limpiar;
            break;
            case 23:
                pf("%i.-%cCu%cnto vale f(x) cuando x vale 1?\n", nP,168,160);
                pf("f(x)=x+1\n");
                pf("a)1\nb)4\nc)2\nd)11\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)2\n");
                system("pause");
                limpiar;
            break;
            case 24:
                pf("%i.-%cCu%cnto vale f(x) cuando x vale -1?\n", nP,168,160);
                pf("f(x)=2x+1\n");
                pf("a)1\nb)-2\nc)-1\nd)0\n");
                fflush(stdin);
                scanf("%c", &opc);
                if(opc=='c' || opc=='C')
                {
                    aci++;
                }
                pf("\nRespuesta correcta: c)-1\n");
                system("pause");
                limpiar;
            break;
        }
    }
    // Imprime los acierto y retorna valor
    pf("Tuviste %i aciertos\n\n", aci);
    system("pause");
    return aci;
}
int esp(int num[], int n)
{
    int i, aci=0, nP;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
    {
        case 1:
            pf("%i.-La ficha_______tiene la funci%cn de ayudarnos a conservar los datos de una obra\n", nP,162);
            pf("a)profesiografica\nb)de cita textual\nc)de trabajo\nd)bibliogr%cfica\n",160);
            fflush(stdin);
            sf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)bibliogr%cfica\n.",160);
            system("pause");
            limpiar;
        break;
        case 2:
        pf("%i.-Se emplea con la finalidad de separar ideas que est%cn relacionadas entre s%c, adem%cs para sumar elementos gramaticales diversos como palabras, frases y oraciones\n", nP,160,161,160);
        pf("a)coma\nb)punto y coma\nc)dos puntos\nd)punto y aparte\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)coma\n");
            system("pause");
            limpiar;
        break;
        case 3:
        pf("%i.-Todos los alumnos podr%can mejorar su desempeno acad%cmico (si) realizaran estrategias de estudio y organizaran su tiempo adecuadamente.", nP,161,130);
        pf("El tipo de nexo que est%c en par%cntesis es:\na)consecutivo\nb)concesivo\nc)condicional\nd)causal\n",160,130);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Condicional\n");
            system("pause");
            limpiar;
        break;
        case 4:
        pf("%i.-Son textos que nos divierten y entretienen con historias y aventuras reales o imaginarias\n", nP);
        pf("a)Cient%cficas\nb)Periodistas\nc)Literarias\nd)Tecnol%cgicas\n",161,162);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Literarias\n");
            system("pause");
            limpiar;
        break;
        case 5:
        pf("%i.-Confrontaci%cn de opiniones que puede estar dirigida por un moderador o persona\n", nP,162);
        pf("a)Entrevista\nb)Debate\nc)Exposici%cn de un tema\nd)Dialogo\n",162);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Debate\n");
            system("pause");
            limpiar;
        break;
        case 6:
        pf("%i.-Son se%cales que avisan al lector lo que sucede dentro de una oraci%cn o p%crrafo\n", nP,164,162,160);
        pf("a)Comillas\nb)punto y coma\nc)Signos de puntuaci%cn\nd)Admiraciones\n",162);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Signos de puntuacion\n");
            system("pause");
            limpiar;
        break;
        case 7:
        pf("%i.-Autor mexicano cuya obra ejemplifica al modernismo\n", nP);
        pf("a)Fernandez de Lizardi\nb)Salvador Diaz Miron\nc)Manuel Payno\nd)Jose Marti\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Salvador Diaz Miron\n");
            system("pause");
            limpiar;
        break;
        case 8:
        pf("%i.-La silaba sobre la cual recae el acento se le conoce como:\n", nP);
        pf("a)Silaba grave\nb)Silaba t%cnica\nc)Silaba atona\nd)Silaba aguda\n",162);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Silaba Grave\n");
            system("pause");
            limpiar;
        break;
        case 9:
        pf("%i.-Toma en cuenta las terminaciones de cada palabra de cada verso\n", nP);
        pf("a)Rima\nb)Estrofa\nc)Met%cfora\nd)Verso\n",160);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Rima\n");
            system("pause");
            limpiar;
        break;
        case 10:
        pf("%i.-Coloca la %cnica opci%cn que incluye un error:\n", nP,163,162);
        pf("a)A%cn lo dudo\nb)En cambio, yo lo acepto\nc)No obstante, te lo dije\nd)Mas sin en cambio, lo sostengo\n",163);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)No obstante, te lo dije\n");
            system("pause");
            limpiar;
        break;
        case 11:
        pf("%i.-Si tuviera que ordenar alfab%cticamente las siguientes palabras.%cCu%cl de ellas colocar%ca en cuarto lugar?\n", nP,130,168,160,161);
        pf("a)Producir\nb)propiciar\nc)Prolongar\nd)Progenitor\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }pf("Respuesta correcta: c)Prolongar\n");
            system("pause");
            limpiar;
        break;
        case 12:
        pf("%i.-El n%ccleo del sujeto siempre es una part%ccula:\n", nP,163,161);
        pf("a)verbal\nb)modificativa\nc)atributiva\nd)sustantiva\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Sustantiva\n");
            system("pause");
            limpiar;
        break;
        case 13:
        pf("%i.-Transmite emociones, preferentemente por medio de formas bellas y elaboradas, despertando el inter%cs del lector y provocando una sensaci%cn placentera.\n", nP,130,162);
        pf("a)Texto Cient%cfico\nb)Texto Literario\nc)Texto Period%cstico\nd)Texto Antiguo\n",161,161);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Texto literario\n");
            system("pause");
            limpiar;
        break;
        case 14:
        pf("%i.-Es quien genera el mensaje dentro del circuito del habla:\n", nP);
        pf("a)Mensaje\nb)Receptor\nc)Emisor\nd)C%cdigo\n",162);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Emisor\n");
            system("pause");
            limpiar;
        break;
        case 15:
        pf("%i.-Conjunto de medios de expresion propios de un grupo determinado, dentro del dominio de una lengua.\n", nP);
        pf("a)Sonido\nb)Senas\nc)Gestos\nd)Habla\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Habla\n");
            system("pause");
            limpiar;
        break;
        case 16:
        pf("%i.-Sistema gr%cfico de registro de los sonidos propios de la lengua:\n", nP,160);
        pf("a)Ideograma\nb)Jerogl%cficos\nc)Alfabeto\nd)Sistema decimal\n",161);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Alfabeto\n");
            system("pause");
            limpiar;
        break;
        case 17:
        pf("%i.-Narraci%cn de sucesos fant%Csticos, a veces con una base hist%crica y que se transmite frecuentemente por tradici%cn oral.\n", nP,162,160,161,162);
        pf("a)Fabula\nb)Novela\nc)Cuento\nd)Leyenda\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Leyenda\n");
            system("pause");
            limpiar;
        break;
        case 18:
        pf("%i.-Figura literaria que consiste en usar palabras con un sentido distinto del propio, en virtud de una comparaci%cn t%ccita.\n", nP,162,160);
        pf("a)Met%cfora\nb)Verso\nc)Hip%crbole\nd)Paradoja\n",160,130);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Met%cfora\n",160);
            system("pause");
            limpiar;
        break;
        case 19:
        pf("%i.-Narraci%cn corta, frecuentemente en verso, de la que se extrae una moraleja:\n", nP,162);
        pf("a)Leyenda\nb)Fabula\nc)Novela\nd)Poema\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Fabula\n");
            system("pause");
            limpiar;
        break;
        case 20:
        pf("%i.-Todas son variaciones propias del adjetivo, excepto:\n", nP);
        pf("a)Aumentativo\nb)Diminutivo\nc)Interrogativo\nd)Calificativo\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Interrogativo\n");
            system("pause");
            limpiar;
        break;
        case 21:
        pf("%i.-Es la persona sobre la que recae la acci%cn expresada por el verbo\n", nP,162);
        pf("a)Objeto Indirecto\nb)Consecuencia\nc)Objeto directo\nd)Voz pasiva\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Objeto directo\n");
            system("pause");
            limpiar;
        break;
        case 22:
        pf("%i.-Palabras en las cuales la %cltima s%claba corresponde a la s%claba t%cnica, y reciben acento escrito si terminan en (n),(s) o (vocal)\n", nP,163,161,161,162);
        pf("a)Agudas\nb)graves\nc)Esdr%cjulas\nd)Sobre esdr%cjulas\n",163,163);
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Agudas\n");
            system("pause");
            limpiar;
        break;
        case 23:
        pf("%i.-Expresa la acci%cn que realiza o padece el sujeto, su existencia o estado, e incluso las modificaciones aportadas a %cste por elementos incluidos en el predicado.\n", nP,162,130);
        pf("a)Articulo\nb)Adjetivo\nc)Sustantivo\nd)Verbo\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Verbo\n");
            system("pause");
            limpiar;
        break;
        case 24:
        pf("%i.-Conjunto de formas de la conjugaci%cn normal de los verbos. En ella, el sujeto (agente) actua, obra; realiza.\n", nP,162);
        pf("a)Tiempo\nb)Voz activa\nc)Voz pasiva\nd)Modo\n");
        fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Voz activa\n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int histM(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++){
        switch(num[i])
        {
        case 1:
            pf("%i.- Cual fue la actividad economica que mas promovio la corona espanola en la Nueva Espana", nP);
            pf("\na)Agricultura\nb)Mineria\nc)Ganaderia\nd)Comercio\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Mineria\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.- Caracteristica que distingue a la Constitucion de 1824", nP);
            pf("\na)La adopcion del sistema federal de gobierno\nb)El establecimiento de la forma de gobierno centralista\nc)El fortalecimiento de una forma de gobierno totalitario\nd)La creacion del sistema presidencialista de gobierno\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) La adopcion del sistema federal de gobierno\n\n", nP);
            system("pause");
            limpiar;

        break;
        case 3:
            pf("%i.- Como se le conocio al grupo de intelectuales que destaco en el gobierno de Porfirio Diaz\n", nP);
            pf("a)Liberales\nb)Contemporaneos\nc)Cientificos\nd)Ateneistas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Cientificos\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.- Nombre que adopto el PNR en 1939, al asumir un contenido mas democratico y popular\n", nP);
            pf("a)Partido Accion Nacional\nb)Partido de la Revolucion Mexicana\nc)Partido Popular Socialista\nd)Partido Nacionalista Democratico\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Partido de la Revolucion Mexicana\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.- Objetivo primordial de la Conspiracion de Queretaro\n", nP);
            pf("a)Constituir una junta gubernativa que tomara el poder a nombre de Fernando VII\nb)Llevar al poder al corregidor Don Miguel Dominguez\nc)Crear una federacion de intendencias novohispanas\nd)Establecer una republica democratica gobernada por Vicente Guerrero\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) Constituir una junta gubernativa que tomara el poder a nomvre de Fernando VII\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-La corriente ideologico politica de la Constitucion de 1857\n", nP);
            pf("a)Conservadora\nb)Liberal\nc)Centralista\nd)Parlamentaria\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Liberal\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-El Partido Antirreeleccionista, la Decena Tragica, el Plan de San Luis, los Tratados de Ciudad Juarez, el sufragio efectivo, la sucesion presidencial de 1910 y el Partido Reyista se asocian a\n", nP);
            pf("a)el movimiento zapatista\nb)la dictadura huertista\nc)el regimen porfirista\nd)el movimiento maderista\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) el movimiento maderista\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-Ante las constantes dificultades de Ferrocariles Nacionales, el presidente Lazaro Cardenas tomo la decision de\n", nP);
            pf("a)autorizar su venta a los extranjeros\nb)convertirlo en una empresa paraestatal\nc)entregar la administracion a los trabajadores\nd)bajar las tarifas a los usuarios nacionales\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) entregar la administracion a los trabajadores\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-La posicion de Mexico ante la Segunda Guerra Mundial fue\n", nP);
            pf("a)romper relaciones diplomaticas con los Aliados\nb)no intervenir en ningun bando\nc)vender petroleo a ambos contendientes\nd)romper relaciones con las potencias del eje\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) romper relaciones con las potencias del eje\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Las politicas neoliberales se iniciaron con el gobierno de\n", nP);
            pf("a)Luis Echeverria Alvarez\nb)Jose Lopez Portillo\nc)Miguel de la Madrid Hurtado\nd)Ernesto Zedillo Ponce de Leon\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Miguel de la Madrid Hurtado\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.- Son instituciones cientificas y culturales del siglo XVIII\n", nP);
            pf("a)Bellas Artes y el Museo de Historia Natural\nb)Colegio de San Idelfonso y el Hospital de Jesus\nc)Academia de San Carlos y el Colegio de Mineria\nd)San Jose de los Naturales y la Universidad de Mexico\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Academia de San Carlos y el Colegio de Mineria\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Que echo relaciona a Miguel Hidalgo en el movimiento de Indepencia\n", nP);
            pf("a)El sitio de Cuautla\nb)La creacion del Congreso de Chilpancingo\nc)La toma de la Alhondiga de Granaditas\nd)La firma de los Tratados de Cordoba\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) La toma de la Alhondiga de Granaditas\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Una de las consecuencias de la guerra contra los Estados Unidos de Amerrica fue la\n", nP);
            pf("a)venta de la Mesilla\nb)firma del Tratado de Guadalupe Hidalgo\nc)firma del Tratado Mc Lane-Ocampo\nd)perdida de El Chamizal\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b)firma del Tratado de Guadalupe Hidalgo\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-La causa principal de la invasion tripartita a nuestro pais fue\n", nP);
            pf("a)la oposicion de Mexico al imperio frances\nb)el deseo espanol de reconquistar Mexico\nc)el establecimiento de la dictadura de Diaz\nd)la suspension del pago de la deuda externa\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d)la suspension del pago de la deuda externa\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-La entrevista que Porfirio Diaz concedio al periodista James Creelman sirvio para\n", nP);
            pf("a)reafirmar a Diaz en el poder\nb)recuperar el prestigio de Mexico en el extranjero\nc)reforzar la relacion bilateral con Estados Unidos y Europa\nd)alentar la creacion de partidos y movimientos de oposicion\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) alentar la creacion de partidos y movimientos de oposicion\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-La corriente ideologico politica de la Constitucion de 1857\n", nP);
            pf("a)Conservadora\nb)Liberal\nc)Centralista\nd)Parlamentaria\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
             pf("Respuesta b) Liberal\n\n", nP);
            system("pause");
            limpiar;
            break;
        case 17:
            pf("%i.-El Plan de Ayala fijaba la posicion politica y agraria de los\n", nP);
            pf("a)villistas\nb)zapatistas\nc)carrancistas\nd)obregonistas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) zapatistas\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Presidente que creo la Secretaria de Educacion Publica\n", nP);
            pf("a)Lazaro Cardenas\nb)Alvaro Obregon\nc)Venustiano\nd)Victoriano Huerta\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Alvaro Obregon\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Presidente que creo el ejido colectivo\n", nP);
            pf("a)Alvaro Obregon\nb)Adolfo Lopez Mateos\nc)Manuel Avila Camacho\nd)Lazaro Cardenas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) Lazaro Cardenas\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 20:
             pf("%i.-Un crecimiento economico sostenidode mas del 6%% anual y la construccion de infraestructura fueron hechos que, entre 1952 y 1970, se conocieron como\n", nP);
            pf("a)Plan Sexenal\nb)Desarrolo compartido\nc)Milagro mexicano\nd)Unidad nacional\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Milagro mexicano\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-Politica economica que aplico el gobierno de Mexico de 1970-1982\n", nP);
            pf("a)Sustitucion de importaciones\nb)Neoliberalismo\nc)Desarrollo estabilizador\nd)Desarrolo compartido\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) Desarrolo compartido\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Ultimo virrey que ratifica el Plan de iguala y reconoce a Mexico como nacion independiente de\n", nP);
            pf("a)Luis de Velasco\nb)Juan O Donoju\nc)Fray Juan de Zumarraga\nd)Antonio de Mendoza\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Juan O Donoju\n\n", nP);
            system("pause");
            limpiar;
                    break;
        case 23:
            pf("%i.-Primer presidente de los Estados Unidos Mexicanos en 1824\n", nP);
            pf("a)Guadalupe Victoria\nb)Nicolas Bravo\nc)Vicente Guerrero\nd)Agustin de Iturbide\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) Guadalupe Victoria\n\n", nP);
            system("pause");
            limpiar;
                  break;
        case 24:
            pf("%i.Causa de la Guerra de Tres Anos o Guerra de Reforma\n", nP);
            pf("a)Muerte de Juarez\nb)Invasion francesa\nc)Venta de la Mesilla\nd)Constitucion de 1857\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) Constitucion de 1857\n\n", nP);
            system("pause");
            limpiar;
        break;
        }

    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;

}
int hist(int num[], int n)
{
    int i, aci=0, nP;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.- M%cximo representante del Materialismo Historico", nP,160);
            pf("\na)C. Collingwood\nb)Karl Marx\nc)Auguste Comte\nd)Leopoold Von  Ranke\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Karl Marx\n\n");
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.- El Enciclopedismo del siglo XVIII tuvo como finalidad", nP);
            pf("\na)concentrar el pensamiento religioso\nb)incluir el pensamiento filos%cfico\nc)concentrar todo el conocimiento de su tiempo\nd)referirse a los dogmas de la Iglesia\n",160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) concentrar todo el conocimiento de su epoca\n\n");
            system("pause");
            limpiar;
        break;
        case 3:
            pf("%i.- Movimiento obrero que planteaba al parlamento ingles los derechos de los trabajadores, su representatividad y participaci%cn pol%ctica\n", nP,162,161);
            pf("a)Ludismo\nb)Socialismo\nc)Cartismo\nd)Liberalismo\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Cartismo\n\n");
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.- Se le da el nombre de imperialismo al fen%cmeno de \n", nP,162);
            pf("a)expansi%cn del capitalismo ocurrido en el %cltimo tercio del siglo XIX\nb)conquista y colonizaci%cn europea del siglo XVI\nc)dominaci%cn se%corial en la Rusia zarista\nd)restauraci%cn de las monarqu%cas absolutas y la intolerancia religiosa\n",162,163,162,162,164,162,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) expansi%cn del capitalismo ocurrido en el %cltimo tercio del siglo XIX\n\n",162,163);
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.- Ordena cronol%cgicamente los siguientes acontecimientos de la primera guerra mundial\n", nP,162);
            pf("I. Formaci%cn de Alianzas\nII.Crisis de Julio\nIII.Guerra de posiciones\nIV.Guerra de trincheras\nV.Catorce puntos de paz del Presidente Wilson",162);
            pf(" \na)I,II,III,IV y V\nb)I,IV,V,III y II\nc)II,IV,V,III y I\nd)III,IV,V,I y III\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) I,II,III,IV y V\n\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-El colapso del orden econ%cmico internacional y del patr%cn oro, conocido como crisis del 29 inicio con la quiebra financiera de \n", nP,162,162);
            pf("a)Gran Bretana\nb)Estados Unidos de Am%crica\nc)Alemania\nd)Francia\n",130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Estados Unidos de America\n\n");
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.- Ordena cronol%cgicamente los siguientes acontecimientos relacionados con la Segunda Guerra Mundial \n", nP,162);
            pf("I.Hitler invade Polonia\nII.Desembarco angloamericano en Normand%ca\nIII.Bombas at%cmicas sobre Hiroshima y Nagasaki\nIV.Los alemanes toman Paris\nV.Ataque Japones a Pearl Harbor",161,162);
            pf("\na)I,IV,V,II y III\nb)II,V,I,III y IV \nc)III,I,IV,V y II\nd)IV,III,I,II y V\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) I,IV,V,II y III\n\n");
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-El primero de octubre de 1949 se proclam%c la Republica Pop%clar China en Nan king. Con ella\n", nP, 162,163);
            pf("I.designo al Partido Comunista Chino como el partido de Estado\nII.busc%c construir un modelo de econ%cmia autosuficiente\nIII.tuv%c como objetivo impulsar la reforma agraria, monetaria y la reeducaci%cn del pueblo\nIV.hicieron acuerdos de libre comercio mar%ctimo y comercial con los Estados Unidos de Am%crica\nV.impuls%c la reconstrucci%cn nacional, apoyada en la tecnolog%ca japonesa\n",162,162,162,162,161,130,162,162,162);
            pf("\na)I,III y IV\nb)I,II y V\nc)I,II y III\nd)II,IV y V\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) II,IV y V\n\n");
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Periodo de luchas pol%cticas, diplom%ctica, ideol%cgicas y de enfretamientos indirectos entre la Uni%cn de Republicas Sovi%cticas Socialistas y Estados Unidos de Am%crica\n", nP,161,160,162,162,130,130);
            pf("a)Luchas de liberaci%cn Nacional\nb)Guerra Fr%ca\nc)Era Neoliberal\nd)Neoimperialismo Nacionalista\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Guerra Fria\n\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Hecho que se consider%c como el inicio de los cambios pol%cticos a finales del siglo XX en la Europa del este\n", nP,162,161);
            pf("a)Paz armada\nb)Guerra Fr%ca\nc)Ca%cda del muro de Berl%cn\nd)Guerra de los Balcanes\n",161,161,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Caida del muro de Berlin\n\n");
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.- M%cximo representante del Positivismo\n", nP,160);
            pf("a)Auguste Comte\nb)Fernand Braudel\nc)C. Collingwood\nd)Leopold Von Ranke\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta a) Auguste Comte\n\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-El pensamiento ilustrado baso su visi%cn del mundo en\n", nP,162);
            pf("a)la escol%cstica\nb)el humanismo\nc)el liberalismo\nd)el racionalismo\n",160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) el racionalismo\n\n");
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Pa%cses que durante la segundad  mitad del siglo XIX practicaron un nacionalismo agresivo, autoritario y conservador, que difundieron el culto a los valores nacionales, el militarismo, la superioridad de la naci%cn y la inferioridad de otros pueblos\n", nP,161,162);
            pf("a)Inglaterra y Francia\nb)Rusia y Turqu%ca\nc)Alemania e Italia\nd)Alemania y Rusia\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c)Alemania e Italia\n\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Circunstancias econ%cmicas y pol%cticas que impulsaron a Alemania, Jap%cn y Estados Unidos como potencias internacionales al finalizar el siglo XIX\n", nP,162,161,162);
            pf("a)Surgir de imperios y colonias de Inglaterra,Francia y Rusia; tener un gobierno y una econom%ca dependientes\nb)Contar con un gobierno independiente, econom%ca s%clida y conservar su expansionismo militar\nc)Ser paises independientes con un gobierno aut%cnomo con una econom%ca basada en sus colonias\nd)la suspension del pago de la deuda externa\n",161,161,162,162,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Contar con un gobierno independiente, econom%ca solida y conservar su expansionismo militar\n\n",161);
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Una consecuencia de la primera guerra mundial fue la\n", nP);
            pf("a)creaci%cn de la Organizaci%cn de las Naciones Unidas\nb)formaci%cn de dos bloques: capitalista y socialista\nc)desintegraci%cn del Imperio austroh%cngaro\nd)integraci%cn del bloque sovi%ctico\n",162,162,162,162,163,162,130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) desintegraci%cn del Imperio austroh%cngaro\n\n",162,163);
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-Reg%cmenes militaristas de Europa en la primera mitad del siglo XX, que se caracterizaron por ser antisocialistas, anticristianos y antidemocr%cticos\n", nP,161,160);
            pf("a)Comunistas\nb)Despoticos\nc)Centralistas\nd)Totalitarios\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
             pf("Respuesta d) Totalitarios\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-Alianzas militares con fines defensivos que se  formaron como consecuencia de la rivalidad entre la Uni%cn de Republicas Sovi%cticas Socialistas y Estados Unidos de Am%crica durante la Guerra Fr%ca\n", nP,162,130,130,161);
            pf("a)La OTAN y la ONU\nb)La ONU y el Pacto de Varsovia\nc)El OMC y la OEA\nd)El Pacto de Varsovia y la OTAN\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) El OMC y la OEA\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Una caracter%cstica de la Guerra Fr%ca fue\n", nP,161,161);
            pf("a)desarrollar un conflicto entre dos pa%cses, sin repercusiones en otras regiones del mundo\nb)propiciar la carrera armamentista entre los Estados Unidos de Am%crica y la Uni%cn de Rep%cblicas Socialistas Sovi%cticas\nc)fomentar una econom%ca global con perspectiva capitalista\nd)legalizar el uso de armas nucleares en guerras posteriores a 1945\n",161,130,162,163,130,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) propiciar la carrera armamentista entre los Estados Unidos de Am%crica y la Uni%cn de Rep%cblicas Socialistas Sovieticas\n\n",130,162,163);
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Fen%cmeno econ%cmico que se manifiesta en una serie de tendencias recientes del desarrollo capitalista que acelera la integracion de las econom%cas nacionales\n", nP,162,162,161);
            pf("a)Alvaro Obregon\nb)Adolfo Lopez Mateos\nc)Manuel Avila Camacho\nd)L%czaro C%crdenas\n",160,160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta d) L%czaro C%crdenas\n\n",160,160);
            system("pause");
            limpiar;
        break;
        case 20:
              pf("%i.-Un crecimiento econom%cco sostenido de m%cs del 6%% anual y la construcci%cn de infraestructura fueron hechos que, entre 1952 y 1970, se conocier%cn como\n", nP,161,160,162,162);
            pf("a)Neocapitalismo\nb)Socialismo\nc)Globalizaci%cn\nd)Nacionalismo\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) Globalizaci%cn\n\n", 162);
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-La lucha de clases, el Manifiesto del Partido Comunista y la distribuci%cn de los bines corresponder a\n", nP,162);
            pf("a)Ludismo\nb)socialismo ut%cpico\nc)socialismo cient%cfico\nd)movimiento cartista\n",162,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) socialismo cient%cfico\n\n", 161);
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Causa externa de la independencia de Hispanoam%crica\n", nP,130);
            pf("a)la divisi%cn social\nb)las Reformas Borb%cnicas\nc)el nacionalismo criollo\nd)el monopolio\n",162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) las Reformas Borb%cnicas\n\n", 162);
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-La ilustraci%cn en el %cmbito pol%ctico se opon%ca al\n", nP,162,160,161,161);
            pf("a)Imperialismo\nb)Absolutismo\nc)Socialismo\nd)Humanismo\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta b) Absolutismo\n\n", nP);
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.Menciona las causas que originaron la Segunda Revoluci%cn Industrial\n", nP,162);
            pf("a)uso del vapor y del carb%cn mineral  \nb)desempleo y la crisis demogr%cfica\nc)aprovechamiento del petr%cleo  y la electricidad\nd)aumento de la poblaci%cn\n",162,160,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta c) aprovechamiento del petr%cleo y la electricidad\n\n", nP,162);
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Aciertos:%i\n", aci);
    system("pause");
    return aci;
}
int fis(int num[], int n)
{
    int i, aci=0, nP;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Unidad de longitud del sistema m%ctrico decimal que es utilizada internacionalmente por los cient%cficos:\n", nP, 130, 161);
            pf("a)Decilitro\nb)Yarda\nc)Libra\nd)Metro\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Metro\n");
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.-Es la cantidad de energ%ca que tiende a mover a los cuerpos o a cambiarles su direcci%cn:\n", nP, 161, 162);
            pf("a)Masa\nb)Movimiento\nc)Fuerza\nd)Peso\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Fuerza\n");
            system("pause");
            limpiar;
        break;
        case 3:
            pf("%i.-Relaciona las columnas:\n\n", nP);
            pf("1. Linea sobre la cual actua una fuerza\n2. Lugar en el que act%ca la fuerza\n3. Indica hacia donde se dirige la fuerza\n4. Magnitud de la fuerza\n\n", 163);
            pf("I) Intensidad\nII)Direcci%cn\nIII)Punto de Aplicaci%cn\nIV)Sentido\n\n", 162, 162);
            pf("a)1,I/2,III/3,II/4,IV\nb)1,II/2,III/3,IV/4,I\nc)1,II/2,I/3,IV/4,III\nd)1,II/2,III/3,II/4,IV\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)1,II/2,III/3,IV/4,I\n");
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-A la velocidad considerada en un tiempo muy corto se le llama:\n", nP);
            pf("a)Velocidad Media\nb)Velocidad Tangencial\nc)Velocidad Angular\nd)Velocidad Instant%cnea\n", 160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Velocidad Instant%cnea\n", 160);
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.-Es la fuerza que sujeta al cuerpo cuando gira y lo mantiene en su trayectoria:\n\n", nP);
            pf("a)Fuerza Total\nb)Fuerza Centr%cfuga\nc)Fuerza Centr%cpeta\nd)Movimiento Circular Uniforme\n", 161, 161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Fuerza Centr%cfuga\n", 161);
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-Son discos resistentes y acanalados que pasan por una cuerda que les permite girar alrededor de un eje (Pueden ser de tipo fijo o m%cvil):\n\n", nP, 162);
            pf("a)Planos Inclinados\nb)Palancas inter-potentes\nc)Poleas\nd)Ninguna de las anteriores\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='C' || opc=='c')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Poleas\n");
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-La explicaci%cn del porqu%c los cuerpos flotan dentro de un l%cquido se conoce como Principio de:\n\n", nP, 162, 130, 161);
            pf("a)Arqu%cmedes\nb)Newton\nc)Avogadro\nd)Pascal\n", 161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Arqu%cmedes\n", 161);
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-A la cantidad de calor que absorbe un gramo de agua en estado l%cquido para aumentar su temperatura en un grado cent%cgrado, se le llama:\n\n", nP, 161, 161);
            pf("a)Volt\nb)Calor%ca\nc)Watt\nd)Joule\n", 161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Calor%ca\n", 161);
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Cuando la energ%ca cambia de una forma a otra, siempre se conserva. Esto corresponde a la:\n\n", nP, 161);
            pf("a)Ley de Coulomb\nb)Ley de Avogadro\nc)Ley de la Conservaci%cn de la energ%ca\nd)Ley de la Conservaci%cn de la Materia\n", 162, 161, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Ley de la Conservaci%cn de la Energ%ca\n", 162, 161);
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-LUX y FOT son unidades de:\n\n", nP);
            pf("a)Fuerza\nb)Temperatura\nc)Iluminaci%cn\nd)Sonido\n", 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Iluminac%cn\n", 162);
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-Es el resultado de la mezcla de los siete colores que tiene el arco-iris:\n\n", nP);
            pf("a)Luz Blanca\nb)Color de la Luz\nc)Espectro Crom%ctico\nd)Polarizaci%cn de la Luz\n", 160, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Luz Blanca\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Es el espacio que ocupa un cuerpo:\n\n", nP);
            pf("a)Superficie\nb)Peso\nc)Tamanio\nd)Volumen\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Volumen\n");
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Propiedad de los cuerpos para cambiar su forma cuando son afectados por las fuerzas y recobrarla cuando cesan:\n\n", nP);
            pf("a)Volumen\nb)Forma\nc)Elasticidad\nd)Masa\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Elasticidad\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Cuando colgamos una pinata en una cuerda, estamos aplicando una serie de fuerzas:\n\n", nP);
            pf("a)Paralelas con el mismo sentido\nb)Paralelas con sentido contrario\nc)Colineales\nd)Angulares\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Angulares\n");
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Es el aumento o disminuci%cn de la velocidad en la unidad de tiempo.\n\n", nP, 162);
            pf("a)Fuerza\nb)Equilibrio\nc)Aceleraci%cn\nd)Movimiento\n", 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Aceleraci%cn\n", 162);
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-Sencillos dispositivos que usa el hombre para facilitar su trabajo y optimizar la energ%ca que usa:\n\n", nP, 161);
            pf("a)Medidas\nb)Animales de carga\nc)Maquinas simples\nd)Computadoras\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Maquinas Simples\n");
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-A la energ%ca que tienen los cuerpos en movimiento se le llama:\n\n", nP, 161);
            pf("a)Potencial\nb)Cin%ctica\nc)MACH\nd)Kilowatt-hora\n", 130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Cin%ctica\n", 130);
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Por este fen%cmeno se puede explicar la formaci%cn de las burbujas de jab%cn:\n\n", nP, 162, 162, 162);
            pf("a)Tensi%cn superficial\nb)Adhesi%cn\nc)Cohesi%cn\nd)Elasticidad\n", 162, 162, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Tensi%cn Superficial\n", 162);
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Al paso del estado s%clido al gaseoso, sin pasar por el estado l%cquido, se le llama:\n\n", nP, 162, 161);
            pf("a)Congelaci%cn\nb)Fusi%cn\nc)Evaporaci%cn\nd)Sublimaci%cn\n", 162, 162, 162, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Sublimaci%cn\n", 162);
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-En la representaci%cn gr%cfica de un sonido, a la distancia entre dos crestas y dos valles consecutivos se le llama:\n\n", nP, 162, 160);
            pf("a)Amplitud de onda\nb)Longitud de onda\nc)Periodo\nd)Frecuencia\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Longitud de onda\n");
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-En %cptica, el %cngulo de incidencia es igual al %cngulo de reflexi%cn:\n\n", nP, 162, 160, 160, 162);
            pf("a)Primera ley de la reflexi%cn de la luz\nb)Segunda ley de la reflexi%cn de la luz\nc)Tercera ley de la reflexi%cn de la luz\nd)Ley de Gay-Lussac\n", 162, 162, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Primera ley de la reflexi%cn de la luz\n", 162);
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Inducci%cn, contacto y frotamiento son formas de:\n\n", nP, 162);
            pf("a)Iluminaci%cn\nb)Filtraci%cn\nc)Atracci%cn\nd)Electrizaci%cn\n", 162, 162, 162, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Electrizaci%n\n", 162);
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-Los adornos de luces de los arboles de navidad son ejemplo de este tipo de conexiones:\n\n", nP);
            pf("a)Resistencia f%csica\nb)Conexi%cn en serie\nc)Conexi%cn en paralelo\nd)Conexi%cn mixta\n", 161, 162, 162, 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Conexi%cn en serie\n", 162);
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-""Un cuerpo no puede modificar por s%c mismo su estado de reposo o movimiento"", este postulado corresponde a:\n\n", nP, 161);
            pf("a)Segunda ley de Newton\nb)Principio de la conservaci%cn de la materia\nc)Tercera ley de Newton\nd)Primera ley de Newton\n", 162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Primera ley de Newton\n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int formacion(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Los integrantes de una sociedad para mantener una convivencia pac%cfica y estable,\n requieren de _________ morales que regulen la _________ en beneficio de la comunidad.\n",nP,161);
            pf("a) juicios- conducta\nb) leyes - conciencia \nc) prohibiciones - vida\nd) h%cbitos - ciencia \n",160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) jucios- conducta \n");
            system("pause");
            limpiar;

        break;
        case 2:
            pf("%i.-%cEn cu%cl de los siguentes casos s%clo al interesado le compete tomar la decisi%cn?\n",nP,168,160,162,162);
            pf("a) Determinar en d%cnde realizar el servicio militar.\nb) Decretar las leyes fiscales para el pa%cs.\nc) Elegir la pareja con la cual contraer%c.\nd) Disponer el castigo por pasarse un alto.\n",162,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) Elegir la pareja con la cual contraer%c.\n",160);
            system("pause");
            limpiar;

        break;
        case 3:
            pf("%i.-De los siguientes enunciados,%ccu%cl expresa una valoraci%cn est%ctica?.\n",nP,168,160,162,130);
            pf("a) Me encant%c la armon%ca,el equilibrio y la proporci%cn con que estaban dise%cados los vestidos en esa tienda de modas.\n",162,161,162,164);
            pf("b) Considero que la lucha por los derechos humanos es justa y el valor universal, sin presencia de tintes pol%cticos.\n",161);
            pf("c) Me parece que no debemos perder de vista la empat%ca y la comprensi%cn que nos debemos unos a otros.\n",161,162);
            pf("d) No creo que Juan haga bien al mentir tanto a su esposa respecto del sueldo que gana, ella trabajaba desmasiado.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) Me encant%c la armon%ca,el equilibrio y la proporci%cn con que estaban dise%cados los vestidos en esa tienda de modas. \n",162,161,162,164);
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-Pablo y Laura le piedieron a su abuela que les mostrara sus %clbumes fotogr%cficos, les contara el contexto y las an%ccdotas.\n",nP,160,160,130);
            pf("Apartir de entonces, descubrieron que las _________ han intervenido en la conformaci%cn de su identidad personal.\n",162);
            pf("a) leyes sociales.\nb) ambiciones infantiles.\nc) historias compartidas.\nd) pol%cticas p%cblicas.\n",161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) historias compartidas.\n");
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.-De los siguientes enunciados, identifica cu%Cles se refieren a los derechos y cu%cles a Las obligaciones de los adolescentes:\n",nP,160,160);
            pf("I. Derechos.\nII. Obligaci%cn\n",162);
            pf("A.Respeto de los padres a los hijos.\nB.Responsabilidad en los estudios.\nC.Cumplimiento de las normas sociales.\nD.Contar con servicios de salud gratuitos.\n");
            pf("a) I: A, D - II: B, C.\nb) I: A, B - II: C, D.\nc) I: B, C - II: A, D.\nd) I: C, D - II: B, A.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) I: a, d - II: b, c\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-El due%co de un establecimiento paga a sus empleados adolecentes un sueldo m%cnimo argumentando que no tienen necesidades importantes que satisfacer,\n como en el caso de los adultos casados. Esta situaci%cn describe un tipo de:\n",nP,164,161,162);
            pf("a) favoritismo econ%cmico empresarial.\nb) violencia econ%cnomica a los adolecentes.\nc)peque%Cas y medianas empresas.\nd) econom%ia propia de la adolecencia.\n",162,162,164,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) violencia econ%cnomica a los adolecentes.\n",162);
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-En una democracia, el m%ctodo que permite resolver las diferencias, en la toma de decisiones,se funtamenta en el principio de\n",nP,130);
            pf("a) igualdad\nb) mayor%ca\nc) utilidad\nd) equidad\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) mayor%ca\n",161);
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-Reto democr%ctico que permite manifestar el reconocimiento de la pluralidad ideol%cgica y pol%ctica de la sociedad.\n",nP,160,162,161);
            pf("a) Participaci%cn ciudadana.\nb) Tranparencia p%cblica.\nc) Acceso a la informaci%cn\nd) Responsabilidad p%cblica.\n",162,163,162,163);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) Participaci%cn ciudadana.\n",162);
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Ejemplo de la soberan%ca popular mediante la participacic%cn cuidadana \n",nP,161,162);
            pf("a) Contribuir en la quema de urnas en las votaciones locales.\nb) Designaci%cn de diputados por el Presidente de la Rep%cblica Mexicana.\nc) Convivir co los vecinos en las fiestas religiosas del pueblo.\nd) Colaborar activamente y concretamente en beneficio de la colectividad.\n",162,163);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) Colaborar activamente y concretamente en beneficio de la colectividad.\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Un medio de comunicaci%cn cumple con una funci%cn social cuando\n",nP,162,162);
            pf("a) organiza y concentra la ayuda para damnificados por desastres naturales.\nb) est%c involucrado en el servicio al sistema econ%cmico y la publicidad. \nc) derrumba mitos al influir y formar opiniones mediante la manipulaci%cn.\nd) convence al receptor sore un tema espec%cfico mediante la persuaci%cn.\n",160,162,162,161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) convence al receptor sore un tema espec%cfico mediante la persuaci%cn.\n"),161,162;
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-El ciudadadano K obtuvo casa,autos,joyas, sirvientes,etc%ctera, mediante la sobreexplotaci%cn ilegal de los recursos \n naturales de su comunidad. Al actuaras%c logr%c su fortuna\n",nP,130,162,161,162);
            pf("a) ejercienbdo sus derechos. \nb) ignoranmdo sus derechos.\nc) ignorando sus obligaciones.\nd) ejerciendo su responsabilidad.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) ignorando sus obligaciones.\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Es la manera racional de resolver un conflicto, es decir, se evita la fuerza f%csica, moral o militar.\n",nP,161);
            pf("a) Segregaci%cn. \nb) Negociaci%cn. \nc) Confrontaci%cn.\nb) Exclusi%cn.\n",162,162,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) Negociaci%cn.\n",162);
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-La ________ es comprender al otro, ponerse en su lugar y respetarlo.\n",nP);
            pf("a) Amistad.\nb) Moralidad.\nc) Empat%ca\nd) Soliralidad.\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) Empat%ca\n",161);
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Tipo de normas para vida diaria, aceptadas y promovidas por la comunidad.\n",nP);
            pf("a) Jur%cdicas\nb) Morales\nc) Sanciones\nd) Decretos\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) Morales\n");
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Son derechos del desarrolo integral durante la adolecencia:\n",nP);
            pf("I. Educaci%cn\nII. Deportes\nIII.Alimentaci%cn\nIV. Lectura\nV. Salud\n",162,162);
            pf("a) I, II, III\nb) I, III, IV \nc) I, II, IV\nd) I, III, V\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) I, III, V\n");
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.Tipo de violencia que ocurre cuando una persona ejerce acciones sobre la sexualidad de una u otras personas, en contra de su voluntad:\n",nP);
            pf("a) Sexual\nb) Verbal\nc) F%csica\nd) Psicol%cgica\n",161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) Sexual\n");
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-Cuando un adolecente presenta maltrato psicol%cgico sufre de...\n",nP,162);
            pf("I. Intimidaci%cn\nII. Lesiones\nIII. Golpes\nIV. Gritos\nV. Insultos\n",162);
            pf("a) I, IV, V\nb) I, II, V\nc) II, III, IV\nd) II, III, V\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) I,IV,V\n");
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-La emisi%cn del voto en las elecciones es una forma de partcipaci%cn  _________.\n",nP,162,162);
            printf("a) dictatorial\nb) parlamentaria\nc) democr%ctica\nd) real\n",160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) democr%ctica\n",160);
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Relaciona el concepto con su definici%cn\n",nP,162);
            pf("I. Territorio\nII.Poblaci%cn\nIII.Gobierno\n",162);
            pf("A. Conjunto de habitantes que forman la unidad social.\nB. Orden pol%ctico que representa a los interese de la cuidadan%ca.\nC. Espacio f%csico que contiene los recursos y bienes de una naci%cn.\n",161,161,161,162);
            pf("a) I A, II C, III B\nb) I C, II B, III A\nc) I C, II A, III B \nd) I B, II C, III A\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c)  I C, II A, III B \n");
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-Caracter%csticas de la conciencia moral individual:\n",nP,161);
            printf("a) Obedecer para obtener beneficios en la sociedad.\nb) Obedecer a las autoridades por temor al castigo.\nc) Responder por nuestros actos ante los dem%cs.\nd) Obedecer por quedar bien con los dem%cs.\n",160,160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) Responder por nuestros actos ante los dem%cs. \n",160);
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-%cDe qu%c habla el art%cculo 3 de la Contituci%cn Pol%ctica de los Estados Unidos Mexicanos? \n",nP,168,130,161,162,161);
            printf("a) Libertad de manifestarse.\nb) Derecho a ser juzgado por la ley.\nc) Derecho a la educaci%cn\nd) Todos los cuidadanos son iguales ante la ley\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) Derecho a la educaci%cn.\n",162);
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Es un medio para evitar la violencia, en que se exponen la postura e intereses de los individuos:\n",nP);
            printf("a) Agresi%cn\nb) Empat%ca\nc) Di%clogo\nd) Insultos\n",162,161,160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) Di%clogo\n",160);
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-%cDe qu%c habla el art%cculo 1 de la Contituci%cn Pol%ctica de los Estados Unidos Mexicanos? \n",nP,168,130,161,162,161);
            printf("a) Libertad de manifestarse.\nb) Derecho a ser juzgado por la ley.\nc) Derecho a la educaci%cn\nd) Todos los cuidadanos son iguales ante la ley\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) Todos los cuidadanos son iguales ante la ley\n");
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-Relaciona los poderes del Estado Mexicano con su definici%cn correcta\n",nP,162);
            pf("I. Ejecutivo\nII. Legislativo \nIII. Judicial\n");
            pf("A. Propone, analiza, promulga,aprueba y deroga leyes.\nB. Aplica la justicia atrav%cs de la Suprema Corte.\nC. Publica y aplica leyes\n",160);
            pf("a) I A, II B, III C \nb) I C, II A, III B\nc) I A, II C, III B\nd) I C, II B, III A\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) I C, II A, III B \n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int habM(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Si se construye una pir%cmide de cuatro lados utilizando pelotas de ping-pong\n",nP,160);
            pf("Cu%cntas pelotas de ping-pong se necesitan para que la pir%cmide tenga siete niveles?\n",160,160);
            pf("a)120 pelotas\nb)80 pelotas\nc)100 pelotas\nd)140 pelotas\n",168);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)140 pelotas\n");
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.-En un concurso para adivinar el n%cmero de chicles en un frasco\n",nP,163);
            pf("Alicia dijo que hab%ca 31, Carolina dijo que hab%ca 23, Diana dijo que hab%ca 25 y Jimena dijo que hab%ca 27.\n",161,161,161,161);
            pf("Una de ellas adivino el n%cmero exacto de chicles; dos de ellas se equivocaron por una diferencia de 2 chicles; y la otra se equivoc%c por una diferencia de 4 chicles.\n)",163,162);
            pf("Cu%cntos chicles hab%ca en el frasco, y quien adivino el n%cmero exacto?\n",160,161,163);
            pf("a)31. Alicia\nb)23, Carolina\nc)27, Jimena\nd)25, Diana\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)27, Jimena\n");
            system("pause");
            limpiar;
        break;
        case 3:
            pf("%i.-Tres viajeros se detienen en un restaurante a cenar. El %cnico platillo que hay disponible es un plato con papas cocidas.\n",nP,163);
            pf("Al ser servido el plato, el primer viajero se comi%c una tercera parte del total de las papas que hab%ca en el plato;\n",162,161);
            pf("el segundo viajero se comi%c una tercera parte de lo que sobro despu%cs de que el primer viajero comi%c;\n",162,130,162);
            pf("y el %cltimo viajero se comi%c una tercera parte de lo que quedaba en el plato una vez que el segundo viajero hab%ca terminado de comer.\n",163,162,161);
            pf("Al terminar los tres viajeros de comer, sobraban en el plato 8 papas cocidas.\n");
            pf("Cu%cntas papas hab%ca en el plato en el momento que fue servido?\n",160,161);
            pf("a)21 papas\nb)27 papas\nc)34 papas\nd)18 papas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)27 papas\n");
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-En un corral hay cierto n%cmero de vacas. La diferencia entre el total de patas que se pueden contar en el corral y el total de orejas es de 40.\n",nP,163);
            pf("Cu%cntas vacas hay en el corral?\n",160);
            pf("a)20 vacas\nb)15 vacas\nc)35 vacas\nd)25 vacas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)20 vacas\n");
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.-Si hay 6 personas en una fiesta y cada uno le estrecha la mano en se%cal de saludo al resto de los invitados\n",nP,164);
            pf("Cu%cntas veces se estrecharon manos en total entre todos los invitados?\n",160);
            pf("a)12 veces\nb)6 veces\nc)36 veces\nd)15 veces\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)15 veces\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-En la siguiente serie Qu%c valor no es correcto?: 85,76,66,58,49,x\n",nP,130);
            pf("a)85\nb)66\nc)76\nd)58\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)66\n");
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-Cu%cl es el valor de M y de N en la serie: 11,9,13,11,15,13,17,15,M,17,21,N?\n",nP,160);
            pf("a)15 y 19\nb)19 y 23\nc)21 y 23\nd)19 y 19\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)19 y 19\n");
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-Si un elefante pesa 1000 kilogramos m%cs dos terceras partes de su propio peso.\n",nP,160);
            pf("Cu%cnto pesara en total el elefante?\n",160);
            pf("a)3000kg\nb)2000kg\nc)1666kg\nd)1500kg\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)3000kg\n");
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-El elefante pesa una quinta parte de su peso total m%cs el peso de un hipop%ctamo, que a su vez pesa 800 kg menos que el elefante\n",nP,160,162);
            pf("Cu%cl es el peso total del elefante?\n",160);
            pf("a)3000kg\nb)4000kg\nc)2500kg\nd)2000kg\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)4000kg\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-El costo de un litro de agua con todo y su envase es de 10 pesos. El litro del l%cquido cuesta 4 pesos m%cs que el envase\n",nP,161,160);
            pf("Cu%cl es el precio del l%cquido sin el envase?\n",160,161);
            pf("a)7 pesos\nb)6 pesos\nc)8 pesos\nd)4 pesos\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)7 pesos\n");
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-Un coronel del ej%crcito quiere saber cu%cntos soldados y cu%cntos caballos tiene bajo su comando.\n",nP,130,160,160);
            pf("Si cuenta 45 cabezas y 120 piernas, entre soldados y caballos;\n");
            pf("Cu%cntos caballos tiene bajo su comando?\n",160);
            pf("a)20 caballos\nb)18 caballos\nc)15 caballos\nd)25 caballos\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)15 caballos\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Un tren sale de San Juan en direcci%cn a San Pedro a una velocidad de 30km/h.\n",nP,162);
            pf("En el mismo instante otro tren sale de San Pedro en direcci%cn a San Juan a una velocidad de 28km/h.\n",162);
            pf("A qu%c distancia se encuentra San Juan de San Pedro, si los trenes se cruzan exactamente una hora despu%cs de haber salido de sus respectivas ciudades?\n",130,130);
            pf("a)30 km\nb)58 km\nc)28 km\nd)56 km\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)58 km\n");
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Una jaula tiene espacio para albergar a 120 perros o a 144 gatos. Si hay 90 perros en la jaula,\n",nP);
            pf("Cu%cntos gatos podr%can aun caber en ella?\n",160,161);
            pf("a)40 gatos\nb)32 gatos\nc)36 gatos\nd)42 gatos\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)36 gatos\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Un viejo mago de la edad media es 3 veces mayor que su hijo;\n",nP);
            pf("el padre del mago es 40 a%cos mayor que el doble de la edad del propio mago;\n",164);
            pf("y la suma de las edades del padre, el mago, y el hijo del mago es de 1240 a%cos.\n",164);
            pf("Cu%cl es la edad del mago?\n",160);
            pf("a)270 a%cos\nb)360 a%cos\nc)250 a%cos\nd)420 a%cos\n",164,164,164,164);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)360 anios\n", 164);
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Para hornear un pavo por cada 1/2 kg se requieren 3/4 de hora a fuego.\n",nP);
            pf("Durante cu%cnto tiempo se debe hornear un pavo de 5 kg?\n",160);
            pf("a)7 horas.\nb)6 horas 30 min.\nc)7 horas 15 min.\nd)7 horas 30 min.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)7 horas 30 min.\n");
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-Una empresa de investigaci%cn privada aplico una encuesta a 200 familias, de las cuales:",nP,162);
            pf("32 dijeron tener un hijo; 55 dos hijos; 58 tres hijos; 25 cuatro hijos; y 30 cinco o m%cs hijos.\n",160);
            pf("Cu%cl es la probabilidad de que una familia escogida de la encuesta al azar tenga a lo m%cs tres hijos?\n",160,160);
            pf("a)72.5 porciento\nb)27.5 porciento\nc)45 porciento\nd)43.5 porciento\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)72.5 porciento\n");
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-A Daniel, David y Dar%co les dieron 360 canicas; a Dar%co le toco 1/4 y a David 1/3,",nP,161,161);
            pf("por lo tanto a Daniel le tocaron:\n");
            pf("a)150\nb)120\nc)200\nd)220\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)150\n");
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Hab%ca $300. Fernando se qued%c con $55, Alejandro con el triple de Fernando y Daniel con el resto.\n",nP,161,162);
            pf("Con cu%cnto se qued%c Daniel?\n",160,162);
            pf("a)$35\nb)$105\nc)$80\nd)$90\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)$80\n");
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-La suma de las edades de Rosario y %cngeles es 50 a%cos. Si Rosario es 6 a%cos mayor que %cngeles,\n",nP,181,164,164,181);
            pf("Qu%c edad tiene %cngeles?\n",130,181);
            pf("a)28\nb)18\nc)22\nd)26\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)26\n");
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-Ra%cl cumplir%c 16 a%cos dentro de 7 meses.\n",nP,163,160,164);
            pf("Cu%cntos meses le faltan para cumplir dieciocho a%cos y medio?\n",160,164);
            pf("a)35\nb)37\nc)24\nd)31\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)37\n");
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-La suma de 2 n%cmeros es 12 y su diferencia es 6; dichos n%cmeros son:\n",nP,163,163);
            pf("a)9, 3\nb)8, 4\nc)10, 2\nd)11, 1\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)9, 3\n");
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Si el %crea de un cuadrado es 121 m2 Cu%cl es su per%cmetro?\n",nP,160,160,161);
            pf("a)11 m\nb)44 m\nc)22 m\nd)121 m\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)44 m\n");
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-Miguel es 8 a%cos mayor que Dar%co y Martin es 2 a%cos menor que Miguel.\n",nP,164,161,164);
            pf("Cu%cntos a%cos es mayor Martin que Dar%co?\n",160,164,161);
            pf("a)4\nb)10\nc)16\nd)6\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)6\n");
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-En un corral hay 76 patas y 25 cabezas,\n",nP);
            pf("Cu%cntos conejos y cu%cntos gallos hay?\n",160,160);
            pf("a)13 conejos y 12 gallos\nb)22 conejos y 13 gallos\nc)30 conejos y 15 gallos\nd)35 conejos y 10 gallos\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)13 conejos y 12 gallos\n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int quim(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Partic%cla m%cs peque%ca de un elemento y que entra a formar parte de una reacci%cn quimica\n",nP,163,160,164,162);
            pf("a)At%cmo\nb)Mol%ccula\nc)Electr%cn\nd)Acido\n",162,130,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) At%cmo\n",162);
            system("pause");
            limpiar;

        break;
        case 2:
            pf("%i.-El n%cmero de orbitas en las que circulan los electrones y se designan a partir del n%ccleo\n",nP,163,163);
            pf("a)10\nb)5\nc)7\nd)11\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) 11\n");
            system("pause");
            limpiar;

        break;
        case 3:
            pf("%i.-Compuesto formado por un metal con hidrogeno.\n",nP);
            pf("a)Hidruros \nb)Sales Acidas \nc)Oxisales\nd)ADN\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) Hidruros\n");
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-Al reaccionar una base y un acido se forma una sal, a este enlace se le llama:\n",nP);
            pf("a)Redox\nb)Cristalizaci%cn\nc)Neutralizaci%cn\nd)Sedimentaci%cn\n",162,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) Sedimentaci%cn\n",162);
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.-Relaciona los compuestos:\n1-Oxisales\n2-Hidracidos.\n3-Sales Acidas\n4-Sales sencillas\n5-Oxidos b%csicos\n",nP,160);
            pf("\nI)Se forman con oaxisales, con radicales (OH)\nII) Sales formadas por un metal y un no-metal.\nIII) Sales formadas por un metal, un no-metal y ox%cgeno",161);
            pf("IV) Formados por hidrogeno y un no-metal.\nV)Formado por un metal y ox%cgeno que al reaccionar con agua forman hidr%cxidos",161,162);
            pf("\n\na) (1 II),(2 III),(3 I),(4 V),(5 IV)\nb)(1 IV),(2 I),(3 II),(4 V),(5 III)");
            pf("\nc)(1 III),(2 IV),(3 I),(4 V),(5 IV)\nd) (1 III),(2 IV),(3 I),(4 II),(5 V)\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) (1 III),(2 IV),(3 I),(4 II),(5 V)\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-Es la fuerza de separaci%cn de la mol%cculas.\n",nP,162,163);
            pf("a)Decantaci%cn\nb)Repulsi%cn\nc)Atracci%cn\nd)Separaci%cn\n",162,162,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b) Respulsi%cn\n",162);
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-Para nombrar un compuesto formado por un metal y un no-metal, se menciona primero el elemento no-met%clico usando la terminaci%cn:\n",nP,160,162);
            pf("a)oso\nb)ico\nc)uro\nd)iro\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c) uro\n");
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-Completa la siguiente frase; Los ____ tienen carga ____ y se ubican dentro del n%ccleo del atomo.\n",nP,163);
            pf("a)Electrones-positiva\nb)neutrones-positiva\nc)At%cmos-Positivos\nd) Electrones-Negativa\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d) Electrones-Negativa\n");
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Esta teor%ca afirma que; \"las sustancias est%cn formadas por at%cmos y los at%cmos de cada elemento tienen peso y tama%co parecidos\"\n",nP,161,160,162,162,164);
            pf("a)Ley de Dalton\nb)Principio de Incertidumbre de Heisenberg\nc)Ley de Rutherford\nd)Leyes ponderales\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a) Ley de Dalton\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Propiedades que permiten identificar sustancias\n",nP);
            pf("a)Volumen, porosidad y viscosidad\nb)Temperatura de ebullici%cn, solubilidad y densidad\nc)Masa, peso y permeabilidad\nd)presi%cn manom%ctrica\n",162,162,130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b)Temperatura de ebullici%cn, solubilidad y densidad\n",162);
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-En la siguiente ecuaci%cn qu%cmica cuales son los reactivos?\n",nP,162,161);
            pf("\n NaOH + HNO3 ---> NANO3 + H2O\n\n");
            pf("a)NaOH y HNO3\nb)NANO3 y H2O\nc)NANO3 y NAOH\nd)NHH y JKL\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a)NaOH y HNO3\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Son %cnicamente elementos d%cctiles y maleables, capaces de conducir el calor y la electricidad\n",nP,163,163);
            pf("a)Al,Fe,S,I\nb)Li,Fe,Al,Cu\nc)Sn,C,Cu,Fe\nd)Fe,Ge,Au\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b)Li,Fe,Al,Cu\n");
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Propiedades f%csicas de los gases:\n",nP,161);
            pf("a)Difusibilidad y volumen propio\nb)volumen definido y maleabilidad\nc)Volumen y forma definida\nd)Forma indefinida y maleabilidad\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c)Volumen y forma definida\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Propiedades que permiten identificar sustancias:\n",nP);
            pf("a)Volumen, porosidad y viscosidad\nb)Temperatura de fusi%cn, volumen y solubilidad\nc)Peso, masa e impermeabilidad\nd)Temperatura de ebullisi%cn, solubilidad y densidad\n",162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d)Temperatura de ebullisi%cn, solubilidad y densidad\n",162);
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-El alcohol presente en una muestra de vino puede separarse mediante:\n",nP);
            pf("a)Destilacion\nb)Sublimacion\nc)Decantacion\nd)Temperatura de ebullision, solubilidad y densidad\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d)Temperatura de ebullision, solubilidad y densidad\n");
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-En la formula del H2O existen:\n",nP);
            pf("a)Dos mol%cculas de agua\nb)dos at%cmos de hidrogeno y uno de ox%cgeno\nc) Dos at%cmos de ox%cgenos y uno de hidrogeno\nd)Temperatura de ebullisi%cn, solubilidad y densidad\n",130,162,161,162,161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b)dos at%cmos de hidrogeno y uno de ox%cgeno\n",162,161);
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-En un enlace covalente existe una ______ de electrones:\n",nP);
            pf("a)Ganancia\nb)Perdida\nc) Compartici%cn\nd)Transferencia\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta es: c)Compartici%cn\n",162);
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-De los siguientes elemenetos cuales son gases?\n",nP);
            printf("a)H,O\nb)C,Cl\nc)Be,C\nd)Xe,N\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a)H,O\n");
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Son procesos de oxido reducci%cn\n",nP,162);
            pf("a)Evaporaci%cn del agua\nb)Corroci%cn de un clavo\nc) Romper un vidrio\nd)Empaniamiento de la plata\n",162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b)Corroci%cn de un clavo\n",162);
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-Al mezclar agua con az%ccar se forma\n",nP,163);
            pf("a)Una reacci%cn\nb)Una combusti%cn\nc)Una suspenci%cn\nd) Una soluci%cn\n",162,162,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a)Una reacci%cn\n",162);
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-La qu%cmica es la ciencia que:\n",nP,161);
            printf("a)Estudia la tierra\nb)Analiza el comportamiento de los seres vivos\nc)Estudia fen%cmenos el%cctricos\nd)Estudia la materia, la energ%ca y sus cambios\n",162,130,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta es: d)Estudia la materia, la energ%ca y sus cambios.\n",161);
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-C%cal de las siguientes mezclas es hetereog%cnea?\n",nP,163,130);
            pf("\na)Mayonesa\nb)Refresco\nc)Agua de mar\nd)Disoluci%cn de sal\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a)Mayonesa\n");
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-De las siguientes sutancias corresponde a un %ccido\n",nP,160);
            pf("a)Nacl\nb)HCl\nc)H2O\nd)FeBC\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta es: b)HCL\n");
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-El cloro tiene n%cmero at%cmico 17, ¿Cu%cntos electrones contiene?\n",nP,163,162,160);
            printf("a)17\nb)18\nc)20\nd)8.5\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta es: a)17\n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Aciertos:%i\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int bio(int num[], int n)
{
   int i, aci=0, nP;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Un ejemplo de mucopolisac%crido (glucosaminoglucano) de importancia biol%cgica es:\n", nP,160,162);
            pf("a)Gluc%cgeno\nb)Celulosa\nc)Heparina\nd)Plasmalogen%c\n",162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Heparina\n");
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.-Cual aseveraci%cn respecto a la estructura del gluc%cgeno es correcta\n", nP,162,162);
            pf("a)Hay enlace B 1,2\nb)Hay enlace a 1,2\nc)Es una mol%ccula no ramificada\nd)Se ramifica cada 6 glucosas\n",130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Se ramifica cada 6 glucosas\n");
            system("pause");
            limpiar;
        break;
        case 3:
            pf("%i.-%ccido graso que sirve de precursor para la s%cntesis de prostaglandinas\n", nP,181,161);
            pf("a)Palmitoleico\nb)Oleico\nc)Araquimico\nd)Araquid%cmico\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Araquid%cnico\n",162);
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-La unidad estructural b%csica repetitiva de la cromatina de los cromosomas eucari%cticos es: \n", nP,160,162);
            pf("a)El proteosoma\nb)El centrosoma\nc)El nucleosoma\nd)EL genoma\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Nucleosoma\n");
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.- La formaci%cn de un enlace disulfuro entre cadenas polipept%cdicas es un ejemplo de estructura:\n", nP,162,161);
            pf("a)Primaria\nb)Secundaria\nc)Terciaria\nd)Cuaternaria\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Terciaria\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-C%cal grupo est%c presente en la estructura de la histidina\n", nP,163,160);
            pf("a)Guanidico\nb)Amino\nc)Sulfh%cdrilo\nd)Imidazol\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Imidazol\n");
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-El amino%ccido que en forma ionizada posee 5 %ctomos de carbono y uno de azufre es:\n", nP,160,160);
            pf("a)Glutamina\nb)Metionina\nc)Cistina\nd)Ciste%cna\n",161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b) Metionina\n");
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-La estructura secundaria en alfa-hélice se rompe cuando en la secuencia aparece:\n", nP);
            pf("a)Tirosina\nb)Fenilalanina\nc)Valina\nd)Prolina\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Prolina\n");
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Cuando se remueve el cofactor de una enzima activa, se obtiene una prote%cna catal%cticamente inactiva, la cual es llamada:\n", nP,161,161);
            pf("a)Holoenzima\nb)Apoenzima\nc)Proenzima\nd)Isoenzima\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b) Apoenzima\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Una reacci%cn qu%cmica catalizada por una enzima se activa cuando esta\n", nP,162,161);
            pf("a)Consigue un pH optimio\nb)Mantiene una cin%ctica de primer orden\nc)Opera en condiciones de saturaci%cn de sustrato\nd)Disminuye la energ%ca de activaci%cn de los reactivos\n",130,162,161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Disminuye su energ%ca de activaci%cn de los reactivos\n",161,162);
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-Considerando que la combusti%cn de la glucosa proporciona 686 Kcal y la hidrolisis de ATP aprox. 7 Kcal, En que margen se encontraria el rendimiento energ%ctico del catabolismo de 1 mol de glucosa\n", nP,162,130);
            pf("a)10-25%\nb)25-50%\nc)50-65%\nd)80-95%\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b) 25-50%\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-La activaci%cn y degradaci%cn de %ccidos grasos tiene lugar en:\n", nP,162,162,160);
            pf("a)matriz mitocondrial y citosol\nb)membrana mitocondrial externa y citosol\nc)matriz mitocondrial y peroxisoma\nd)membrana mitocondrial externa y matriz mitocondrial\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) membrana mitocondrial externa y matriz mitocondrial\n");
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.- Es la reacci%cn neta de la gluc%clisis aer%cbica:\n", nP,162,162,162);
            pf("a)Glucosa + 2ADP + 2Pi + 3NAD -> 2 piruvato + 2ATP + 3 NADH + 3H + 2H2O\nb)Glucosa + 2ADP + 2Pi + 2NAD ->2 lactato + 2ATP + 2 NADH + 2H + 2H2O\nc)Glucosa + 2ADP + 2Pi + 2NAD -> 2 piruvato + 2ATP + 2 NADH + 2H + 2H2O\nd)Glucosa + 2ADP + 2Pi + 3NAD -> 2 lactato + 2ATP + 3 NADH + 3H + 2H2O\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Glucosa + 2ADP + 2Pi + 2NAD -> 2 piruvato + 2ATP + 2 NADH + 2H + 2H2O\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Aceptor de hidr%cgenos provenientes del succinato:\n", nP,162);
            pf("a)FAD+EN\nb)NAD+\nc)FMN\nd)Coeinzima A\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a) FAD+\n");
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Cuantos ATP se forman en la oxidaci%cn de la lactosa hasta CO2 y H2O:\n", nP,162);
            pf("a)32\nb)56\nc)60\nd)72\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) 72\n");
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-Es el precursor anterior del cetogluatarato en el ciclo de Krebs.\n", nP);
            pf("a)Fumarato\nb)Aconinato\nc)Isocitrato\nd)Succinato\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Isocitrato\n");
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-Si un %ccido graso tiene 20 carbonos, Cuantos ciclos de  oxidaci%cn puede sufrir.\n", nP,160,162);
            pf("a)9\nb)10\nc)18\nd)20\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a) 9\n");
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Antes de ser usados como fuente de energ%ca, todos los amino%ccidos deben sufrir:\n", nP,161,160);
            pf("a)Transaminacion\nb)Desaminacion\nc)Oxidacion\nd)Hidrolisis\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a) Transaminacion\n");
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Donde suceden las reacciones luminosas de la fotosintes%cs\n", nP,161);
            pf("a)En las cel%clas guardianas del estoma\nb)En el estroma de del cloroplasto\nc)Dentro de las membranas tilacoidales de los cloroplastos\nd)En el citoplasma celular de la hoja\n",163);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Dentro de las membranas tilacoidales de los cloroplastos\n");
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-El papel de los pigmentos accesorios es:\n", nP);
            pf("a)Proporcionar un fotosistema adicional para generar m%cs ATP\nb)Permitir que la fotos%cntesis ocurra en la oscuridad\nc)Donar electrones a los centros de reacci%cn de la clorofila\nd)Captar energ%ca luminosa adicional y transferirla a los centros de reacci%cn de la clorofila\n",160,161,162,161,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) Captar energ%ca luminosa adicional y transferirla a los centros de reacci%cn de la clorofila\n",161,162);
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-Un gene a lo largo del DNA tiene la siguiente secuencia de bases AAATTTGGGCCC. Cu%cl ser%c la secuencia resultante del proceso de transcripci%cn\n", nP,160,160,162);
            pf("a)TTTAAACCCGGG\nb)AAAUUUGGGCCC\nc)AAATTTGGGCCC\nd)UUUAAACCCGGG\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) UUUAAACCCGGG\n");
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Si a una c%clula se le quitara el aparato de Golgi, Que proceso se ver%ca principalmente afectado\n", nP,130,161);
            pf("a)La producci%cn de ATP\nb)La s%cntesis de carbohidratos\nc)La divisi%cn celular\nd)La secreci%cn celular\n",162,161,162,162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d) La secreci%cn cel%clar\n",162,163);
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-Son componentes del citoesqueleto \n", nP);
            pf("a)Actina y miosina\nb)Vimentina y actinina alfa\nc)Microfilamentos, microt%cbulos y filamentos intermedios\nd)Calmodulina y miosina II\n",163);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c) Microfilamentos, microt%cbulos y filamentos intermedios\n",163);
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-Cual de los siguientes organismos tendra la mayor proporciocn de acidos grasos insaturados en sus membranas\n", nP);
            pf("a)Un pez en el %crtico\nb)Una planta des%crtica\nc)Una bacteria term%cfila\nd)El humano\n",160,130,132);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a) Un pez en el %crtico\n",160);
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Aciertos:%i\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int habV(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
        case 1:
            pf("%i.-Sin%cnimo de Panfleto\n",nP,162);
            pf("a)Barullo\nb)Libreto\nc)Men%c\nd)Folleto\n",163);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Folleto\n");
            system("pause");
            limpiar;
        break;
        case 2:
            pf("%i.-Sin%cnimo de Baldosa\n",nP,162);
            pf("a)Azulejo\nb)Placa\nc)Piso\nd)Pared\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Azulejo\n");
            system("pause");
            limpiar;
        break;
        case 3:
            pf("%i.-Sin%cnimo de Crespo\n",nP,162);
            pf("a)Liso\nb)Suave\nc)Ensortijado\nd)Largo\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Ensortijado\n");
            system("pause");
            limpiar;
        break;
        case 4:
            pf("%i.-Ant%cnimo de Ce%cir\n",nP,162,164);
            pf("a)Atar\nb)Apretar\nc)Aflojar\nd)Arrugar\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Aflojar\n");
            system("pause");
            limpiar;
        break;
        case 5:
            pf("%i.-Ant%cnimo de Postizo\n",nP,162);
            pf("a)Sobrepuesto\nb)Real\nc)Enga%coso\nd)Fingido\n",164);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Real\n");
            system("pause");
            limpiar;
        break;
        case 6:
            pf("%i.-Ant%cnimo de Enigma\n",nP,162);
            pf("a)Inc%cgnita\nb)Secreto\nc)Misterio\nd)Clave\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Clave\n");
            system("pause");
            limpiar;
        break;
        case 7:
            pf("%i.-Completar la siguiente frase: Quien con lobos anda...\n",nP);
            pf("a)no se le ve colmillo.\nb)nada de provecho saca.\nc)ni se haga ni se aprenda.\nd)a aullar se ense%ca.\n",164);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)a aullar se ense%ca.\n",164);
            system("pause");
            limpiar;
        break;
        case 8:
            pf("%i.-Completar la siguiente frase: El que a buen %crbol se arrima...\n",nP,160);
            pf("a)buena sombra le cobija.\nb)buen futuro se le avecina.\nc)nunca es buen cazador.\nd)se echa a dormir.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)buena sombra le cobija.\n");
            system("pause");
            limpiar;
        break;
        case 9:
            pf("%i.-Completar la siguiente frase: Cuando uno quiere...\n",nP);
            pf("a)el sol sale para todos.\nb)dos no pelean.\nc)da dos veces.\nd)todo se consigue.\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)dos no pelean.\n");
            system("pause");
            limpiar;
        break;
        case 10:
            pf("%i.-Completar la analog%ca: Pez es a Cardumen como...\n",nP,161);
            pf("a)Ave es a Parvada\nb)Gato es a Perro\nc)P%cjaro es a Alas\nd)Agua a Botella\n",160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Ave es a Parvada\n");
            system("pause");
            limpiar;
        break;
        case 11:
            pf("%i.-Completa la analog%ca: Acuario es a Pez como: \n",nP,161);
            pf("a)Caballo es a Campo\nb)Granja es a Pollo\nc)Techo a Hogar\nd)Taza es a Caf%c\n",130);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Granja es a Pollo\n");
            system("pause");
            limpiar;
        break;
        case 12:
            pf("%i.-Completa la analog%ca: Sill%cn es a Reposo como: \n",nP,161,162);
            pf("a)Alumno es a Escuela\nb)Parque es a Distracci%cn\nc)Medicina es a Farmacia\nd)Papel es a L%cpiz\n",162,160);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Parque es a Distracci%cn\n",160);
            system("pause");
            limpiar;
        break;
        case 13:
            pf("%i.-Completa de forma congruente la oraci%cn: Se puede reclamar una reparaci%cn sin costo si...\n",nP,162,162);
            pf("a)ya se venci%c la garant%ca.\nb)no se cuenta con un seguro.\nc)esta en perfectas condiciones.\nd)aun est%c vigente la garant%ca.\n",162,161,160,161);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Aun esta vigente la garantia.\n");
            system("pause");
            limpiar;
        break;
        case 14:
            pf("%i.-Completa de forma congruente la oraci%cn: Para una buena educaci%cn de los hijos, ambos padres deben tener _____________ en el hogar.\n",nP,162,162);
            pf("a)Desagrado\nb)Dependencia\nc)Autoridad\nd)Sumisi%cn\n",162);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Autoridad\n");
            system("pause");
            limpiar;
        break;
        case 15:
            pf("%i.-Completa de forma congruente la oraci%cn: La adversidad revela el genio, la prosperidad lo _____________?\n",nP,162);
            pf("a)Compensa\nb)Esconde\nc)Equilibra\nd)Supera\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Esconde\n");
            system("pause");
            limpiar;
        break;
        case 16:
            pf("%i.-Completa de forma congruente la oraci%cn: Si quieres hacer la paz, no hables con tus amigos; habla a tus ____________\n",nP,162);
            pf("a)Enemigos\nb)Allegados\nc)Parientes\nd)Aliados\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Enemigos\n");
            system("pause");
            limpiar;
        break;
        case 17:
            pf("%i.-Completa de forma congruente la oraci%cn: La pereza viaja tan despacio, que la pobreza no tarda en ______________\n",nP,162);
            pf("a)Opacarla\nb)Atenuarla\nc)Revelarla\nd)Alcanzarla\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Alcanzarla\n");
            system("pause");
            limpiar;
        break;
        case 18:
            pf("%i.-Completa de forma congruente la oraci%cn: Saber lo que es justo y no hacerlo es la peor de las _____________\n",nP,162);
            pf("a)Cobardias\nb)Elecciones\nc)Desgracias\nd)Alternativas\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Cobardías\n");
            system("pause");
            limpiar;
        break;
        case 19:
            pf("%i.-Sin%cnimo de Denigrar: \n",nP,162);
            pf("a)Enaltecer\nb)Admirar\nc)Enga%car\nd)Difamar\n",164);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)Difamar\n");
            system("pause");
            limpiar;
        break;
        case 20:
            pf("%i.-Sin%cnimo de Bancarrota\n",nP,162);
            pf("a)Ruina\nb)Auge\nc)Bonanza\nd)Desabasto\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("Respuesta correcta: a)Ruina\n");
            system("pause");
            limpiar;
        break;
        case 21:
            pf("%i.-Ant%cnimo de Cansar: \n",nP,162);
            pf("a)Acelerar\nb)Ascender\nc)Vigorizar\nd)Entorpecer\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)Vigorizar\n");
            system("pause");
            limpiar;
        break;
        case 22:
            pf("%i.-Ant%cnimo de Libertador: \n",nP,162);
            pf("a)Juez\nb)Tirano\nc)Oprimido\nd)Lugarteniente\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("Respuesta correcta: b)Tirano\n");
            system("pause");
            limpiar;
        break;
        case 23:
            pf("%i.-Completar la siguiente frase: Quien m%cs sabe...\n",nP,160);
            pf("a)no le dan autoridad\nb)mas puede y mas quiere\nc)yerra menos\nd)mayores dudas tiene\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("Respuesta correcta: d)mayores dudas tiene.\n");
            system("pause");
            limpiar;
        break;
        case 24:
            pf("%i.-Completar la siguiente frase: En el peligro... \n",nP);
            pf("a)no hay necesidad de ense%car al gato a ara%car.\nb)pocas palabras bastan.\nc)se conoce al amigo.\nd)vale prevenir que lamentar.\n",164,164);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("Respuesta correcta: c)se conoce al amigo.\n");
            system("pause");
            limpiar;
        break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);// Imprime los acierto y retorna valor
    system("pause");
    return aci;
}
int geo(int num[], int n)
{
    int i, nP , aci=0;
    char opc='\0';
    for(i=0, nP=1;i<n;i++, nP++)
    {
        switch(num[i])
        {
            case 1:
            pf("%i-C%cmo se llama la linea imaginaria que pasa por el centro del Polo Norte y del Polo Sur?\n",nP, 162);
            pf ("a-primer eje\n");
            pf ("b-Eje Central\n");
            pf ("c-Meridiano de Grenwitch\n");
            pf ("d-Primer meridiano\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Primer Meridiano\n");
            system("pause");
            break;
            case 2:
            pf("%i.-Qu%C pa%Cses colindan al mar muerto?\n",nP,130, 161);
            pf ("a-Egipto, Sudan y Etrea\n");
            pf ("b-Rusia, Iran y Aserbyan\n");
            pf ("c-Israel Jordania y Palestina\n");
            pf ("d-Grecia y Turquia\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')//Aqui modifiquenlo por la respuesta correcta
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Israel Jordania y Palestina\n");
            system("pause");
            limpiar;
            break;
            case 3:
            pf("%i.-Cu%Cl es la ciudad mas antigua del mundo?\n",nP, 160);
            pf("a-Luxor\n");
            pf("b-Ur\n");
            pf("c-Biblos\n");
            pf("d-Jerico\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Jerico\n");
            system("pause");
            limpiar;
            break;
            case 4:
            pf("%i.-Cu%cl es el pa%Cs mas poblado del mundo?\n",nP, 160, 161);
            pf("a-China\n");
            pf("b-Indonesia\n");
            pf("c-Rusia\n");
            pf("d-India\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)China\n");
            system("pause");
            limpiar;
            break;
            case 5:
            pf("%i.-Cu%cl es el r%Co mas largo del mundo?\n",nP, 160, 161);
            pf ("a-Rio Nilo\n");
            pf ("b-Rio Grande\n");
            pf ("c-Rio Amazonas\n");
            pf ("d-Rio Congo\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Rio Nilo\n");
            system("pause");
            limpiar;
            break;
            case 6:
            pf("%i.-A qu%c se le conoce como Cinturon de Fuego?\n",nP, 130);
            pf ("a-Regi%cn volc%Cnica que rodea Hawuai\n", 162, 160);
            pf ("b-El apodo del volcan Kilawea\n");
            pf ("c-Una zona de la cuenca del Oceano Pac%cfico, donde se encuentra una intensa actividad sismica\n", 161);
            pf ("d-Region de volcanes sumergida en el mar\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='C' || opc=='c')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Una zona de la cuenca del Oceano Pac%cfico, donde se encuentra una intensa actividad sismica\n");
            system("pause");
            limpiar;
            break;
            case 7:
            pf("%i.-Cu%Cl es el estado mas pequeño del mundo?\n",nP, 160);
            pf ("a-Vaticano\n");
            pf ("b-Siracusa\n");
            pf ("c-Tuvalo\n");
            pf ("d-Monaco\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Vaticano\n");
            system("pause");
            limpiar;
            break;
            case 8:
            pf("%i.-Cu%Cl es el volc%Cn mas grande del mundo?\n",nP, 160, 160);
            pf ("a-Popocatepetl\n");
            pf ("b-Krakatoa\n");
            pf ("c-Mauna Loa\n");
            pf ("d-Etna\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Krakatoa\n");
            system("pause");
            limpiar;
            break;
            case 9:
            pf("%i.-Cu%cntos paises hay en el mundo?\n",nP, 160);
            pf ("a-183\n");
            pf ("b-210\n");
            pf ("c-177\n");
            pf ("d-196\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)196\n");
            system("pause");
            limpiar;
            break;
            case 10:
            pf("%i.-En que pa%Cs queda el grupo mas grande de geiseres del hemisferio sur llamados El Tatio?\n",nP, 161);
            pf ("a-Uruguay\n");
            pf ("b-Bolivia\n");
            pf ("c-Peru\n");
            pf ("d-Chile\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)Chile\n");
            system("pause");
            limpiar;
            break;
            case 11:
            pf("%i.-Cu%cl es el oceano m%Cs grande del mundo?\n",nP, 160, 160);
            pf ("a-Indico\n");
            pf ("b-Atlantico\n");
            pf ("c-Pac%Cfico\n", 161);
            pf ("d-%Crtico\n", 181);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Pac%Cfico\n", 161);
            system("pause");
            limpiar;
            break;
            case 12:
            pf("%i.-En d%Cnde se ubica el monte Kilimanjaro?\n",nP, 162);
            pf ("a-Australia\n");
            pf ("b-Tanzania\n");
            pf ("c-Zimbabwe\n");
            pf ("d-Peru\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Tanzania\n");
            system("pause");
            limpiar;
            break;
            case 13:
            pf("%i.-Cu%Cl es el lago de agua dulce mas grande del mundo?\n",nP, 160);
            pf ("a-Lago Superior\n");
            pf ("b-Lago Victoria\n");
            pf ("c-Lago Turkana\n");
            pf ("d-Lago Michigan\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='b')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Lago Victoria\n");
            system("pause");
            limpiar;
            break;
            case 14:
            pf("%i.-Cu%Cntos paises hay en Am%Crica Central?\n",nP, 160, 130);
            pf ("a-7\n");
            pf ("b-9\n");
            pf ("c-13\n");
            pf ("d-11\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)7\n");
            system("pause");
            limpiar;
            break;
            case 15:
            pf("%i.-Cu%Cl es el lugar mas seco del planeta?\n",nP, 160);
            pf ("a-Desierto de Nambia\n");
            pf ("b-Desierto de Atacama\n");
            pf ("c-Desierto de Sahara\n");
            pf ("d-Desierto de Gobi\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Desierto de Atacama\n");
            system("pause");
            limpiar;
            break;
            case 16:
           pf("%i.-Nigeria es un pa%Cs localizado en el ______ de %Cfrica\n",nP, 161, 181);
            pf ("a-Oeste\n");
            pf ("b-Sur\n");
            pf ("c-Norte\n");
            pf ("d-Noreste\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Norte\n");
            system("pause");
            limpiar;
            break;
            case 17:
            pf("%i.-Cu%cl es el tercer continente mas grande del mundo?\n",nP, 160);
            pf ("a-Australia\n");
            pf ("b-China\n");
            pf ("c-Am%crica\n", 130);
            pf ("d-%Cfrica\n", 181);
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='d' || opc=='D')
            {
                aci++;
            }
            pf("La repuesta correcta es: d)%Cfrica\n", 181);
            system("pause");
            limpiar;
            break;
            case 18:
            pf("%i.-Entre que paises se encuentra el estrecho de Bering?",nP);
            pf ("a-Roma e Italia\n");
            pf ("b-Alaska y Rusia\n");
            pf ("c-Finlandia y Suecia\n");
            pf ("d-Inglaterra y Francia\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Alaska y Rusia\n");
            system("pause");
            limpiar;
            break;
            case 19:
            pf("%i.-Qu%c ciudades se encuentran entre dos continentes?",nP, 130);
            pf ("a-Estambul,Moscu, Suez, Atyrau y Tokio\n");
            pf ("b-Estambul, Alyrau, Melboume y Tiplis\n");
            pf ("c-Estambul, Almeria, Suez, Atyrau, Oremburgo y Tokio\n");
            pf ("d-Estambul, Tiplis y Atyrau\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)Estambul, Almeria, Suez, Atyrau, Oremburgo y Tokio\n");
            system("pause");
            limpiar;
            break;
            case 20:
            pf("%i.-Cu%Cntos paises tiene Europa?\n",nP, 160);
            pf ("a-63\n");
            pf ("b-58\n");
            pf ("c-50\n");
            pf ("d-54\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)50\n");
            system("pause");
            limpiar;
            break;
            case 21:
            pf("%i.-Cu%Cl es el lugar mas fr%Co del mundo?\n",nP, 160, 161);
            pf ("a-Groelandia\n");
            pf ("b-Antartida\n");
            pf ("c-Alaska\n");
            pf ("d-Aldea de Omykason\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='b' || opc=='B')
            {
                aci++;
            }
            pf("La repuesta correcta es: b)Antartida\n");
            system("pause");
            limpiar;
            break;
            case 22:
            pf("%i.-Cu%Cl es la montaña mas alta de Am%Crica Latina?\n",nP, 160, 130);
            pf ("a-Aconcagua\n");
            pf ("b-Pico Cristobal\n");
            pf ("c-Navado Ojos del Salado\n");
            pf ("d-Monte Pissis\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)Aconcagua\n");
            system("pause");
            limpiar;
            break;
            case 23:
            pf("%i.-Cu%Cntos continentes hay en el planeta?\n", nP, 160);
            pf ("a-5\n");
            pf ("b-6\n");
            pf ("c-11\n");
            pf ("d-13\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='a' || opc=='A')
            {
                aci++;
            }
            pf("La repuesta correcta es: a)5\n");
            system("pause");
            limpiar;
            break;
            case 24:
            pf ("%i.-Cu%Cntos oceanos hay en la Tierra?\n",nP, 160);
            pf ("a-3\n");
            pf ("b-4\n");
            pf ("c-5\n");
            pf ("d-6\n");
            fflush(stdin);
            scanf("%c", &opc);
            if(opc=='c' || opc=='C')
            {
                aci++;
            }
            pf("La repuesta correcta es: c)5\n");
            system("pause");
            limpiar;
            break;
        }
    }
    pf("Tuviste %i aciertos\n\n", aci);
    system("pause");
    return aci;
}
void general(int num[], int n)
{
    FILE *datos;
    int acum=0;
    float porc;
    printf("Recomendaciones previas:\n\n");
    printf("*Evita distracciones\n");
    printf("*Considera el tiempo necesario\n");
    printf("*Si lo deseas apoyate de un diccionario\n");
    printf("*Recuerda que una vez iniciado el examen no podras interrumpir la simulacion\n\n");
    system("pause");
    limpiar;
    acum=mate(num, n)+esp(num, n)+histM(num, n)+hist(num, n)+fis(num,n)+formacion(num,n)+habM(num,n)+quim(num, n)+bio(num,n)+habV(num, n)+geo(num, n);//manda a llamar cada funcion de los examenes
    pf("Total de aciertos: %i de 132\n", acum);
    porc=acum*100;
    pf("Porcentaje de aciertos:%%%.2f\n", porc/132);
    //Muestra un mensaje dependiendo de lo que saco el usuario
    if(acum<70)
    {
        pf("Te hace falta estudiar :c\n");
    }
    else
    {
        if(acum<90)
        {
            pf("Vas muy bien!\n");
        }
        else
        {
            if(acum<110)
            {
                pf("Excelente :D\n");
            }
            else
            {
                pf("FELICIDADEEEEEEEEEEEEEEEEES!!!!!!!!!!!!\n");
            }

        }
    }
    system("pause");
    datos=fopen("DatosUsuario.txt", "a");
    fprintf(datos, "%i\n", acum);
    fclose(datos);
}
void portada()
{
    system("color F4");
    espacio;
    pf("                                                 BIENVENIDO AL\n                               SIMULADOR DE EXAMEN DE INGRESO AL BACHILLERATO!!!\n\n\n");
    pf("                                         ADVERTENCIAS Y RECOMENDACIONES:\n\n");
    pf("*Una vez iniciado un examen no podr%cs interrumpir el proceso o de lo contrario no se almacenar%cn tus resultados\n",160,160);
    pf("*S%clo deberas responder pulsando la letra correspondiente al inciso correcto (Y no toda la respuesta)\n",162);
    pf("*S%clo ingresa caracteres de la a) a la d), caso contrario se considerar%c como error\n",162);
    pf("*Revisa tu respuesta antes de presionar enter, despu%cs no podr%cs corregirla\n",130,160);
    pf("*Se recomienda realizar el examen en una sola sesi%cn\n",162);
    pf("*Se recomienda tener a la mano l%cpiz y papel para c%clculos\n",160,160);
    pf("*Si lo deseas puedes apoyarte de un diccionario\n");
    pf("*Realizar el examen en un ambiente tranquilo\n");
    pf("*Considera el tiempo necesario\n\n");
    pf("*EL %cXITO NO SE LOGRA CON LA SUERTE, ES EL RESULTADO DE UN ESFUERZO CONSTANTE\n\n",144);
    pf("Listo??? ");
    system("pause");
    limpiar;
}

