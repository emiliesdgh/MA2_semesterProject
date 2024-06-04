import ThymioStates
from ThymioStates import ThymioStates

from tdmclient import ClientAsync, aw

import numpy as np


client = ClientAsync()
node = aw(client.wait_for_node())

# aw(node.lock())
aw(node.wait_for_variables())

robot = ThymioStates()

def update_sensors_data(robot):

    # get button values
    robot.update()

def stop_program(robot, motor_speed=0) :

    robot.setLEDTop([0,0,0])

    robot.setSpeedLeft(motor_speed)
    robot.setSpeedRight(motor_speed)

def accelerometer_effect(robot, motor_speed=100) :
    # accel = list(node["acc"]) + [0]

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
    if robot.accel[0] > 4: #Thymio is blue when placed on one of its sides
        robot.setLEDTop([0,0,32])
        # on the side
        robot.setSpeedLeft(0)
        robot.setSpeedRight(motor_speed)

    # DROITE
    if robot.accel[0]< -2: #Thymio is blue when placed on one of its sides
        robot.setLEDTop([0,0,32])
        # on the side
        robot.setSpeedLeft(motor_speed)
        robot.setSpeedRight(0)

    # DERRIERE
    if robot.accel[1] > 2: #Thymio is red when placed on its front or backside
        robot.setLEDTop([32,0,0])
        # on back
        robot.setSpeedLeft(-motor_speed)
        robot.setSpeedRight(-motor_speed)

    # DEVANT
    if robot.accel[1]< -2: #Thymio is red when placed on its front or backside
        robot.setLEDTop([32,0,0])
        # on front
        robot.setSpeedLeft(motor_speed)
        robot.setSpeedRight(motor_speed)

    if robot.accel[2] > 18 or robot.accel[2] < -18: #Thymio is green when placed on its wheels or upside-down
        robot.setLEDTop([0,32,0])
        # horizontal
        robot.setSpeedLeft(0)
        robot.setSpeedRight(0)


while(1) :

    update_sensors_data(robot)

    accelerometer_effect(robot, motor_speed=100)

    if (robot.button_center) :

        print("Program stopped")
        stop_program(robot, motor_speed=0)
        aw(node.unlock())
        break