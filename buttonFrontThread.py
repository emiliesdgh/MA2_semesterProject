import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np
import fonctions
import threading
import random


class ButtonFrontThread(threading.Thread):
    def __init__(self, event_list_thread, robot):
        super(ButtonFrontThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.client = ClientAsync()
        self.node = aw(self.client.wait_for_node())

        self.robot = robot

        self.random_integer = 0
        # self.robot.leftNOTright = robot.leftNOTright
        self.i = 0

    def run(self):
        self.stop = False

        self.random_integer = random.randint(1,5)

        while not self.stop:

            if(self.robot.button_forward) :

                self.random_integer = random.randint(1,5)


            color = [24,0,0,0,0,0,0,0]
            self.robot.setLEDCircle(color) 

            self.robot.setLEDTop([32,0,32])

            print(self.random_integer)

            # fonctions.no_costume(self.robot, motor_speed=0)

            if(self.random_integer == 1) :
                color = [24,24,0,0,0,0,0,0]
                self.robot.setLEDCircle(color) 

                self.i = self.i + 1

                fonctions.auto_ext_interaction(self.robot, self.i, motor_speed=100)
                
                if(self.i == 3) :
                    self.i = 0
            
            elif(self.random_integer == 2) :
                color = [24,0,24,0,0,0,0,0]
                self.robot.setLEDCircle(color) 

                self.i = self.i + 1

                fonctions.auto_forward_backward(self.robot, self.i, motor_speed=100)
                
                if(self.i == 3) :
                    self.i = 0

            elif(self.random_integer == 3) :
                color = [24,0,0,24,0,0,0,0]
                self.robot.setLEDCircle(color) 

            elif(self.random_integer == 4) :
                color = [24,0,0,0,24,0,0,0]
                self.robot.setLEDCircle(color) 

            elif(self.random_integer == 5) :
                color = [24,0,0,0,0,24,0,0]
                self.robot.setLEDCircle(color) 

    def kill(self):
        self.stop = True