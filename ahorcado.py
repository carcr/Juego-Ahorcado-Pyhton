####################################
###########JUEGO AHORCADO###########
####################################

###IMPORTS
import random,os,getpass,ahorcadoDraw
'''
Importamos random para sacar una palabra aleatoria del fichero.
Getpass lo utilizamos para que la palabra que escribamos por teclado no se pueda ver.
También importamos el archivo ahorcadoDaw.py que contiene un array con el dibujo del monigote.
'''



###############
###FUNCIONES###
###############

#FUNCION VISUALIZAR PALABRA JUEGO con '_'
def mostrarJuego(palabraOcultaVacia):
    '''
    Recibe el array con la palabra oculta vacia con guinos.
    Cada guion representa una letra.
    Nos muestra la palabra que tenemos que adivinar
    Por ejemplo 'HOLA' -> _ _ _ _ 
    '''
    print('\n\t\t',end=' ')
    for l in palabraOcultaVacia:
        print(l,end=' ')
    print('\n')

#Menu Selección VS MÁQUINA o JUGADOR
def seleccionarTipoDeJuego():
    '''
    Menu de selección de jugar contra la máquina u otro jugador
        1.-MAQUINA: Se elige una palara aleatoria de un fichero
        2.-JUGADOR: otra persona escribe la palabra oculta.
    Al pulsar la opcion salir se termina el programa
    '''
    menuTipoJuego='\n***SELECCIONA TIPO DE JUEGO***\n\t1.-VS MÁQUINA\n\t2.-VS OTRO JUGADOR\n\t0.-SALIR'
    salirMenuTipoJuego=False
    global tipoJuego
    global jugarJuego
    global jugarPalabra

    global siguienteMenuTema
    global siguienteMenuDificultad

    while salirMenuTipoJuego==False:
        salirMenuTipoJuego=True
        print(menuTipoJuego)
        inputOpcionTipoJuego=input('Elige una opción\t')
        if inputOpcionTipoJuego=='1':
            tipoJuego='maquina'
        elif inputOpcionTipoJuego=='2':

            tipoJuego='persona'
            siguienteMenuTema=False

        elif inputOpcionTipoJuego=='0':

            print('\n**FIN DEL PROGRAMA**')
            jugarJuego=False
            jugarPalabra=False

            siguienteMenuTema=False
            siguienteMenuDificultad=False

        else:
            os.system('cls')
            print('\nEscoge una opción correcta')
            salirMenuTipoJuego=False
    os.system('cls')

#Escribir palabra OTRO JUGADOR
def escribirPalabraOtroJugador():
    '''
    Pide una palabra al usuario.
    Si la palabra contiene algun caracter que no esté entre [a-z] y [A-Z] la vuelve a pedir.
    Devuelve la palabra oculta introducida.
    '''

    #BUCLE HASTA QUE LAS PALABRAS INTRODUCIDAS SEANN IGUALES
    while True:

        #INTROUDCCIÓN PALABRA 1
        while True:
            #inputPalabraOculta=str(input('Introduce una palabra:\t'))
            inputPalabraOculta=getpass.getpass(prompt='Introduce una palabra:\t') 
            contadorCorrecto=0
            for i in inputPalabraOculta:
                letra=ord(i)
                if (letra>=65 and letra<=90) or (letra>=97 and letra<=122) or letra==32 or (letra>=48 and letra<=57):
                    contadorCorrecto+=1
            if contadorCorrecto!=len(inputPalabraOculta):
                print('La palabra no puede tener carácteres extraños')
                continue
            else:
                break
        
        #INTROUDCCIÓN PALABRA 2
        while True:
            #inputPalabraOculta=str(input('Introduce una palabra:\t'))
            inputPalabraOculta2=getpass.getpass(prompt='Introduce otra vez la palabra:\t') 
            contadorCorrecto2=0
            for i in inputPalabraOculta2:
                letra2=ord(i)
                if (letra2>=65 and letra2<=90) or (letra2>=97 and letra2<=122) or letra2==32 or (letra>=48 and letra<=57):
                    contadorCorrecto2+=1
            if contadorCorrecto2!=len(inputPalabraOculta2):
                print('La palabra no puede tener carácteres extraños')
                continue
            else:
                break
        
        ##COMPROBACIÓN LAS 2 PALABRAS SON IGUALES
        if inputPalabraOculta!=inputPalabraOculta2:
            print('Las palabras no coinciden')
            continue
        else:
            break

    #DEVUELVE la palabra
    return inputPalabraOculta

