#“We all are made of stars (WAAMOS)”
#Integrantes: Ignacio Bittner, Diego Mancilla, Matias Espinoza
import random 
my_list = [" "," ","´"," ","*"," "," "] #Lista 0,1,2,3,4
for i in range (20):
    for i in range (80):
        x=random.randint(0,6) #Funcion que elige un numero aleatorio entre 0 y 6
        y=my_list[x]
        print (y,end="")
    print ("\n",end="")