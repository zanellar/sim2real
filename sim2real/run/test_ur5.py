

'''
Constant value of position displacements are sent to each joint of the robot for a specified number of steps. 
The the opposite values are sent for the same number of steps. The end-effector position is recorded at each step 
and saved to a file toghether with the corresponding joint positions.   
'''

from sim2real.control.controller import RobotController
from sim2real.utils.pkgpaths import PkgPath
import numpy as np
import os
import time
import json

config_file_name = "config_mujoco"  # TODO: choose config file name

##############################################################################
##############################################################################
##############################################################################
# DO NOT MODIFY THE CODE BELOW
##############################################################################
##############################################################################
##############################################################################

# path to configuation file
config = os.path.join(PkgPath.CONFIGS, f"{config_file_name}.json")  

# path to log file (where the data will be saved) in format "yyyy-mm-dd-hh-mm-ss.json"
file_name = time.strftime("%Y-%m-%d-%H-%M-%S") + ".json"
log_file = os.path.join(PkgPath.LOGS, file_name)

# create controller
controller = RobotController(config)

action = np.zeros(7)
for t in range(controller.config["max_episode_length"]):

    # send constant action
    action = np.array([0.1, 0.1, 0.1, 0.1])
    controller.execute(action)

    # measure end-effector position
    eef_pos = controller.measure("eef_pos") 
    print(eef_pos)

    # save to file 
    data = {
        "eef_pos": eef_pos.tolist(),
        "action": action.tolist(),
    }
    with open(log_file, "a") as f:
        json.dump(data, f)
        f.write("\n")


