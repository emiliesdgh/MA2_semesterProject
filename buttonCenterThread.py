import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from tdmclient import ClientAsync, aw

import numpy as np
import fonctions
import threading


class ButtonCenterThread(threading.Thread):
    def __init__(self, event_list_thread, robot):
        super(ButtonCenterThread, self).__init__()
        self.event_list_thread = event_list_thread
        self.shutdown_event = threading.Event()  # Event to signal shutdown

        self.client = ClientAsync()
        self.node = aw(self.client.wait_for_node())

        self.robot = robot

    def run(self):
        self.stop = False
        while not self.stop:

            color = [24,24,24,24,24,24,24,24]
            self.robot.setLEDCircle(color) 

            fonctions.stop_program(self.robot)

    def kill(self):
        self.stop = True