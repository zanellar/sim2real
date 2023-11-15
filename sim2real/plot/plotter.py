from matplotlib import pyplot as plt
import numpy as np
import json
import os

from sim2real.utils.pkgpaths import PkgPath

class Plotter():

    def __init__(self):
        self.data = None

    def load_data(self, file_name):
        '''
        Load data from log file.
        '''
        self.data = []  
        log_file = os.path.join(PkgPath.LOGS, file_name)

        with open(log_file, "r") as f:
            for line in f:
                self.data.append(json.loads(line)) 

    def plot(self):
        '''
        Plot end-effector position and joint positions.
        '''
        eef_pos = np.array([d["eef_pos"] for d in self.data])
        action = np.array([d["action"] for d in self.data])
        joint_torque = np.array([d["joint_torque"] for d in self.data])

        fig = plt.figure()

        # subplot 1
        plt.subplot(3, 1, 1)
        plt.title("End-effector position")
        plt.plot(eef_pos)
        plt.legend(["x", "y", "z"])
        plt.xlabel("time")
        plt.ylabel("position")
        plt.grid()
        # plt.tight_layout() 

        # subplot 2
        plt.subplot(3, 1, 2)
        plt.title("Action")
        plt.plot(action)
        plt.legend(["j1", "j2", "j3", "j4", "j5", "j6", "j7"])
        plt.xlabel("time")
        plt.ylabel("position")
        plt.grid()
        # plt.tight_layout()

        # subplot 3
        plt.subplot(3, 1, 3)
        plt.title("Joint Torque")
        plt.plot(joint_torque)
        plt.legend(["j1", "j2", "j3", "j4", "j5", "j6", "j7"])
        plt.xlabel("time")
        plt.ylabel("torque")
        plt.grid()  
        # plt.tight_layout()

        plt.show()