

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

config_file_name = "config_mujoco_panda"  # TODO: choose config file name

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
# file_name = time.strftime("%Y-%m-%d-%H-%M-%S") + ".json"
file_name = "test.json" # TODO
log_file = os.path.join(PkgPath.LOGS, file_name)

# create controller
controller = RobotController(config)

action = controller.measure("joint_pos")[0:8] 

N = controller.config["max_episode_length"] 
for t in range(N):

    # send constant action
    if t < N//2:
        action += 0.0001*np.ones(len(action))
    else:
        action -= 0.0001*np.ones(len(action)) 
        
    controller.execute(action)

    # measure end-effector position
    eef_pos = controller.measure("eef_pos") 
    joint_torque = controller.measure("joint_torque")

    print("@@@@@@@@@@@@@@@@")
    print("t", t)
    print("eef_pos", eef_pos)
    print("action", action)
    print("joint_pos", joint_torque)
    print("joint_torque", joint_torque)

    # save to file 
    data = {
        "eef_pos": eef_pos.tolist(),
        "joint_torque": joint_torque.tolist(),
        "action": action.tolist(),
    }
    with open(log_file, "a") as f:
        json.dump(data, f)
        f.write("\n")
 