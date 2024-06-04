import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np
import fonctions
import threading


class ButtonLeftThread(threading.Thread):
    def __init__(self, event_list_thread, robot):
        super(ButtonLeftThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.robot = robot

    def run(self):
        self.stop = False
        while not self.stop:

            color = [0,0,0,0,0,0,24,0]
            self.robot.setLEDCircle(color) 
            
            self.robot.setLEDTop([0,0,32])

            fonctions.autoTurn(self.robot, motor_speed=50)

    def kill(self):
        self.stop = True