import ThymioStates
from ThymioStates import ThymioStates

from EventListThread import EventListThread

from buttonCenterThread import ButtonCenterThread
from buttonFrontThread import ButtonFrontThread
from buttonBackThread import ButtonBackThread
from buttonRightThread import ButtonRightThread
from buttonLeftThread import ButtonLeftThread

from tdmclient import ClientAsync, aw

import numpy as np
import fonctions

client = ClientAsync()
node = aw(client.wait_for_node())

aw(node.wait_for_variables())


if __name__ == "__main__":
    try:
        robot = ThymioStates()

        # Create an instance of the EventListThread
        event_list_thread = EventListThread(robot)

        # Start event list thread
        event_list_thread.start()
        
        program = None

        while True :

            if (robot.allButtons):

                if (program is not None) and (robot.button_center) :

                    program.kill()
                    program = None
                    fonctions.stop_program(robot)
                    robot.setLEDTop([0,0,0])
                    robot.setLEDCircle([0,0,0,0,0,0,0,0])

                if (program is None) and (robot.button_center):

                    program = ButtonCenterThread(event_list_thread, robot)
                    program.start()

                elif (program is None) and (robot.button_forward):

                    program = ButtonFrontThread(event_list_thread, robot)
                    program.start()

                elif (program is None) and (robot.button_backward):

                    program = ButtonBackThread(event_list_thread, robot, node)
                    program.start()

                elif (program is None) and (robot.button_right):

                    program = ButtonRightThread(event_list_thread, robot, node)
                    program.start()

                elif (program is None) and (robot.button_left):

                    program = ButtonLeftThread(event_list_thread, robot)
                    program.start()
           
    except Exception as e:
        print(e)
        event_list_thread.kill()