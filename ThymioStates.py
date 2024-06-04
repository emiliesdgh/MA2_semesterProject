from tdmclient import ClientAsync, aw

import numpy as np

class ThymioStates :

    def __init__ (self) :

        self.button_center = 0
        self.button_forward = 0
        self.button_backward = 0
        self.button_right = 0
        self.button_left = 0

        self.variable = True

        self.leftNOTright = True

        self.auto = True

        self.allButtons = []

        self.client = ClientAsync()
        self.node = aw(self.client.wait_for_node())

        aw(self.node.lock())
        aw(self.node.wait_for_variables())

    def update(self):

        self.node = aw(self.client.wait_for_node())

        self.button_center = self.node.v.button.center
        self.button_forward = self.node.v.button.forward
        self.button_left = self.node.v.button.left
        self.button_right = self.node.v.button.right
        self.button_backward = self.node.v.button.backward

        self.allButtons = [self.node.v.button.center, self.node.v.button.forward, self.node.v.button.left, self.node.v.button.right, self.node.v.button.backward]

        self.accel = list(self.node["acc"])

        self.mic = self.node.v.mic.intensity
        
        self.prox = list(self.node["prox.horizontal"])
        self.prox_ground = list(self.node["prox.ground.ambiant"])
        
        self.motor_left_speed = self.node["motor.left.speed"]
        self.motor_right_speed = self.node["motor.right.speed"]

    def __del__(self):
        aw(self.node.unlock())

    def setLEDCircle(self, color):
        
        ledCircle = {"leds.circle" : color}
        aw(self.node.set_variables(ledCircle))

    def setLEDTop(self, color):

        ledTop = {"leds.top" : color}
        aw(self.node.set_variables(ledTop))

    def setSpeedLeft(self,speed):
        
        self.motor_target_left=speed
        aw(self.node.set_variables({"motor.left.target": [speed]}))
    
    def setSpeedRight(self,speed):
        self.motor_target_right=speed
        aw(self.node.set_variables({"motor.right.target": [speed]}))