#Mostrar MENU de selección TEMA
def menuTema():
    '''
    Modo de juego VS MÁQUINA
    Menú de selección del tema de palabras a adivinar.
    '''
    menuTema='\n***SELECCIONA TEMA***\n\t1.-ANIMALES\n\t2.-VEHICULOS\n\t3.-PAISES AFRICA\n\t4.-PAISES EUROPA'
    menuTema+='\n\t5.-PELÍCULAS\n\t6.-VIDEOJUEGOS\n\tJ.-TIPO\n\t0.-SALIR'
    salirMenuTema=False

    global temaPalabras
    global jugarJuego
    global jugarPalabra

    global siguienteMenuDificultad
    global siguienteMenuTipo

    while salirMenuTema==False:
        salirMenuTema=True
        print(menuTema)
        inputOpcionDif=input('Elige una opción\t')
        if inputOpcionDif=='1':
            temaPalabras='animales'
        elif inputOpcionDif=='2':
            temaPalabras='marcas'
        elif inputOpcionDif=='3':
            temaPalabras='paisesAfrica'
        elif inputOpcionDif=='4':
            temaPalabras='paisesEuropa'
        elif inputOpcionDif=='5':
            temaPalabras='peliculas'
        elif inputOpcionDif=='6':
            temaPalabras='videojuegos'
        elif inputOpcionDif=='j' or inputOpcionDif=='J':
            os.system('cls')

            jugarPalabra=False
            siguienteMenuDificultad=False
            siguienteMenuTipo=True

        elif inputOpcionDif=='0':

            print('\n**FIN DEL PROGRAMA**')            
            jugarPalabra=False
            jugarJuego=False

            siguienteMenuDificultad=False

        else:
            os.system('cls')
            print('\nEscoge una opción correcta')
            salirMenuTema=False
    os.system('cls')

#Mostrar MENU de selección DIFICULTAD
def menuDificultad():
    menuDificultadJugador='\n***SELECCIONA DIFICULTAD***\n\t1.-Fácil\n\t2.-Normal\n\t3.-Difícil\n\tJ.-TIPO\n\t0.-SALIR'
    menuDificultad='\n***SELECCIONA DIFICULTAD***\n\t1.-Fácil\n\t2.-Normal\n\t3.-Difícil\n\t4.-Elegir TEMA\n\tJ.-TIPO\n\t0.-SALIR'
    salirMenuDificultad=False

    global numIntentosRestantes
    global jugarPalabra
    global jugarJuego

    global siguienteMenuTipo

    while salirMenuDificultad==False:
        salirMenuDificultad=True
        jugarPalabra=True
        if tipoJuego=='maquina':
            print(menuDificultad)
        else:
            print(menuDificultadJugador)
        inputOpcion=input('Elige una opción\t')
        if inputOpcion=='1':
            numIntentosRestantes=10
        elif inputOpcion=='2':
            numIntentosRestantes=7
        elif inputOpcion=='3':
            numIntentosRestantes=5
        elif inputOpcion=='4':

            os.system('cls') 
            jugarPalabra=False

            siguienteMenuTipo=False

        elif inputOpcion=='j' or inputOpcion=='J':
            os.system('cls')
            #siguienteMenuDificultad=False
            #volverElegirTipo=True
            jugarPalabra=False
        elif inputOpcion=='0':

            print('\n**FIN DEL PROGRAMA**')
            jugarPalabra=False
            jugarJuego=False

        else:
            os.system('cls')
            salirMenuDificultad=False            
            print('\nEscoge una opción correcta')

