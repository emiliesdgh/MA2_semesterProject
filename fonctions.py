import ThymioStates
from ThymioStates import ThymioStates

from tdmclient import ClientAsync, aw
import numpy as np


def stop_program(Thymio) :

    Thymio.setLEDTop([32,32,32])

    Thymio.setSpeedLeft(0)
    Thymio.setSpeedRight(0)


def see_costume(Thymio, motor_speed=0) :

    Thymio.setSpeedLeft(motor_speed)
    Thymio.setSpeedRight(motor_speed)


def auto_ext_interaction(Thymio, i, motor_speed=100) :

    if(i == 2) and (Thymio.auto) :
        Thymio.auto = False

    elif(i == 2) and (not Thymio.auto) :
        Thymio.auto = True

    if(Thymio.auto) :
        Thymio.setSpeedLeft(-motor_speed)
        Thymio.setSpeedRight(motor_speed)

    elif(not Thymio.auto) :
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(-motor_speed)


def auto_forward_backward(Thymio, i, motor_speed=100) :

    if(i == 2) and (Thymio.auto) :
        Thymio.auto = False

    elif(i == 2) and (not Thymio.auto) :
        Thymio.auto = True

    if(Thymio.auto) :
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(motor_speed)

    elif(not Thymio.auto) :
        Thymio.setSpeedLeft(-motor_speed)
        Thymio.setSpeedRight(-motor_speed)


def ext_interaction(Thymio, motor_speed=100) :

    if(Thymio.prox[5] > 2000) and (Thymio.prox[5] > 2000) :

        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(motor_speed)

    if (Thymio.prox[5] + Thymio.prox[6] < 6000) :

        if Thymio.prox[5] > Thymio.prox[6] :

            Thymio.setSpeedLeft(motor_speed)
            Thymio.setSpeedRight(-motor_speed)

        elif Thymio.prox[6] > Thymio.prox[5] : 

            Thymio.setSpeedLeft(-motor_speed)
            Thymio.setSpeedRight(motor_speed)

        elif Thymio.prox[0]+Thymio.prox[1] > Thymio.prox[3] + Thymio.prox[4] :

            Thymio.setSpeedLeft(-motor_speed)
            Thymio.setSpeedRight(motor_speed)

        elif Thymio.prox[0]+Thymio.prox[1] < Thymio.prox[3] + Thymio.prox[4] :

            Thymio.setSpeedLeft(motor_speed)
            Thymio.setSpeedRight(-motor_speed)

        elif Thymio.prox[2] > (Thymio.prox[0] or Thymio.prox[1] or Thymio.prox[3] or Thymio.prox[4]) :

            Thymio.setSpeedLeft(-motor_speed)
            Thymio.setSpeedRight(-motor_speed)

        else :

            Thymio.setSpeedLeft(0)
            Thymio.setSpeedRight(0)


def accelerometer_effect(Thymio, motor_speed=100) :

    # print(accel[0]) 
    # max droite  : -18 - -20
    # max gauche : 22 - 25
    # max devant derrière : rien
    # ~2-3 quand a plat, augmente + quand penché côté senseur 6, 
    # augmente - quand penché côté senseur 5, change pas quand penché avant arrière

    # print(accel[1])
    # max gauche  droite :  rien
    # max devant : - 21 - -22
    # max derrière : 20 - 22
    #  ~-1,0,1 quand horizontal, change pas quand penché droite, gauche
    # augment + quand penché en arrière, augmente - quand penché en avant

    # print(accel[2])
    # max droite : -1 - 1
    # max gauche : 0 - 1
    # max devant : 0 - 1
    # max derrière : -2 - 0
    # ~-20,-21 quand horizontal sur le dos, diminue - quand placé sur les côtés


    # GAUCHE
    if Thymio.accel[0] > 4: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop([0,0,32])
        # on the side
        Thymio.setSpeedLeft(0)
        Thymio.setSpeedRight(motor_speed)

    # DROITE
    if Thymio.accel[0]< -2: #Thymio is blue when placed on one of its sides
        Thymio.setLEDTop([0,0,32])
        # on the side
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(0)

    # DERRIERE
    if Thymio.accel[1] > 2: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop([32,0,0])
        # on back
        Thymio.setSpeedLeft(-motor_speed)
        Thymio.setSpeedRight(-motor_speed)

    # DEVANT
    if Thymio.accel[1]< -2: #Thymio is red when placed on its front or backside
        Thymio.setLEDTop([32,0,0])
        # on front
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(motor_speed)

    if Thymio.accel[2] > 18 or Thymio.accel[2] < -18: #Thymio is green when placed on its wheels or upside-down
        Thymio.setLEDTop([0,32,0])
        # horizontal
        Thymio.setSpeedLeft(0)
        Thymio.setSpeedRight(0)


def autoTurn(Thymio, motor_speed=50) :

    if (Thymio.prox > [0,0,0,0,0,0,2000]) :
        
        if (Thymio.variable) :

            Thymio.variable = False

            Thymio.setSpeedLeft(-motor_speed)
            Thymio.setSpeedRight(motor_speed)
        
    if (Thymio.prox > [2000,0,0,0,0,0]) :

        if (not Thymio.variable) :

            Thymio.variable = True

            Thymio.setSpeedLeft(motor_speed)
            Thymio.setSpeedRight(-motor_speed)


    if Thymio.variable : #Clockwise
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(-motor_speed)
    
    elif not Thymio.variable : #ConterClockwise
        Thymio.setSpeedLeft(-motor_speed)
        Thymio.setSpeedRight(motor_speed)


def microphone(Thymio, client, motor_speed=50) :

    print(Thymio.mic)
    if Thymio.microphone_set and Thymio.mic>20 :
        Thymio.setSpeedLeft(-motor_speed)
        Thymio.setSpeedRight(motor_speed)

        aw(client.sleep(2))

        Thymio.setSpeedLeft(0)
        Thymio.setSpeedRight(0)

        Thymio.microphone_set = 0

    elif (not Thymio.microphone_set) and Thymio.mic>20 :
        Thymio.setSpeedLeft(motor_speed)
        Thymio.setSpeedRight(-motor_speed)

        aw(client.sleep(2))

        Thymio.setSpeedLeft(0)
        Thymio.setSpeedRight(0)

        Thymio.microphone_set = 1


def no_costume(Thymio, motor_speed=0) :

    Thymio.setSpeedLeft(motor_speed)
    Thymio.setSpeedRight(motor_speed)


def programFront (Thymio, client) :

    Thymio.setLEDTop([20,0,32])
    color = [0,0,0,0,0,0,0,0]
    Thymio.setLEDCircle(color)

    Thymio.setSpeedLeft(50)
    Thymio.setSpeedRight(-50)

    aw(client.sleep(2))

    Thymio.setSpeedLeft(-50)
    Thymio.setSpeedRight(50)

    aw(client.sleep(2))
    

def programBack (Thymio) :

    if (Thymio.prox[5]>1000 and Thymio.prox[6]>1000 and Thymio.prox_ground[0]>10) :

        Thymio.setLEDTop([20,0,32])
        color = [0,0,0,0,0,0,0,0]
        Thymio.setLEDCircle(color)

        Thymio.setSpeedLeft(50)
        Thymio.setSpeedRight(50)