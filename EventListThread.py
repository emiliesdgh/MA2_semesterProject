import ThymioStates
from ThymioStates import ThymioStates

from tdmclient import ClientAsync, aw

import numpy as np
import threading
import queue

class EventListThread(threading.Thread):
    def __init__(self, robot):
        super(EventListThread, self).__init__()
        self.event_queue = queue.PriorityQueue()
        self.event_list = []
        self.event_list_lock = threading.Lock()  # Lock for protecting access to event list
        self.shutdown_event = threading.Event()  # Event to signal shutdown
        self.stop = True
        self.robot = robot

    def add_event(self, priority, event_data):

        self.event_queue.put((priority, event_data))

    def run(self):
        self.stop = False
        while not self.stop:

            self.robot.update()
            
            self.add_event(0, self.robot.button_center)
            self.add_event(1, self.robot.allButtons)
            self.add_event(2, self.robot.prox)
            self.add_event(3, self.robot.accel)
            self.add_event(4, self.robot.mic)
            
            while not self.event_queue.empty():
                priority, event_data = self.event_queue.get()
                # print("Event added with priority {}: {}".format(priority, event_data))       

    def kill(self):
        self.stop = True