#Sacar PALABRA RANDOM de FICHERO
def sacarPalabraOculta (tema):
    '''
    Abrimos el fichero y metemos todo el conenido en un array
    De ese array sacamos una linea aleatoria(Solo hay 1 palabra en cada linea).
    Cerramos el fichero
    Devuelve la palabra oculta selecionada de manera aleatoria.
    '''
    filepath='c:/ahorcado/temas/'+tema+'.txt'
    fichero=open(filepath,'r')                              #Abrimos fichero
    allLines=fichero.readlines()                            #Array con todas las palabras por linea
    numLinea=random.randint(0,len(allLines)-1)              #Número Linea RANDOM
    palabraOculta=allLines[numLinea].upper()                #Pasamos la palabra a MAYUSCULAS 
    fichero.close()
    return palabraOculta

#CREACIÓN DE ARRAYS PALABRA OCULTA
def initArraysPalabras(palabraOcultaVacia,palabraOcultaArr,palabraOculta,tipoJuego):
    #Llenamos el array con '_'
    #print(palabraOculta)
    for i in palabraOculta:
        if i==' ':
            palabraOcultaArr.append(' ')
            palabraOcultaVacia.append(' ')
        else:           
            palabraOcultaArr.append(i)
            palabraOcultaVacia.append('_')
    
    #print(palabraOcultaVacia)
    #print(palabraOcultaArr)
    #BORRAMOS último elemento del array.EL SALTO DE LINEA de la palabra
    #Si no, nos apraecerá ['O','L','A','\n']

    #Vemos si jugamos contra la máquina y sacamos la palabra del fichero
    if tipoJuego=='maquina': 
        palabraOcultaVacia.pop()
        palabraOcultaArr.pop()

##JUEGO EN SI
def ahorcadoJuego(palabraAdivinada,numIntentosRestantes,palabraOcultaArr,palabraOcultaVacia):
    os.system('cls')
    mostrarJuego(palabraOcultaVacia)                        #Visualiza palabra
    print('**Tienes',numIntentosRestantes,'intentos**\n')
    letrasYaIntroducidas=[]  
    numIntentosUsados=0                                     #NUM INTENTOS usados
    
    ##UTILIZARARRAYS DEL OTRO ARCHIVO py
    if numIntentosRestantes==10:
        dibujo=ahorcadoDraw.AHORCADO_DRAW_10
    elif numIntentosRestantes==7:
        dibujo=ahorcadoDraw.AHORCADO_DRAW_7
    elif numIntentosRestantes==5:
        dibujo=ahorcadoDraw.AHORCADO_DRAW_5


    #CONDICIONES FINALIZAR JUEGO
    while palabraAdivinada==False and numIntentosRestantes>0:       #Adivanar o quedarse sin intentos
        
        #########################
        ##MOSTRAR AHORCADO DIBUJO
        #########################
        
        print(dibujo[numIntentosRestantes])

        #INPUT VALIDACIONES    
        while True:
            inputLetra=str(input('Introduce una letra:\t'))

             #VALIDACION de longitud de string. Si solo se ha introducido una letra
            if len(inputLetra)>1:                                   
                print('Introduce una letra')
                continue
            asciiInput=ord(inputLetra)      #ASCII del char

            #VALIDACION ASCII.Comprobar si se ha introducido una letra
            if (asciiInput>=65 and asciiInput<=90) or (asciiInput>=97 and asciiInput<=122) or (asciiInput>=48 and asciiInput<=57):
                break
            else:
                print('Introduce una letra')
        
        ##INIT variables de control
        letraEnPalabraVacia=False
        letraYaEscrita=False

        #BUSCAR en PALABRA la LETRA INTRODUCIDA
        for i,letra in enumerate(palabraOcultaArr):

            #COMPROBAR que se ENCUENTRA en la PALABRA OCULTA
            if inputLetra.upper()==letra:                    #Pasar a MAYUSCULAS la letra introducida
                letraEnPalabraVacia=True

                #COMPROBAR si ya esta DESVELADA
                if palabraOcultaVacia[i]=='_':
                    palabraOcultaVacia[i]=inputLetra.upper()
                    #comprobarLetrasYaEscritas(letrasYaEscritas,letra)
                    #letrasYaEscritas.append(letra)  
                else:
                    letraYaEscrita=True
        comprobarLetrasYaIntroducidas(letrasYaIntroducidas,inputLetra.upper())
        os.system('cls')

        ##COMPROBACION de FALLOS        
        if letraYaEscrita:
            print('\n- Letra ya escrita')
            #numIntentosRestantes-=1
            #numIntentosUsados+=1        
        
        if letraEnPalabraVacia==False:
            print('\n- Letra no encontrada')
            numIntentosRestantes-=1
            numIntentosUsados+=1

        ##COMPROBACION de si se ha ganado
        if palabraOcultaArr==palabraOcultaVacia:
            palabraAdivinada=True
        
        ###VISUALIZAR JUEGO     
        mostrarJuego(palabraOcultaVacia)       
        mostrarLetrasYaIntroducidas(letrasYaIntroducidas)
        print('Intentos restantes ->',numIntentosRestantes)


    ###RESULTADO FIN JUEGO     
    if palabraAdivinada:
        print('\n¡¡¡HAS GANDADO!!!')
        print('Nº de fallos:',numIntentosUsados)
    else:
        print('\n¡HAS PERDIDO! :(')
        print('La palabra oculta era:',palabraOculta)
        print(ahorcadoDraw.MUERTE[0])

