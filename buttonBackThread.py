import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np
import fonctions
import threading


class ButtonBackThread(threading.Thread):
    def __init__(self, event_list_thread, robot, node):
        super(ButtonBackThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.robot = robot
        # self.node = node
        self.robot.leftNOTright = robot.leftNOTright

        self.i = 0

    def run(self):
        self.stop = False
        while not self.stop:

            color = [0,0,0,0,24,0,0,0]
            self.robot.setLEDCircle(color)

            self.robot.setLEDTop([32,0,0])

            if(self.robot.button_left) :

                self.robot.leftNOTright = True

                self.i = 0 
            
            elif(self.robot.button_right) :

                self.i = 0

                self.robot.leftNOTright = False
                color = [0,0,24,0,24,0,0,0]
                self.robot.setLEDCircle(color) 

            if(self.robot.leftNOTright) :

                self.i = self.i + 1

                fonctions.auto_ext_interaction(self.robot, self.i, motor_speed=100)
                
                if(self.i == 3) :
                    self.i = 0

                color = [0,0,0,0,24,0,24,0]
                self.robot.setLEDCircle(color)

            elif(not self.robot.leftNOTright) :

                color = [0,0,24,0,24,0,0,0]
                self.robot.setLEDCircle(color) 
                fonctions.ext_interaction(self.robot, motor_speed=100)


    def kill(self):
        self.stop = True