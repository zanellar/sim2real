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
        plt.plot(eef_pos)
        plt.plot(action)
        plt.show()