#MOSTRAR LETRAS INTRODUCIDAS
def mostrarLetrasYaIntroducidas(letrasYaIntroducidas):
    print('\n\t',end=' ')
    print("LETRAS YA INTRODUCIDAS ->",end=' ')
    for l in letrasYaIntroducidas:
        print(l,end=' ')
    print('\n')

#COMPROBAR si LETRA INTRODUCIDA
def comprobarLetrasYaIntroducidas(letrasYaIntroducidas,letra):
    introducirLetra=True
    for i in letrasYaIntroducidas:
        if i==letra:
            introducirLetra=False
    if introducirLetra:
        letrasYaIntroducidas.append(letra)


#################################
#########INCIO PROGRAMA##########
#################################

###INIT VARIABLES y VAR CONTROL
palabraOcultaVacia=''
palabraAdivinada=False

tipoJuego=''                    #Tipo de JUEGO
temaPalabras=''                 #POOL de PALABRAS

siguienteMenuTipo=True          #ControlMENU
siguienteMenuTema=True          #ControlMENU
siguienteMenuDificultad=True    #ControlMENU
jugarPalabra=True               #JUGAR
jugarJuego=True                 #JUGAR

numIntentosRestantes=0



while jugarJuego:
    
    #### CONTROL DE MENÚS ####
    
    #siguienteMenuTipo=True          #ControlMENU
    siguienteMenuTema=True          #ControlMENU
    siguienteMenuDificultad=True    #ControlMENU

    if siguienteMenuTipo:                   #ELEIGR vs
        seleccionarTipoDeJuego()  

    if siguienteMenuTema:                   #VS MÁQUINA

        menuTema()

        if siguienteMenuDificultad:         #DIFICULTAD
            
            menuDificultad()

    else:                                   #VS JUGADOR

        if siguienteMenuDificultad:         #DIFICULTAD
            
            menuDificultad()
            
    #### CONTROL DE MENÚS ####
    
    if jugarPalabra:
        
        ###########INCIO JUEGO###########
        
        #CREACIÓN DE ARRAY PALABRA OCULTA
        palabraOcultaVacia=[]           #Array vacio que se imprime                    
        palabraOcultaArr=[]             #Array con palabra oculta
                             
        if tipoJuego=='maquina':
            palabraOculta=sacarPalabraOculta(temaPalabras)
        else:
            palabraOculta=escribirPalabraOtroJugador().upper()
        initArraysPalabras(palabraOcultaVacia,palabraOcultaArr,palabraOculta,tipoJuego)
        ahorcadoJuego(palabraAdivinada,numIntentosRestantes,palabraOcultaArr,palabraOcultaVacia)
        
        ############FIN JUEGO############
        
#################################
##########FIN PROGRAMA###########
#################################
