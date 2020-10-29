dividendo=int(input("Introduzca un divisor: "))     #SOLICITA VALOR
divisor=int(input("Introduzca un dividendo: "))     #SOLICITA VALOR
resto=dividendo     #RESTO ES DIVIDENDO
sol=0       #SOLUCIÓN

if divisor==0:      #DIVISOR 0
    print("El divisor es 0. No existe solución.")       #OUTPUT
else:
    while resto>=divisor:       #MIENTRAS EL RESTO SEA MAYOR O IGUAL AL DIVISOR
        resto=resto-divisor     #EL RESTO ES EL DIVIDENDO MENOS EL DIVISOR
        sol=sol+1       #COCIENTE

    print ("El cociente de la división es:",sol)       #OUTPUT